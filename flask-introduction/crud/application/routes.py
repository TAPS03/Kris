from ast import Compare
from application import app, db
from flask import redirect, render_template, request, url_for
from application.models import CustomerForm, Customer, Thoughts, ThoughtsForm, UpdateCustomer
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
            return redirect(url_for('put_thought'))
    return render_template('add.html', form=form)


@app.route('/put_thought', methods=["GET", "POST"])
def put_thought():
    form= ThoughtsForm()
    customers = Customer.query.all()
    for customer in customers:
        form.persons_thoughts.choices.append(
            (customer.id, f"{customer.f_name}"))
    if request.method == 'POST':
        if form.validate_on_submit():
            new_thought= Thoughts(favourite_book=form.favourite_book.data,rating= form.rating.data,why_like_book=form.why_like_book.data,compare=form.compare.data,persons_thoughts= form.persons_thoughts.data) 
            db.session.add(new_thought)
            db.session.commit()
            return redirect(url_for('all_thoughts'))
    return render_template('put_thought.html', form= form)

@app.route('/all_thoughts')
def all_thoughts():
    all_thoughts = Thoughts.query.all()
    all_customers= Customer.query.all()
    return render_template('all_thoughts.html', all_thoughts=all_thoughts, all_customers=all_customers )

@app.route('/updatecustomer/<f_name>', methods=['GET', 'POST'])
def updatecustomer(f_name):
    update_customer = UpdateCustomer()
    customer = Customer.query.filter_by(f_name=f_name).first()
    
    if update_customer.validate_on_submit():
        customer.f_name = update_customer.f_name.data
        db.session.commit()
        return redirect(url_for('all_thoughts'))
    return render_template('update_customer.html', form=update_customer)

@app.route('/deletecustomer/<f_name>', methods=['GET', 'POST'])
def deletecustomer(f_name):
        customer = Customer.query.filter_by(f_name=f_name).first()
        db.session.delete(customer)
        db.session.commit()
        return redirect(url_for('all_thoughts'))

@app.route('/deletethoughts/<f_name>', methods=['GET', 'POST'])
def deletethoughts(f_name):
        thoughts = Thoughts.query.filter_by(f_name=f_name).first()
        db.session.delete(thoughts)
        db.session.commit()
        return redirect(url_for('all_thoughts'))
   
        


