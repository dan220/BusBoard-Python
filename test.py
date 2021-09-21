import requests
from bus_stops import Bus_stops

stops = Bus_stops()

lat,long = stops.get_latandlong('ba22dz')

print(lat)
print(long)

bus_stops = requests.get(f'https://transportapi.com/v3/uk/places.json?lat={lat}&lon={long} \
                         &type=bus_stop&app_id=d469280a&app_key=004f69bc55849dfc0066c1c160a04424')

bus_stops = bus_stops.json()

print(bus_stops)

def get_atocode(bus_stops):
    bus_stops = bus_stops['member']
    first_stop = bus_stops[0]
    second_stop = bus_stops[1]
    first_stop_atocode = first_stop['atcocode']
    second_stop_atocode = second_stop['atcocode']
    return first_stop_atocode, second_stop_atocode

print(get_atocode(bus_stops))