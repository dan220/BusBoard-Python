import requests
from buses import Buses
from bus_stops import Bus_stops

def return_buses(atcocode):
    time_table = requests.get(
        f'https://transportapi.com/v3/uk/bus/stop/{atcocode}/live.json?app_id=d469280a&app_key=004f69bc55849dfc0066c1c160a04424&group=no')
    time_table = time_table.json()
    buses = Buses(time_table)
    buses.get_buses2()

def main():
    print("Welcome to BusBoard.")
    atcocode = input("Please input the bus stop atocode: ")
    return_buses(atcocode)

    bus_stops = Bus_stops()
    postcode = input("Please input a postcode: ")
    lat,long = bus_stops.get_latandlong(postcode)
    bus_stops_dict = requests.get(f'https://transportapi.com/v3/uk/places.json?lat={lat}&lon={long} \
                             &type=bus_stop&app_id=d469280a&app_key=004f69bc55849dfc0066c1c160a04424')
    bus_stops_dict = bus_stops_dict.json()
    first_atcocode, second_atcocode = bus_stops.get_atocode(bus_stops_dict)

    return_buses(first_atcocode)
    return_buses(second_atcocode)


if __name__ == "__main__":
    main()