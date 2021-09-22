from bus_board import Bus_board

class Bus_board_web(Bus_board):

    def __init__(self):
        super().__init__()

    def return_board(self, atcocode):
        board = []
        self.buses.get_buses(atcocode)
        bus_list = self.buses.get_bus_information()
        print(f'Stop -> {self.buses.time_table["name"]}')
        for i in bus_list:
            board.append(({i[0]},{i[1]},{i[2]}))
        return board

