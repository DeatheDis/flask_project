from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(),
                                                Length(min=2, message='Your name is too short')])
    email = StringField('Your Email', validators=[DataRequired(), Email('Incorrect Email')])
    message = TextAreaField('Your Message', validators=[DataRequired(),
                                                        Length(min=1, message='This field is required')])
    submit = SubmitField('Send')
