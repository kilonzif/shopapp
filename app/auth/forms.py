
from ast import Sub
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField,SubmitField,BooleanField

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Optional
)



class SignUpForm(FlaskForm):
    username = StringField(
        'username',
        validators=[DataRequired()]
    )
    email = StringField(
        'email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.'),
            Length(min=8)
            ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6,message='Put a stronger password')
        ]
    )

    confirm = PasswordField(
        'Confirm Password',
       validators=[
            DataRequired(),
            Length(min=6,message='Passwords must match')
        ]
    )

    submit = SubmitField('Sign Up')




class LoginForm(FlaskForm):
    email = StringField('Email Address',validators=[DataRequired(),Email(message='Enter a valid email.')])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')