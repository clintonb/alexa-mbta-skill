from __future__ import unicode_literals

import datetime
import itertools
import logging
import math
import os

import requests
from flask import Flask
from flask_ask import Ask, statement
from pytz import timezone

app = Flask(__name__)
# app.config['ASK_VERIFY_REQUESTS'] = False
ask = Ask(app, '/')
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

# TODO Pull location/timezone from user details
LATITUDE = 42.3698964
LONGITUDE = -71.0878818
TIMEZONE = timezone('US/Eastern')

APP_NAME = 'MBTA'
MBTA_API_KEY = os.environ['MBTA_API_KEY']

STATIONS = {
    'airport': 'place-aport',
    'alewife': 'place-alfcl',
    'andrew': 'place-andrw',
    'aquarium': 'place-aqucl',
    'ashmont': 'place-asmnl',
    'assembly': 'place-astao',
    'back bay': 'place-bbsta',
    'beachmont': 'place-bmmnl',
    'bowdoin': 'place-bomnl',
    'braintree': 'place-brntn',
    'broadway': 'place-brdwy',
    'central': 'place-cntsq',
    'charles m.g.h.': 'place-chmnl',
    'chinatown': 'place-chncl',
    'community college': 'place-ccmnl',
    'davis': 'place-davis',
    'downtown crossing': 'place-dwnxg',
    'fields corner': 'place-fldcr',
    'forest hills': 'place-forhl',
    'government center': 'place-gover',
    'green street': 'place-grnst',
    'harvard': 'place-harsq',
    'haymarket': 'place-haecl',
    'jackson square': 'place-jaksn',
    'jfk/umass': 'place-jfk',
    'kendall/mit': 'place-knncl',
    'malden center': 'place-mlmnl',
    'massachusetts ave.': 'place-masta',
    'maverick': 'place-mvbcl',
    'north quincy': 'place-nqncy',
    'north station': 'place-north',
    'oak grove': 'place-ogmnl',
    'orient heights': 'place-orhte',
    'park street': 'place-pktrm',
    'porter': 'place-portr',
    'quincy adams': 'place-qamnl',
    'quincy center': 'place-qnctr',
    'revere beach': 'place-rbmnl',
    'roxbury crossing': 'place-rcmnl',
    'ruggles': 'place-rugg',
    'savin hill': 'place-shmnl',
    'shawmut': 'place-smmnl',
    'south station': 'place-sstat',
    'state street': 'place-state',
    'stony brook': 'place-sbmnl',
    'suffolk downs': 'place-sdmnl',
    'sullivan square': 'place-sull',
    'tufts medical center': 'place-tumnl',
    'wellington': 'place-welln',
    'wollaston': 'place-wlsta',
    'wonderland': 'place-wondl',
    'wood island': 'place-wimnl',
}


def distance(p1, p2):
    """ Returns the distance between two points. """
    return math.sqrt(pow((p2[0] - p1[0]), 2) + pow((p2[1] - p1[1]), 2))


class NoPredictionsError(Exception):
    """ Raised if predictions cannot be determined for a route/stop. """
    pass


