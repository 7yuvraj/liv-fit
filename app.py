import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient("mongodb+srv://navdeep:navdeep@livfit.zdzc3.mongodb.net/test")
app.db = client.livfit
users = []


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/customersignup/", methods=["GET", "POST"])
def customer_signup():
    if request.method == "POST":
        customer = {}
        customer["name"] = request.form.get("name")
        customer["age"] = request.form.get("age")
        customer["gender"] = request.form.get("gender")
        customer["occupation"] = request.form.get("occupation")
        customer["email_id"] = request.form.get("email")
        customer["password"] = request.form.get("password")
        customer["aim"] = request.form.get("aim")
        customer["registration_date"] = datetime.datetime.today().strftime("%Y-%m-%d")
        print(customer)
        '''
        app.db.users.insert(customer)
        '''
    return render_template('customersignup.html')


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

'''
from User.models import User
@app.route('/user/signup/', methods=['GET'])
def signup(member):
    return 
'''
