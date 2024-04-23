import kink
from flask import Flask,request
from flask import jsonify

from application.ports.outbound.plate_data_repo import PlateNumberRepository


app = Flask(__name__)


@app.route('/set', methods=['GET'])
def get_plate_number():
    plate_numbers = kink.di[PlateNumberRepository].get_all_plate_number()
    return jsonify(plate_numbers)


@app.route('/set', methods=['PUT'])    
def recive_new_plate_number():
    plate_numbers = request.json['plate_numbers']
    kink.di[PlateNumberRepository].update_plate_number(plate_numbers)
    return "Dane zostały odebrane: {}".format(plate_numbers)



