from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable= False)
    l_name = db.Column(db.String(30), nullable= False)
    email = db.Column(db.String(40), nullable= False)
    username = db.Column(db.String(40), nullable= False)
    password = db.Column(db.String(40), nullable= False)
    address = db.Column(db.String(30), nullable= False)
    postcode = db.Column(db.String(10), nullable= False)
#     orders = db.relationship('Orders', backref='customer', lazy= True)

# class Orders(db.Model):
#     customer_id= db.Column(db.Integer, db.ForeignKey('customer_id', nullable= False))
#     order_number = db.Column(db.String(15), nullable= False)
#     deliver_address = db.Column(db.String(50), nullable= False)
#     amount = db.Column(db.Float(40), nullable= False)
   






class CustomerForm(FlaskForm):
    f_name = StringField("First Name:" , validators=[DataRequired()] )
    l_name = StringField("Last Name: ", validators=[DataRequired()] )
    email = StringField("Email Address:", validators=[DataRequired()] )
    username = StringField("Username:", validators=[DataRequired()], )
    password = PasswordField("Password:", validators=[DataRequired()] )
    confirm_password = PasswordField("Confirm Password:", validators=[DataRequired()] )
    address = StringField("Street number and Name:", validators=[DataRequired()] )
    postcode = StringField("PostCode:", validators=[DataRequired()] )
    submit = SubmitField("Create")








db.create_all()