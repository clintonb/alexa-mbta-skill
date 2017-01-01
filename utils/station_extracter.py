import pprint

station_inputs = {
  "direction": [
    {
      "direction_id": "0",
      "direction_name": "Southbound",
      "stop": [
        {
          "stop_order": "1",
          "stop_id": "70036",
          "stop_name": "Oak Grove",
          "parent_station": "place-ogmnl",
          "parent_station_name": "Oak Grove",
          "stop_lat": "42.43668",
          "stop_lon": "-71.071097"
        },
        {
          "stop_order": "10",
          "stop_id": "70034",
          "stop_name": "Malden - Inbound",
          "parent_station": "place-mlmnl",
          "parent_station_name": "Malden Center",
          "stop_lat": "42.426632",
          "stop_lon": "-71.07411"
        },
        {
          "stop_order": "20",
          "stop_id": "70032",
          "stop_name": "Wellington - Inbound",
          "parent_station": "place-welln",
          "parent_station_name": "Wellington",
          "stop_lat": "42.40237",
          "stop_lon": "-71.077082"
        },
        {
          "stop_order": "30",
          "stop_id": "70278",
          "stop_name": "Assembly - Inbound",
          "parent_station": "place-astao",
          "parent_station_name": "Assembly",
          "stop_lat": "42.392811",
          "stop_lon": "-71.077257"
        },
        {
          "stop_order": "40",
          "stop_id": "70030",
          "stop_name": "Sullivan Square - Inbound",
          "parent_station": "place-sull",
          "parent_station_name": "Sullivan Square",
          "stop_lat": "42.383975",
          "stop_lon": "-71.076994"
        },
        {
          "stop_order": "50",
          "stop_id": "70028",
          "stop_name": "Community College - Inbound",
          "parent_station": "place-ccmnl",
          "parent_station_name": "Community College",
          "stop_lat": "42.373622",
          "stop_lon": "-71.069533"
        },
        {
          "stop_order": "60",
          "stop_id": "70026",
          "stop_name": "North Station - Orange Line Inbound",
          "parent_station": "place-north",
          "parent_station_name": "North Station",
          "stop_lat": "42.365577",
          "stop_lon": "-71.06129"
        },
        {
          "stop_order": "70",
          "stop_id": "70024",
          "stop_name": "Haymarket - Orange Line Inbound",
          "parent_station": "place-haecl",
          "parent_station_name": "Haymarket",
          "stop_lat": "42.363021",
          "stop_lon": "-71.05829"
        },
        {
          "stop_order": "80",
          "stop_id": "70022",
          "stop_name": "State Street - to Forest Hills",
          "parent_station": "place-state",
          "parent_station_name": "State Street",
          "stop_lat": "42.358978",
          "stop_lon": "-71.057598"
        },
        {
          "stop_order": "90",
          "stop_id": "70020",
          "stop_name": "Downtown Crossing - to Forest Hills",
          "parent_station": "place-dwnxg",
          "parent_station_name": "Downtown Crossing",
          "stop_lat": "42.355518",
          "stop_lon": "-71.060225"
        },
        {
          "stop_order": "100",
          "stop_id": "70018",
          "stop_name": "Chinatown - Outbound",
          "parent_station": "place-chncl",
          "parent_station_name": "Chinatown",
          "stop_lat": "42.352547",
          "stop_lon": "-71.062752"
        },
        {
          "stop_order": "110",
          "stop_id": "70016",
          "stop_name": "Tufts Medical Center - Outbound",
          "parent_station": "place-tumnl",
          "parent_station_name": "Tufts Medical Center",
          "stop_lat": "42.349662",
          "stop_lon": "-71.063917"
        },
        {
          "stop_order": "120",
          "stop_id": "70014",
          "stop_name": "Back Bay - Outbound",
          "parent_station": "place-bbsta",
          "parent_station_name": "Back Bay",
          "stop_lat": "42.34735",
          "stop_lon": "-71.075727"
        },
        {
          "stop_order": "130",
          "stop_id": "70012",
          "stop_name": "Massachusetts Avenue - Outbound",
          "parent_station": "place-masta",
          "parent_station_name": "Massachusetts Ave.",
          "stop_lat": "42.341512",
          "stop_lon": "-71.083423"
        },
        {
          "stop_order": "140",
          "stop_id": "70010",
          "stop_name": "Ruggles - Outbound",
          "parent_station": "place-rugg",
          "parent_station_name": "Ruggles",
          "stop_lat": "42.336377",
          "stop_lon": "-71.088961"
        },
        {
          "stop_order": "150",
          "stop_id": "70008",
          "stop_name": "Roxbury Crossing - Outbound",
          "parent_station": "place-rcmnl",
          "parent_station_name": "Roxbury Crossing",
          "stop_lat": "42.331397",
          "stop_lon": "-71.095451"
        },
        {
          "stop_order": "160",
          "stop_id": "70006",
          "stop_name": "Jackson Square - Outbound",
          "parent_station": "place-jaksn",
          "parent_station_name": "Jackson Square",
          "stop_lat": "42.323132",
          "stop_lon": "-71.099592"
        },
        {
          "stop_order": "170",
          "stop_id": "70004",
          "stop_name": "Stony Brook - Outbound",
          "parent_station": "place-sbmnl",
          "parent_station_name": "Stony Brook",
          "stop_lat": "42.317062",
          "stop_lon": "-71.104248"
        },
        {
          "stop_order": "180",
          "stop_id": "70002",
          "stop_name": "Green Street - Outbound",
          "parent_station": "place-grnst",
          "parent_station_name": "Green Street",
          "stop_lat": "42.310525",
          "stop_lon": "-71.107414"
        },
        {
          "stop_order": "190",
          "stop_id": "70001",
          "stop_name": "Forest Hills Orange Line",
          "parent_station": "place-forhl",
          "parent_station_name": "Forest Hills",
          "stop_lat": "42.300523",
          "stop_lon": "-71.113686"
        }
      ]
    },
    {
      "direction_id": "1",
      "direction_name": "Northbound",
      "stop": [
        {
          "stop_order": "1",
          "stop_id": "70001",
          "stop_name": "Forest Hills Orange Line",
          "parent_station": "place-forhl",
          "parent_station_name": "Forest Hills",
          "stop_lat": "42.300523",
          "stop_lon": "-71.113686"
        },
        {
          "stop_order": "10",
          "stop_id": "70003",
          "stop_name": "Green Street - Inbound",
          "parent_station": "place-grnst",
          "parent_station_name": "Green Street",
          "stop_lat": "42.310525",
          "stop_lon": "-71.107414"
        },
        {
          "stop_order": "20",
          "stop_id": "70005",
          "stop_name": "Stony Brook - Inbound",
          "parent_station": "place-sbmnl",
          "parent_station_name": "Stony Brook",
          "stop_lat": "42.317062",
          "stop_lon": "-71.104248"
        },
        {
          "stop_order": "30",
          "stop_id": "70007",
          "stop_name": "Jackson Square - Inbound",
          "parent_station": "place-jaksn",
          "parent_station_name": "Jackson Square",
          "stop_lat": "42.323132",
          "stop_lon": "-71.099592"
        },
        {
          "stop_order": "40",
          "stop_id": "70009",
          "stop_name": "Roxbury Crossing - Inbound",
          "parent_station": "place-rcmnl",
          "parent_station_name": "Roxbury Crossing",
          "stop_lat": "42.331397",
          "stop_lon": "-71.095451"
        },
        {
          "stop_order": "50",
          "stop_id": "70011",
          "stop_name": "Ruggles - Inbound",
          "parent_station": "place-rugg",
          "parent_station_name": "Ruggles",
          "stop_lat": "42.336377",
          "stop_lon": "-71.088961"
        },
        {
          "stop_order": "60",
          "stop_id": "70013",
          "stop_name": "Massachusetts Avenue - Inbound",
          "parent_station": "place-masta",
          "parent_station_name": "Massachusetts Ave.",
          "stop_lat": "42.341512",
          "stop_lon": "-71.083423"
        },
        {
          "stop_order": "70",
          "stop_id": "70015",
          "stop_name": "Back Bay - Inbound",
          "parent_station": "place-bbsta",
          "parent_station_name": "Back Bay",
          "stop_lat": "42.34735",
          "stop_lon": "-71.075727"
        },
        {
          "stop_order": "80",
          "stop_id": "70017",
          "stop_name": "Tufts Medical Center - Inbound",
          "parent_station": "place-tumnl",
          "parent_station_name": "Tufts Medical Center",
          "stop_lat": "42.349662",
          "stop_lon": "-71.063917"
        },
        {
          "stop_order": "90",
          "stop_id": "70019",
          "stop_name": "Chinatown - Inbound",
          "parent_station": "place-chncl",
          "parent_station_name": "Chinatown",
          "stop_lat": "42.352547",
          "stop_lon": "-71.062752"
        },
        {
          "stop_order": "100",
          "stop_id": "70021",
          "stop_name": "Downtown Crossing - to Oak Grove",
          "parent_station": "place-dwnxg",
          "parent_station_name": "Downtown Crossing",
          "stop_lat": "42.355518",
          "stop_lon": "-71.060225"
        },
        {
          "stop_order": "110",
          "stop_id": "70023",
          "stop_name": "State Street - to Oak Grove",
          "parent_station": "place-state",
          "parent_station_name": "State Street",
          "stop_lat": "42.358978",
          "stop_lon": "-71.057598"
        },
        {
          "stop_order": "120",
          "stop_id": "70025",
          "stop_name": "Haymarket - Orange Line Outbound",
          "parent_station": "place-haecl",
          "parent_station_name": "Haymarket",
          "stop_lat": "42.363021",
          "stop_lon": "-71.05829"
        },
        {
          "stop_order": "130",
          "stop_id": "70027",
          "stop_name": "North Station - Orange Line Outbound",
          "parent_station": "place-north",
          "parent_station_name": "North Station",
          "stop_lat": "42.365577",
          "stop_lon": "-71.06129"
        },
        {
          "stop_order": "140",
          "stop_id": "70029",
          "stop_name": "Community College - Outbound",
          "parent_station": "place-ccmnl",
          "parent_station_name": "Community College",
          "stop_lat": "42.373622",
          "stop_lon": "-71.069533"
        },
        {
          "stop_order": "150",
          "stop_id": "70031",
          "stop_name": "Sullivan Square - Outbound",
          "parent_station": "place-sull",
          "parent_station_name": "Sullivan Square",
          "stop_lat": "42.383975",
          "stop_lon": "-71.076994"
        },
        {
          "stop_order": "160",
          "stop_id": "70279",
          "stop_name": "Assembly - Outbound",
          "parent_station": "place-astao",
          "parent_station_name": "Assembly",
          "stop_lat": "42.392811",
          "stop_lon": "-71.077257"
        },
        {
          "stop_order": "170",
          "stop_id": "70033",
          "stop_name": "Wellington - Outbound",
          "parent_station": "place-welln",
          "parent_station_name": "Wellington",
          "stop_lat": "42.40237",
          "stop_lon": "-71.077082"
        },
        {
          "stop_order": "180",
          "stop_id": "70035",
          "stop_name": "Malden - Outbound",
          "parent_station": "place-mlmnl",
          "parent_station_name": "Malden Center",
          "stop_lat": "42.426632",
          "stop_lon": "-71.07411"
        },
        {
          "stop_order": "190",
          "stop_id": "70036",
          "stop_name": "Oak Grove",
          "parent_station": "place-ogmnl",
          "parent_station_name": "Oak Grove",
          "stop_lat": "42.43668",
          "stop_lon": "-71.071097"
        }
      ]
    }
  ]
}

stations = {}

for direction in station_inputs['direction']:
    for stop in direction['stop']:
        stations[stop['parent_station_name'].lower()] = stop['parent_station'].lower()

pprint.pprint(stations)
