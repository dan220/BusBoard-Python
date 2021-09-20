import requests

class Buses():
    time_table = None

    def __init__(self,atocode):
        self.atocode = atocode

    def update_timetable(self):
        time_table = requests.get(
            'https://transportapi.com/v3/uk/bus/stop/' + self.atocode + '/live.json?app_id=d469280a&app_key=004f69bc55849dfc0066c1c160a04424&group=no&limit=5')
        self.time_table = time_table.json()

    def get_buses(self):
        departures = self.time_table['departures']
        all = departures['all']
        count = 0
        for buses in all:
            for key in buses:
                if key == 'line':
                    line = buses[key]
                if key == 'direction':
                    direction = buses[key]
                if key == 'expected':
                    expected_dict = buses[key]
                    for sub_key in expected_dict:
                        if sub_key == 'arrival':
                            arrival_dict = expected_dict['arrival']
                            for sub_sub_key in arrival_dict:
                                if sub_sub_key == 'time':
                                    time = arrival_dict['time']
            count += 1
            print(f'{line} {direction} {time} ')
            if count == 5:
                break
