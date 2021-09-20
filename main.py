import requests
import json
#0180BAC30592

def main():
    print("Welcome to BusBoard.")
    atcode = input("Please input the bus stop atcode: ")
    r = requests.get('https://transportapi.com/v3/uk/bus/stop/' + atcode + '/live.json?app_id=d469280a&app_key=004f69bc55849dfc0066c1c160a04424&group=no&limit=5')
    r1 = r.json()
    departures = r1['departures']
    all = departures['all']
    count = 0
    for buses in all:
        for element in buses:
            print(element, '->', buses[element])
        count += 1
        if count == 5:
            break





if __name__ == "__main__":
    main()