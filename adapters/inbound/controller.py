from flask import Flask


app = Flask(__name__)


@app.route('/set', methods=['GET'])
def get_plate_number():
    return 'TETS'


@app.route('/set', methods=['PUT'])    
def recive_new_plate_number():
    pass   



