from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# user registration
class RegisterForm(Form):
    name = TextField(
        'Username',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email',
        validators=[DataRequired(), Email(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField(
        'Repeat Password',
        validators=[DataRequired(), EqualTo('password')]  
    )

# user login
class LoginForm(Form):
    name = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])