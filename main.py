import requests
from buses import Buses
from bus_board import Bus_board
from bus_stops import Bus_stops

def main():
    print("Welcome to BusBoard.")
   # atcocode = input("Please input an atcocode: ")
    bus_board = Bus_board()
    #bus_board.print_board(atcocode)

    bus_stops = Bus_stops()
    postcode = input("Please input a postcode: ")
    bus_stops.update_bus_stops(postcode)
    first_stop_atcocode, second_stop_atcocode = bus_stops.get_atcocodes()
    bus_board.print_board(first_stop_atcocode)
    bus_board.print_board(second_stop_atcocode)




if __name__ == "__main__":
    main()