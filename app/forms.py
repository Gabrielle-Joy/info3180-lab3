from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, length

class ContactForm(FlaskForm):
    name = StringField('Name', description='Please enter your full name', validators=[DataRequired()])
    email = StringField('Email', description='Please enter your e-mail address', validators=[DataRequired(), Email()])
    subject = StringField('Name', description='Please enter the subject for your message.', validators=[DataRequired()])
    message = TextAreaField('Message', description='Please enter the message you would like to send', validators=[DataRequired(), length(max=200)])
