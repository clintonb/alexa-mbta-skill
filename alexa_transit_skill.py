from __future__ import unicode_literals

import datetime
import logging
import math
import os

import requests
from flask import Flask
from flask_ask import Ask, statement
from pytz import timezone

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

# TODO Pull location/timezone from user details
LATITUDE = 42.3698964
LONGITUDE = -71.0878818
TIMEZONE = timezone('US/Eastern')

APP_NAME = 'MBTA'
MBTA_API_KEY = os.environ['MBTA_API_KEY']


def distance(p1, p2):
    """ Returns the distance between two points. """
    return math.sqrt(pow((p2[0] - p1[0]), 2) + pow((p2[1] - p1[1]), 2))


class MbtaApi(object):
    """
    API wrapper for MBTA-realtime API v2.

    See http://realtime.mbta.com/Portal/Home/Documents for full details.
    """
    API_HOST = 'http://realtime.mbta.com/developer/api/v2'
    INBOUND = '1'
    OUTBOUND = '0'

    def __init__(self, latitude, longitude):
        self.api_key = MBTA_API_KEY
        self.current_location = (latitude, longitude)

    @classmethod
    def convert_direction(cls, s):
        return {
            'inbound': cls.INBOUND,
            'outbound': cls.OUTBOUND,
        }[s]

    def stops_by_route(self, route_id, direction):
        # TODO Cache this information for all users
        url = '{api_host}/stopsbyroute?api_key={api_key}&route={route}&format=json'.format(
            api_host=self.API_HOST, api_key=self.api_key, route=route_id
        )
        stops_by_route = requests.get(url).json()['direction']
        stops_by_route = [stops for stops in stops_by_route if stops['direction_id'] == direction][0]['stop']
        return stops_by_route

    def next_departure(self, route_id, direction):
        stops_by_route = self.stops_by_route(route_id, direction)

        # Determine the closest stop
        closest = (float('inf'), None)

        for stop in stops_by_route:
            stop_location = (float(stop['stop_lat']), float(stop['stop_lon']))
            stop_distance = distance(self.current_location, stop_location)
            if stop_distance < closest[0]:
                closest = (stop_distance, stop)

        stop_id = closest[1]['stop_id']
        url = '{api_host}/predictionsbystop?api_key={api_key}&stop={stop_id}&format=json'.format(
            api_host=self.API_HOST, api_key=self.api_key, stop_id=stop_id
        )
        predictions = requests.get(url).json()
        stop = predictions['stop_name']
        prediction = predictions['mode'][0]['route'][0]['direction'][0]['trip'][0]
        prediction = datetime.datetime.fromtimestamp(int(prediction['pre_dt']), tz=TIMEZONE)
        return stop, prediction


@ask.intent('BusIntent')
def bus(direction, route):
    mbta_api = MbtaApi(LATITUDE, LONGITUDE)
    int_direction = mbta_api.convert_direction(direction)
    location, departure = mbta_api.next_departure(route, int_direction)

    spoken_departure = departure.strftime('%I:%M %p')

    text = 'The next {direction} {route} bus departs {location} at {departure}.'.format(
        direction=direction, route=route, location=location, departure=spoken_departure
    )
    return statement(text).simple_card(APP_NAME, text)


if __name__ == '__main__':
    app.run(debug=True)
