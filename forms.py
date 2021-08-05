# we could put forms in to the html files, but it's best to split things out in to their own files.
# this way if we need to update it in the future we know exactly where to go.
# its easier breaking things up in to more manageable chunks of code.
# these forms are written in python classes then converted to html.
# each form field will have a list of errors thanks to the wtforms.validators modules. this allows us to open conditionals and print the errors

# from flask_wtf import FlaskForm
# from wtforms import StringField #add a string field
# from wtforms import PasswordField # password field
# from wtforms import SubmitField # to submit the form
# from wtforms import BooleanField # for true or false statements, like a Remember Me or Stay Logged In
# from wtforms.validators import DataRequired #add validators input for limiting what a user can put in a field
# from wtforms.validators import Length # add length validation
# from wtforms.validators import Email # email validation. @ .com etc. Must use 'pip install email_validation'
# from wtforms.validators import EqualTo # confirm that 2 inputs are the same (think both password fields)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)]) # 'Username' is also the label in the html.
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')
#
# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')