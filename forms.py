from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Regexp, Optional

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    
    phone = StringField(
        'Phone', 
        validators=[
            DataRequired(),
            Regexp(r'^\+974[0-9]{8}$', message="Phone number must start with +974 followed by 8 digits.")
        ]
    )
    
    email = StringField(
        'Email', 
        validators=[
            Optional(),  # Email is optional but must be valid if entered
            Email(message="Invalid email format. Please enter a valid email address.")
        ]
    )
    
    type = SelectField(
        'Type', 
        choices=[('Personal', 'Personal'), 
                 ('Work', 'Work'), 
                 ('Other', 'Other'),
                 ('Custom', 'Custom')]
    )
    
    custom_type = StringField('Custom Type', validators=[Optional()])  # Allows a custom type if selected
    
    is_favourite = BooleanField('Favourite')  # New field for marking contact as favorite
    
    submit = SubmitField('Submit')
