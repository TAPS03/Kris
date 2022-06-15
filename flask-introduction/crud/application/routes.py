from ast import Compare
from application import app, db
from flask import redirect, render_template, request
from application.models import CustomerForm, Customer, Thoughts, ThoughtsForm
import pdb


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def realhome():
    return render_template('home.html') 


@app.route('/', methods=["GET", "POST"])
def add_customer():
    form= CustomerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_customer= Customer(f_name=form.f_name.data, l_name=form.l_name.data)
            db.session.add(new_customer)
            db.session.commit()
            return render_template('put_thought.html', message = "Thank you {f_name} {l_name}, you have been added.")
    return render_template('add.html', form=form)


@app.route('/put_thought', methods=["GET", "POST"])
def put_thought():
    put_thought_form= ThoughtsForm()
    customers = Customer.query.all()
    for Customer in customers:
        put_thought_form.persons_thoughts.choices.append((Customer.id, f"(Customer,f_name)" f"(Customer.l_name"))
    if request.method == 'POST':
        if put_thought_form.validate_on_submit():
            new_thought= Thoughts(favourite_book=put_thought_form.favourite_book.data,rating= put_thought_form.rating.data,why_like_book=put_thought_form.why_like_book.data,compare=put_thought_form.compare.data,customer_id= put_thought_form.persons_thoughts.data) 
            db.session.add(new_thought)
            db.session.commit()
            return render_template('account.html')
    return render_template('/put_thought', form= put_thought_form)
   
        