class MbtaApi(object):
    """
    API wrapper for MBTA-realtime API v2.

    See http://realtime.mbta.com/Portal/Home/Documents for full details.
    """
    API_HOST = 'http://realtime.mbta.com/developer/api/v2'
    INBOUND = '1'
    OUTBOUND = '0'
    SUBWAY_ROUTE_TYPE = '1'

    def __init__(self, latitude, longitude):
        self.api_key = MBTA_API_KEY
        self.current_location = (latitude, longitude)

    @classmethod
    def convert_direction(cls, s):
        return {
            'inbound': cls.INBOUND,
            'outbound': cls.OUTBOUND,
        }[s]

    def stops_by_route(self, route_id):
        # TODO Cache this information for all users
        url = '{api_host}/stopsbyroute?api_key={api_key}&route={route}&format=json'.format(
            api_host=self.API_HOST, api_key=self.api_key, route=route_id
        )
        return requests.get(url).json()

    def get_closest_stop(self, stops):
        """ Given a list of stops, returns the stop closest to the current location.

        Returns:
            (distance, stop)
        """
        closest = (float('inf'), None)

        for stop in stops:
            stop_location = (float(stop['stop_lat']), float(stop['stop_lon']))
            stop_distance = distance(self.current_location, stop_location)
            if stop_distance < closest[0]:
                closest = (stop_distance, stop)

        return closest

    def next_predicted_departures(self, stop_id, route_id, direction_id):
        route_id = route_id.lower()
        direction_id = int(direction_id)
        url = '{api_host}/predictionsbystop?api_key={api_key}&stop={stop_id}&format=json'.format(
            api_host=self.API_HOST, api_key=self.api_key, stop_id=stop_id
        )
        predictions = requests.get(url).json()

        # Ensure we have predictions
        if 'mode' not in predictions:
            raise NoPredictionsError

        # Get the route we actually care about
        routes = list(itertools.chain.from_iterable([mode['route'] for mode in predictions['mode']]))
        routes = [route for route in routes if route['route_id'].lower() == route_id]

        if not routes:
            raise NoPredictionsError

        # Get the desired direction of the route
        trips = []
        for direction in routes[0]['direction']:
            if int(direction['direction_id']) == direction_id:
                trips = direction['trip']
                break

        predictions = []
        for trip in trips[:3]:
            predictions.append(datetime.datetime.fromtimestamp(int(trip['pre_dt']), tz=TIMEZONE))

        predictions.sort()
        return predictions

    def next_bus_departure(self, route_id, direction_id):
        stops_by_route = self.stops_by_route(route_id)
        stops_by_route = stops_by_route['direction']
        stops_by_route = [stops for stops in stops_by_route if stops['direction_id'] == direction_id][0]['stop']

        # Determine the closest stop
        __, closest_stop = self.get_closest_stop(stops_by_route)
        stop_id = closest_stop['stop_id']
        prediction = self.next_predicted_departures(stop_id, route_id, direction_id)

        # TODO Format street types properly
        stop_name = closest_stop['stop_name'].replace(' St ', ' St. ')
        return stop_name, prediction

    def next_subway_departure(self, route_id, destination_station):
        directions = self.stops_by_route(route_id)['direction']
        closest = (float('inf'), None, None)

        for direction in directions:
            candidates = []
            for stop in direction['stop']:
                if stop['parent_station'] == destination_station:
                    break
                candidates.append(stop)

            distance, stop = self.get_closest_stop(candidates)
            if distance < closest[0]:
                closest = distance, stop, int(direction['direction_id'])

        closest_stop = closest[1]

        if closest_stop:
            direction_id = closest[2]
            prediction = self.next_predicted_departures(closest_stop['stop_id'], route_id, direction_id)
            return closest_stop['parent_station_name'], prediction
        else:
            # TODO Raise an exception!
            return None, None


def handle_no_predictions_error():
    text = 'I was unable to locate a departure time.'
    return statement(text).simple_card(APP_NAME, text)


def format_predictions(predictions):
    departure_times = [departure_time.strftime('%I:%M %p') for departure_time in predictions]

    if len(departure_times) == 1:
        spoken_departures = departure_times[0]
    else:
        spoken_departures = ', '.join(departure_times[:-1]) + ', and ' + departure_times[-1]

    return spoken_departures


@ask.intent('BusIntent')
def bus(direction, route):
    mbta_api = MbtaApi(LATITUDE, LONGITUDE)
    int_direction = mbta_api.convert_direction(direction)
    try:
        location, departure_times = mbta_api.next_bus_departure(route, int_direction)
    except NoPredictionsError:
        return handle_no_predictions_error()

    spoken_departures = format_predictions(departure_times)

    text = 'The next {direction} {route} bus departs {location} at {departure}.'.format(
        direction=direction, route=route, location=location, departure=spoken_departures
    )
    return statement(text).simple_card(APP_NAME, text)


@ask.intent('SubwayIntent')
def subway(subway_line, destination_station):
    # TODO Determine how to differentiate between the different green lines (B, C, D, E)
    if subway_line == 'green':
        text = 'I cannot provide times for the green line.'
        return statement(text).simple_card(APP_NAME, text)

    parent_station = STATIONS.get(destination_station.lower())
    if not parent_station:
        text = 'I am was unable to locate a station named {station}.'.format(station=destination_station)
        return statement(text).simple_card(APP_NAME, text)

    mbta_api = MbtaApi(LATITUDE, LONGITUDE)
    try:
        departure_station, departure_times = mbta_api.next_subway_departure(subway_line, parent_station)
    except NoPredictionsError:
        return handle_no_predictions_error()

    spoken_departures = format_predictions(departure_times)

    text = 'The next {subway_line} line trains to {destination_station} depart {departure_station} at {departure_times}.'.format(
        subway_line=subway_line, destination_station=destination_station, departure_station=departure_station,
        departure_times=spoken_departures
    )
    return statement(text).simple_card(APP_NAME, text)


if __name__ == '__main__':
    app.run(debug=True)
