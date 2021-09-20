import requests
from buses import Buses
#0180BAC30592

def get_latandlong(postcode):
    pass



def main():
    print("Welcome to BusBoard.")
    atocode = input("Please input the bus stop atocode: ")
    time_table = requests.get(
            'https://transportapi.com/v3/uk/bus/stop/' + atocode + '/live.json?app_id=d469280a&app_key=004f69bc55849dfc0066c1c160a04424&group=no')
    time_table = time_table.json()
    buses = Buses(time_table)
    buses.get_buses2()

    bus_stops = requests.get('https://transportapi.com/v3/uk/places.json?lat=51.534121&lon=-0.006944&type=bus_stop&app_id=d469280a&app_key=004f69bc55849dfc0066c1c160a04424')




if __name__ == "__main__":
    main()