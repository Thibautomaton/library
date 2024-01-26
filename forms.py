
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class UserForm(FlaskForm):
    name = StringField("Your Name : ", validators= [DataRequired()])
    submit = SubmitField("Envoyer")