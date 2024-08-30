from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo, ValidationError
from .model import User

#To work with forms we install forms using 
# pip install wtf


class RegistrationForm(FlaskForm):

#Accept input Username
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=5, max=20)])

#accept input for email                          
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

#accept input for password
    password = PasswordField('Password', 
                        validators=[DataRequired()])

#accept input to confirm password
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
                                    

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username already used. please create another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already used. please create a different one.')


class LoginForm(FlaskForm):
#accept input the email
    email = StringField('Email',
                         validators= [InputRequired('Username required!'), Email()])
#accept input password
    password = PasswordField('Password',
                             validators= [InputRequired('Password required!')])
#Remember the password
    remember = BooleanField('Remember Me')

# submit
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')