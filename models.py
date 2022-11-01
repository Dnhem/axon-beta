from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


DEFAULT_IMG = "https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png"


class Client(db.Model):
    """Client details"""

    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    image = db.Column(db.String, default=DEFAULT_IMG)
    goals = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String(50), unique=True)
    exercises = db.relationship("Exercise")

    def organize_exercise_dates(self, exercises):
        # Generate organized list of lists by dates
        # Template list displaying dated records ("date blocks") of exercises
        unique_dates = set()
        organize_dates = []
        for e in exercises:
            unique_dates.add(e.date)
        convert_unique_dates = list(unique_dates)
        for i in range(len(convert_unique_dates)):
            dated_exercise = []
            for e in exercises:
                if e.date in convert_unique_dates[i]:
                    dated_exercise.append(e)
            organize_dates.append(dated_exercise)
        return sorted(organize_dates, key=lambda x: x[0].date)

    def __repr__(self):
        c = self
        return f"<Client id={c.id}, first_name={c.first_name}, last_name={c.last_name}>"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Exercise(db.Model):
    """Exercise details"""

    __tablename__ = "exercises"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    sets = db.Column(db.String(50))
    reps = db.Column(db.String(50))
    weight = db.Column(db.String(50))
    rest = db.Column(db.String(50))
    duration = db.Column(db.String(50))
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"))
    date = db.Column(db.String(50))

    def __repr__(self):
        e = self
        return f"<Exercise id={e.id}, name={e.name}, sets={e.sets}, reps={e.reps}, weight={e.weight}, rest={e.rest}, duration={e.duration}, client={e.client_id}, date={e.date}>"
