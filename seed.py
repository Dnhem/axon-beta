from models import Client,Exercise, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If tables aren't empty, empty it
Client.query.delete()
Exercise.query.delete()

# Add example clients
john = Client(first_name = "John", last_name = "Smith", phone="415-999-9999", email="johnsmith@pretendmail.com", image="../static/assets/john-modified.png", start_date="2020-08-15", goals="Muscle gain")

ada = Client(first_name = "Ada", last_name = "Lovelace", phone="415-777-7777", email="adalovelace@pretendmail.com", image="../static/assets/ada-modified.png", start_date="2018-12-08", goals="Muscle tone")

marco = Client(first_name = "Marco", last_name = "Polo", phone="650-555-5555", email="marcopolo@pretendmail.com", image="../static/assets/marco-modified.png", start_date="2022-09-2", goals="Weight loss")

# Add example exercises
jumping_jacks = Exercise(name="jumping jacks", sets="3", rest="1:00", duration="3:00", client_id=1, date="2022-09-10")
elevated_foot_squat = Exercise(name="elevated foot squat", sets="4", reps="12", weight="25", rest="1:30", client_id=1, date="2022-09-10")

bench_push_ups = Exercise(name="bench push-ups", sets="3", reps="6", rest="30", client_id=2, date="2022-09-12")
banded_glute_bridge = Exercise(name="banded glute bridge", sets="3", reps="12", rest="30", client_id=2, date="2022-09-12")
adductor_stretch = Exercise(name="adductor stretch", sets="2", duration="1:00", rest="0:10", client_id=2, date="2022-09-12")
barbell_bench_press = Exercise(name="barbell bench press", sets="4", reps="12", rest="45", client_id=2, date="2022-09-15")
barbell_hip_thruster = Exercise(name="barbell hip thruster", sets="4", reps="15", weight="175", rest="45", client_id=2, date="2022-09-15")
high_knees = Exercise(name="high knees", sets="3", rest="0:45", duration="1:25", client_id=2, date="2022-09-15")

db.session.add(john)
db.session.add(ada)
db.session.add(marco)
db.session.commit()

db.session.add(jumping_jacks)
db.session.add(elevated_foot_squat)
db.session.add(bench_push_ups)
db.session.add(banded_glute_bridge)
db.session.add(adductor_stretch)
db.session.add(barbell_bench_press)
db.session.add(barbell_hip_thruster)
db.session.add(high_knees)
db.session.commit()