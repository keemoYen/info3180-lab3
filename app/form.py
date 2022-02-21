import email
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('Please enter your full name', validators=[DataRequired()])
    email = StringField('please enter your e-mail address', validators=[DataRequired()])
    subject = StringField('please enter the subject of your message', validators=[DataRequired()])