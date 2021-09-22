import requests
from buses import Buses

class Bus_stops:
    bus_stops = None
    buses = Buses()

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

    def update_bus_stops(self,postcode):
        lat, long = self.get_latandlong(postcode)
        bus_stops_dict = requests.get(f'https://transportapi.com/v3/uk/places.json?lat={lat}&lon={long} \
                                     &type=bus_stop&app_id=d469280a&app_key=004f69bc55849dfc0066c1c160a04424')
        self.bus_stops = bus_stops_dict.json()

    def get_atcocodes(self):
        bus_stops = self.bus_stops['member']
        first_stop = bus_stops[0]
        second_stop = bus_stops[1]
        first_stop_atocode = first_stop['atcocode']
        second_stop_atocode = second_stop['atcocode']
        return first_stop_atocode, second_stop_atocode


