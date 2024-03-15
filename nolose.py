from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return 'hola mundo'

@app.route('/home/<name>')
def home(name):
    return f'esto es la pagina de inicio de {name}'

@app.route('/login')
def login():
    return 'bienvenido'


if __name__ == '__main__':
    app.run(debug=True)