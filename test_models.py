from unittest import TestCase
from app import app
from models import db, Client, Exercise

# RUN TEST: python3 -m unittest test_models.py

app.config["SQLALCHEMY_ECHO"] = False


class ClientModelTestCase(TestCase):
    """Test for model for Clients."""

    def setUp(self):
        """Clean up existing client and associated exercises"""
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///axon_test"
        db.create_all()
        Client.query.delete()
        Exercise.query.delete()

        # Create mock client
        client = Client(
            first_name="Daniel",
            last_name="Burns",
            phone="5555555555",
            email="danielburns@pretendmail.com",
            goals="weight loss",
        )

        db.session.add(client)
        db.session.commit()

        # Create mock exercises
        exercise_one = Exercise(
            name="jumping jacks",
            sets="3",
            rest="1:00",
            duration="3:00",
            client_id=1,
            date="2022-09-10",
        )
        exercise_two = Exercise(
            name="elevated foot squat",
            sets="4",
            reps="12",
            weight="25",
            rest="1:30",
            client_id=1,
            date="2022-09-10",
        )
        exercise_three = Exercise(
            name="bench push-ups",
            sets="3",
            reps="6",
            rest="30",
            client_id=1,
            date="2022-09-12",
        )
        exercise_four = Exercise(
            name="banded glute bridge",
            sets="3",
            reps="12",
            rest="30",
            client_id=1,
            date="2022-09-12",
        )
        db.session.add(exercise_one)
        db.session.add(exercise_two)
        db.session.add(exercise_three)
        db.session.add(exercise_four)
        db.session.commit()

    def tearDown(self):
        """Clean up any fouled transaction"""
        db.session.rollback()
        db.drop_all()

    def test_organize_exercise_date(self):
      client = Client.query.get(1)
      organized_exercises = client.organize_exercise_dates(client.exercises)
      print(organized_exercises)
      first_exercise = organized_exercises[0][0]
      last_exercise = organized_exercises[0][-1]

      self.assertEqual(first_exercise.name, 'jumping jacks')
      self.assertEqual(last_exercise.name, 'elevated foot squat')
      
      first_exercise = organized_exercises[1][0]
      last_exercise = organized_exercises[1][-1]

      self.assertEqual(first_exercise.name, 'bench push-ups')
      self.assertEqual(last_exercise.name, 'banded glute bridge')

