from flask import render_template, request, redirect, url_for
from app import app
import requests
from http import HTTPStatus

url = 'https://official-joke-api.appspot.com/random_joke'


def get_joke(url):
    try:
        response = requests.get(url)
        if response.status_code == HTTPStatus.OK:
            data = response.json()
            return f"{data['setup']} {data['punchline']}"
        else:
            return f'{response.status_code}'
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return 'Failed to load a joke'


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/result")
def result():
    return render_template("result.html")


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        color = request.form.get('color')
        profession = request.form.get('profession')
        hobbies = request.form.getlist('hobbies')
        level = request.form.get('level')
        joke = get_joke(url)

        if not name:
            error = "Мы не можем обработать форму без вашего имени, мистер Аноним!"
            return render_template('form.html', error=error)
        if not email:
            error = 'Без почты не пройдешь, введи свой email'
            return render_template('form.html', error=error)

        return render_template('result.html',
                               name=name, email=email, color=color,
                               profession=profession, hobbies=hobbies,
                               level=level, joke=joke)

    else:
        return redirect(url_for('form'))





