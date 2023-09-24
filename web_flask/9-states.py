#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Removes current SQLAlchemy Session """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Displays html with States """
    states = storage.all(State)
    return render_template('9-states_list.html', states=states, mode='all')


@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id):
    """Displays html with States/cities """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
