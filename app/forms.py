from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import InputRequired
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileAllowed, FileRequired

class profileform(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    upload = FileField('Profile Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])
    