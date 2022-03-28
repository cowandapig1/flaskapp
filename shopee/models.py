from flask_sqlalchemy import SQLAlchemy
from shopee import app

app.secret_key = "Billy N Micah809"

db = SQLAlchemy(app)

class Courses(db.Model):
    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    instructor = db.Column(db.Text, nullable=False) 
    description = db.Column(db.Text)

def __init__(
    self, c_name, start_date, end_date,instructor ,description
):
    self.c_name = c_name
    self.start_date = start_date
    self.end_date = end_date
    self.instructor = instructor
    self.description = description
class Products(db.Model):
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    origin = db.Column(db.Text)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)

    def __init__(
        self, pid, name, origin, description, quantity, unit_price
    ):
        self.pid = pid
        self.name = name
        self.origin = origin
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return self.name


db.create_all()

    