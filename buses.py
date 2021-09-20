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
            for element in buses:
                print(element, '->', buses[element])
            count += 1
            if count == 5:
                break
