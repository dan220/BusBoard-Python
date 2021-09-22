from flask import Flask, render_template, request
from bus_stops import Bus_stops
from bus_baord_web import Bus_board_web

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/busInfo")
def busInfo():
    postcode = request.args.get('postcode')
    bus_stops = Bus_stops()
    bus_board = Bus_board_web()
    bus_stops.update_bus_stops(postcode)
    first_stop_atcocode, second_stop_atcocode = bus_stops.get_atcocodes()
    board_1 = bus_board.return_board(first_stop_atcocode)
    board_2 = bus_board.print_board(second_stop_atcocode)
    return render_template('info.html', board=board_1)

if __name__ == "__main__": app.run()