import requests
from buses import Buses
from bus_stops import Bus_stops

def main():
    print("Welcome to BusBoard.")
    atcocode = input("Please input the bus stop atocode: ")
    buses = Buses()
    buses.get_buses(atcocode)

    bus_stops = Bus_stops()
    postcode = input("Please input a postcode: ")
    bus_stops.return_bus_stops(postcode)




if __name__ == "__main__":
    main()