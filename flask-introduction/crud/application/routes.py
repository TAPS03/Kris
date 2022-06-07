from application import app, db
from flask import render_template, request
from application.models import CustomerForm, Customer



@app.route('/')
def home():
    return render_template('home.html')



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
            new_customer= Customer(f_name=form.f_name.data, l_name=form.l_name.data, email=form.email.data, username=form.username.data, password=form.password.data, confirm_password=form.confirm_password.data ,address=form.address.data ,postcode=form.postcode.data)
            db.session.add(new_customer)
            db.session.commit()
            return render_template('home.html', message = "Thank you {f_name} {l_name}, your account has been created.")
    else:
        return render_template('account.html', form=form)


