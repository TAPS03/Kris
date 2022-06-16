from flask import render_template
from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable= False)
    l_name = db.Column(db.String(30), nullable= False)
    thoughts = db.relationship('Thoughts', backref='customer')


class Thoughts(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    favourite_book= db.Column(db.String(40), nullable= False)
    rating= db.Column(db.String(10), nullable= False)
    why_like_book= db.Column(db.String(50), nullable= False)
    compare= db.Column(db.String(30), nullable= False)
    persons_thoughts= db.Column(db.String(30), nullable= False)
    customer_id= db.Column(db.Integer, db.ForeignKey('customer.id'))

class ThoughtsForm(FlaskForm):
    favourite_book=StringField("What is your favourite book: ", validators=[DataRequired()])
    rating= SelectField("Out of 10, what do you rate this book: ", choices= [("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10")],  validators=[DataRequired()])
    why_like_book= StringField("Why is this your favourite book: ",  validators=[DataRequired()])
    compare= SelectField("Compared to your favourite book... which one of these would you be most likely to read: ", choices= [("Harry Potter","Harry Potter"), ("The Paper Palace","The Paper Palace"), ("The Island Of Missing Trees","The Island Of Missing Trees"), ("Sunset","Sunset")], validators=[DataRequired()])
    persons_thoughts = SelectField("Person's opinion: " ,choices=[])
    submit = SubmitField("Add Thoughts")

class CustomerForm(FlaskForm):
    f_name = StringField("First Name:" , validators=[DataRequired()] )
    l_name = StringField("Last Name: ", validators=[DataRequired()] )
    submit = SubmitField("Create")
    def stop_duplication(self,f_name):
        name_dupe= Customer.query.filter_by(f_name=f_name.data).first()
        if name_dupe:
            raise ValidationError ("This name already exists")


