import requests
import json
from buses import Buses
#0180BAC30592

def main():
    print("Welcome to BusBoard.")
    atocode = input("Please input the bus stop atcode: ")
    buses = Buses(atocode)
    buses.update_timetable()
    buses_text= buses.get_buses()
    print(buses_text)



if __name__ == "__main__":
    main()