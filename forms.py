from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class Customer_Sign_up(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=25)])

    age = IntegerField('Age', validators=[DataRequired()])

    gender = StringField('Gender', validators=[DataRequired])

    height = FloatField('Height', validators=[DataRequired()])

    weight = FloatField('Weight', validators=[DataRequired()])

    occupation = StringField('Occupation', validators=[DataRequired()])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = StringField('Password', validators=[DataRequired()])

    aim = StringField('Aim', validators=[DataRequired])

    submit = SubmitField('Sign Up')
