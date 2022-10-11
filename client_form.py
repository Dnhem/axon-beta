from wtforms.validators import InputRequired, Optional
from flask_wtf import FlaskForm
from wtforms import StringField, DateField

class ClientForm(FlaskForm):
  """Form to edit client details"""

  first_name = StringField("First Name", validators=[InputRequired()])
  last_name = StringField("Last Name", validators=[InputRequired()])
  start_date = DateField("Start Date", validators=[Optional()])
  goals = StringField("Goals", validators=[Optional()])
  email = StringField("Email", validators=[Optional()])
  phone = StringField("Phone", validators=[Optional()])

