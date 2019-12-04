import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/templates/index.html")
def home():
   
    return (           )

@app.route("/Sixers/sixers.html")
def sixers():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)



@app.route("/Sixers/horford.html")
def horford():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)


@app.route("/Sixers/embiid.html")
def embiid():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)

@app.route("/Sixers/harris.html")
def harris():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)

@app.route("/Sixers/richardson.html")
def richardson():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)

@app.route("/Sixers/simmons.html")
def simmons():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)






@app.route("/Knicks/knicks.html")
def knicks():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)


@app.route("/Knicks/knox.html")
def knox():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)



@app.route("/Knicks/barrett.html")
def barrett():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)

@app.route("/Knicks/randle.html")
def randle():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)


@app.route("/Knicks/robinson.html")
def robinson():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)


@app.route("/Knicks/smithjr.html")
def smithjr():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)





















@app.route("/api/v1.0/passengers")
def passenknox():
    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    # all_passengers = []
    # for name, age, sex in results:
    #     passenger_dict = {}
    #     passenger_dict["name"] = name
    #     passenger_dict["age"] = age
    #     passenger_dict["sex"] = sex
    #     all_passengers.append(passenger_dict)

    # return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
