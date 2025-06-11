from flask import render_template, request, url_for, redirect, flash
from app import app
from app.forms import ContactForm
from datetime import datetime


@app.route('/')
def index():
    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)


@app.route('/about')
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template('about.html', team_members=team_members)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    department_info = {
        'manager': {
            'name': 'Ирина Смирнова',
            'position': 'Менеджер по работе с клиентами',
            'email': 'irina@gmail.com'
        },
        'address': {
            'street': 'ул. Есенина, д. Каруселина',
            'city': 'Москва',
            'zip': '12345'
        }
    }

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))

    if request.method == 'POST':
        flash('There were errors in the form', 'error')

    return render_template('contact.html', form=form, department_info=department_info)





