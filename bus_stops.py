import requests

class Bus_stops:
    bus_stops = []

    def __init__(self):
        pass

    def add_bus_stops(self):
        pass

    def get_latandlong(self, postcode):
        postcode_dict = requests.get(f'https://api.postcodes.io/postcodes/{postcode}')
        postcode_dict_json = postcode_dict.json()

        sub_dict = postcode_dict_json['result']

        lat = sub_dict['latitude']
        long = sub_dict['longitude']
        return lat, long

    def get_atocode(self, bus_stops):
        bus_stops = bus_stops['member']
        first_stop = bus_stops[0]
        second_stop = bus_stops[1]
        first_stop_atocode = first_stop['atcocode']
        second_stop_atocode = second_stop['atcocode']
        return first_stop_atocode, second_stop_atocode

