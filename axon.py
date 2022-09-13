from flask import Flask, render_template, redirect, request, flash, jsonify
from models import db, connect_db, Client, Exercise
from flask_debugtoolbar import DebugToolbarExtension
import requests
from api_key import API_SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///axon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'thisasecret'
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def display_home():
  """Display homepage 
     Access clients 
     View upcoming appointments"""
  clients = Client.query.all()
  return render_template('home.html', clients = clients)

@app.route('/exercises/bodyPart/<bodypart>')
def list_exercise(bodypart):
    data = requests.get(f"https://exercisedb.p.rapidapi.com/exercises/bodyPart/{bodypart}",  headers = {
        "X-RapidAPI-Key": API_SECRET_KEY,
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com",
      })
    return data.json()

@app.route('/', methods=["POST"])
def add_client():
  """Add new client to database"""
  first_name = request.form["firstname"]
  last_name = request.form["lastname"] 
  new_client = Client(first_name=first_name, last_name=last_name)
  db.session.add(new_client)
  db.session.commit()
  return redirect('/')

@app.route('/client/<int:client_id>')
def show_client_page(client_id):
  """Display Client details
     View/select workout history 
     Design workout template"""
  client = Client.query.get(client_id)
  exercises = client.organize_exercise_dates(client.exercises)
  print(exercises)
  return render_template('client-page.html', client=client, exercises=exercises)

@app.route('/client/<int:client_id>', methods=["POST"])
def save_workout(client_id):
  """Save client workout to database"""
  inputData = {}
  for i in range(request.form.__len__()//5):
    inputData["name"] = request.form[f"name-{i}"]
    inputData["sets"] = request.form[f"sets-{i}"]
    inputData["reps"] = request.form[f"reps-{i}"]
    inputData["weight"] = request.form[f"weight-{i}"]
    inputData["rest"] = request.form[f"rest-{i}"]
    inputData["duration"] = request.form[f"duration-{i}"]
    inputData["date"] = request.form["date"]
    exercises = Exercise(name=inputData["name"], sets=inputData["sets"], reps=inputData["reps"], weight=inputData["weight"], rest=inputData["rest"], duration=inputData["duration"], client_id=client_id, date=inputData["date"])
    db.session.add(exercises)
    db.session.commit()
    inputData.clear()
  return redirect(f"/client/{client_id}")

@app.route('/client/<int:client_id>/workout')
def display_workout_record(client_id):
  date = request.args["date"]
  client = Client.query.get(client_id)
  exercises = Exercise.query.filter(Exercise.client_id==client_id, Exercise.date==date).all()
  return render_template('client-workout-record.html', client=client, date=date, exercises=exercises)

