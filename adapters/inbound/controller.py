from flask import Flask,request
from flask import jsonify
from adapters.outbound import get_palte_repository

app = Flask(__name__)


@app.route('/set', methods=['GET'])
def get_plate_number():
    plate_numbers = get_palte_repository().get_all_plate_number()
    return jsonify(plate_numbers)


@app.route('/set', methods=['PUT'])    
def recive_new_plate_number():
    plate_numbers = request.json['plate_numbers']
    get_palte_repository().update_plate_number(plate_numbers)
    return "Dane zostały odebrane: {}".format(plate_numbers)



