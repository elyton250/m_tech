from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mine_api import Unit
import random
from os import getenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}'.format(
         getenv("DB_USER"),
         getenv("DB_PASS"),
         getenv("DB_HOST"),
         getenv("DB_NAME")
    )

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

def add_random_entries(num_entries=50):
    for _ in range(num_entries):
        new_unit = Unit(
            temperature=random.randint(10, 40),
            humidity=random.randint(30, 80),
            vibration=random.randint(0, 100),
            pressure=random.randint(900, 1100),
            dust_concentration=random.randint(0, 50),
            oxygen_concentration=random.randint(18, 22),
            stress=random.randint(0, 100),
            strain=random.randint(0, 100)
        )
        db.session.add(new_unit)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        add_random_entries()
