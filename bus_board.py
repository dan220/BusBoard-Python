from buses import Buses

class Bus_board():
    buses = Buses()

    def __init__(self):
        pass

    def print_board(self, atcocode):
        self.buses.get_buses(atcocode)
        bus_list = self.buses.get_bus_information()
        print(f'Stop -> {self.buses.time_table["name"]}')
        for i in bus_list:
            print(f'{i[0]} {i[1]}. {i[2]}')