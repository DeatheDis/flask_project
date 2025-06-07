from flask import render_template, request, url_for, redirect, flash
from app import app
from app.forms import ContactForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))

    if request.method == 'POST':
        flash('There were errors in the form', 'error')

    return render_template('contact.html', form=form)





