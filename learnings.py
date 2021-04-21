from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

app = Flask(__name__)

class GalileonMoons:
    def __init__(self, first, second, third, fourth):
        self.first=first
        self.second=second
        self.third=third
        self.fourth=fourth



@app.route('/')
def home():
    return render_template('home.html', name='NAVDEEP SINGH', template_name='JINJA2')


@app.route('/expressions')
def expressions():
    color = 'browm'
    animal_one = 'fox'
    animal_two = 'dog'
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15
    first_name = 'Captain'
    last_name = 'Marvel'

    kwargs = {
        'color' : color,
        'animal_one' : animal_one,
        'animal_two' : animal_two,
        'orange_amount' : orange_amount,
        'apple_amount' : apple_amount,
        'donate_amount' : donate_amount,
        'first_name' : first_name,
        'last_name' : last_name
    }
    return render_template('expressions.html', **kwargs)


@app.route('/jinjadatastructures')
def data_structures():
    movies = [
        "RAJA BABU",
        "COOLIE NO 1",
        "DDLJ"
    ]
    car = {
        "brand":"Tesla",
        "model":"Roadster",
        "year":"2020"
    }
    moons = GalileonMoons("moon1","moon2","moon3","moon4")

    return render_template('data_structures.html', movies=movies, car=car, moons=moons)


@app.route('/loops')
def planets():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
        "Pluto"
    ]
    return render_template('planets.html', planets=planets)