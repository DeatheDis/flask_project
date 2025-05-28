from app import app


@app.route('/')
def index():
    return 'This is start page!'


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/info')
def info():
    return 'This is the informational page'


@app.route('/calc/<first_number>/<second_number>')
def calc(first_number, second_number):
    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        return 'First number or second number must be digit'

    result = first_number + second_number
    return f'The sum of {first_number} and {second_number} is {result}'


@app.route('/reverse/')
@app.route('/reverse/<word>')
def reverse(word=None):
    if not word:
        return 'Enter a word'
    return f'The reverse of {word} is {word[::-1]}'


@app.route('/user/<name>/<int:age>')
def user(name, age):
    if age <= 0:
        return 'Your age must be more than 0'
    return f'Hello, {name}. You are {age} years old.'

