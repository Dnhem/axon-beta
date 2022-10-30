from flask import Flask, render_template, redirect, request, jsonify
import requests
from client_form import ClientForm
from models import db, connect_db, Client, Exercise
from flask_debugtoolbar import DebugToolbarExtension
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql:///axon"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SECRET_KEY"] = "thisasecret"
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# REMOTE API CALL
# Hidden API_KEY
@app.route("/exercises/bodyPart/<bodypart>")
def list_exercise(bodypart):
    response = requests.get(
        f"https://exercisedb.p.rapidapi.com/exercises/bodyPart/{bodypart}",
        headers={
            "X-RapidAPI-Key": os.environ.get("API_SECRET_KEY"),
            "X-RapidAPI-Host": "exercisedb.p.rapidapi.com",
        },
    )
    return { "data": response.json() }

@app.route("/")
def display_home():
    """Display homepage
    List clients
       Access clients profile page"""
    clients = Client.query.all()
    return render_template("home.html", clients=clients)


@app.route("/", methods=["POST"])
def add_client():
    """Add new client to database"""
    try: 
        first_name = request.form["firstname"]
        last_name = request.form["lastname"]
        start_date = request.form["date"]
        goals = request.form["goals"]
        phone = request.form["phone"]
        email = request.form["email"]
        new_client = Client(
            first_name=first_name,
            last_name=last_name,
            start_date=start_date,
            goals=goals,
            phone=phone,
            email=email,
        )
        db.session.add(new_client)
        db.session.commit()
        return redirect("/")
    except:
        return jsonify({'msg': 'Missing required input fields.'}), 500

@app.route("/client/<int:client_id>", methods=["GET"])
def show_client_page(client_id):
    """Display Client details
    View/select workout history
    Design workout template"""
    client = Client.query.get(client_id)
    exercises = client.organize_exercise_dates(client.exercises)
    return render_template("client-page.html", client=client, exercises=exercises)


@app.route("/client/<int:client_id>", methods=["POST"])
def save_workout(client_id):
    """Save client workout to database"""
    inputData = {}
    inputData["date"] = request.form["date"]
    length = 0
    for i in request.form.keys():
        if 'name' in i:
            length += 1
    for i in range(length):
        inputData["name"] = request.form[f"name-{i}"]
        inputData["sets"] = request.form[f"sets-{i}"]
        inputData["reps"] = request.form[f"reps-{i}"]
        inputData["weight"] = request.form[f"weight-{i}"]
        inputData["rest"] = request.form[f"rest-{i}"]
        inputData["duration"] = request.form[f"duration-{i}"]
        exercises = Exercise(
            name=inputData["name"],
            sets=inputData["sets"],
            reps=inputData["reps"],
            weight=inputData["weight"],
            rest=inputData["rest"],
            duration=inputData["duration"],
            client_id=client_id,
            date=inputData["date"],
        )
        print(exercises.__dict__)
        db.session.add(exercises)
        db.session.commit()
    return redirect(f"/client/{client_id}")


@app.route("/client/<int:client_id>/delete", methods=["GET", "POST"])
def delete_client(client_id):
    """Remove client from database"""
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return redirect("/")


@app.route("/client/<int:client_id>/edit", methods=["GET", "POST"])
def update_client(client_id):
    """Update client details
    Prepopulated with original details
    """
    client = Client.query.get_or_404(client_id)
    client_form = ClientForm(obj=client)

    if client_form.validate_on_submit():
        client.first_name = client_form.first_name.data
        client.last_name = client_form.last_name.data
        client.start_date = client_form.start_date.data
        client.goals = client_form.goals.data
        client.email = client_form.email.data
        client.phone = client_form.phone.data
        db.session.commit()
        return redirect(f"/client/{client_id}")

    return render_template("client_form.html", form=client_form, client=client)


@app.route("/client/<int:client_id>/workout")
def display_workout_record(client_id):
    """Query database for exercises respective to
    Client and Date.
    Provides workout history display table
    """
    date = request.args["date"]
    client = Client.query.get(client_id)
    exercises = Exercise.query.filter(
        Exercise.client_id == client_id, Exercise.date == date
    ).all()
    return render_template(
        "client-workout-record.html", client=client, date=date, exercises=exercises
    )
