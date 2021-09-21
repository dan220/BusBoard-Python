import requests

class Buses():

    def __init__(self,time_table):
        self.time_table = time_table

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


    def get_buses2(self):
        print(self.time_table)
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



