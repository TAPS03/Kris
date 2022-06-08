from application import app, db
from flask import render_template, request
from application.models import CustomerForm, Customer
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/placeOrder')
def placeOrder():
    return render_template('placeOrder.html')



@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def realhome():
    return render_template('home.html')


@app.route('/account', methods=["GET", "POST"])
def add_customer():
    form= CustomerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            password_to_save=generate_password_hash(form.password.data("password"), method='sha256')
            new_customer= Customer(f_name=form.f_name.data, l_name=form.l_name.data, email=form.email.data, username=form.username.data, password=password_to_save, confirm_password=password_to_save ,address=form.address.data ,postcode=form.postcode.data)
            if form.get('password') !=form.get('confirm_password'): 
                return render_template('account.html', message = "passwords do not match")
            user = user.query.filter_by(username=user).first()
            db.session.add(new_customer)
            db.session.commit()
            return render_template('home.html', message = "Thank you {f_name} {l_name}, your account has been created.")
    else:
        return render_template('account.html', form=form)


