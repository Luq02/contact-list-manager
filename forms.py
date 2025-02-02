from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField

class ContactForm(FlaskForm):
    name = StringField('Name')
    phone = StringField('Phone')
    email = StringField('Email')
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    is_favourite = BooleanField('Favourite')  # New field
    submit = SubmitField('Submit')
