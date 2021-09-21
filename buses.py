import requests

class Buses():
    time_table = None

    def __init__(self):
        pass

    def get_buses(self, atcocode):
        time_table = requests.get(
            f'https://transportapi.com/v3/uk/bus/stop/{atcocode}/live.json?app_id=d469280a&app_key=004f69bc55849dfc0066c1c160a04424&group=no')
        self.time_table = time_table.json()
        self.get_bus_information()

    def get_bus_information(self):
        print(f'Stop -> {self.time_table["name"]}')
        departures = self.time_table['departures']
        if len(departures) == 0:
            print('No buses for this stop')
        all = departures['all']
        if len(all) > 5:
            for i in range(0,5):
                bus = all[i]
                line = bus['line']
                direction = bus['direction']
                expected = bus['expected']
                arrival_dict = expected['arrival']
                time = arrival_dict['time']
                print(f'{line} {direction} {time} ')
        else:
            for i in range(0,len(all)):
                bus = all[i]
                line = bus['line']
                direction = bus['direction']
                expected = bus['expected']
                arrival_dict = expected['arrival']
                time = arrival_dict['time']
                print(f'{line} {direction} {time} ')



