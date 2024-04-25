from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_cors import CORS
from os import getenv
from dotenv import load_dotenv
"""My Flask App"""


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}'.format(
         getenv("DB_USER"),
         getenv("DB_PASS"),
         getenv("DB_HOST"),
         getenv("DB_NAME")
    )
CORS(app)
"""initializing database"""
db = SQLAlchemy(app)

class Unit(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    vibration = db.Column(db.Integer)
    pressure = db.Column(db.Integer)
    dust_concentration = db.Column(db.Integer)
    oxygen_concentration = db.Column(db.Integer)
    stress = db.Column(db.Integer)
    strain = db.Column(db.Integer)


with app.app_context():
    db.create_all()

# this the api route

@app.route('/', methods=['GET'])
def get_units():
    units = Unit.query.all()
    # print(units)
    units_data = [{
        'id': unit.id,
        'temperature': unit.temperature,
        'humidity': unit.humidity,
        'vibration': unit.vibration,
        'pressure': unit.pressure,
        'dust_concentration': unit.dust_concentration,
        'oxygen_concentration': unit.oxygen_concentration,
        'stress': unit.stress,
        'strain': unit.strain
    } for unit in units]
    return jsonify(units_data)

@app.route('/units', methods=['POST'])
def add_unit():
    data = request.get_json()
    new_unit = Unit(
        temperature=data['temperature'],
        humidity=data['humidity'],
        vibration=data['vibration'],
        pressure=data['pressure'],
        dust_concentration=data['dust_concentration'],
        oxygen_concentration=data['oxygen_concentration'],
        stress=data['stress'],
        strain=data['strain']
    )
    db.session.add(new_unit)
    db.session.commit()
    return jsonify({'message': 'Unit added successfully!'})

if __name__ == '__main__':
    app.run(port=5000)
