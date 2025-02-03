from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import Optional

class ContactForm(FlaskForm):
    name = StringField('Name')
    phone = StringField('Phone')
    email = StringField('Email')
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other'),
                              ('Custom', 'Custom')])
    custom_type = StringField('Custom Type', validators=[Optional()])  # New field for custom input
    is_favourite = BooleanField('Favourite')  # New field
    submit = SubmitField('Submit')
