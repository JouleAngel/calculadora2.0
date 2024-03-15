from flask import Flask
app = Flask(__name__)
@app.route('/home/<name>')
def home(name):
    return f'<h1>Tu nombre es {name} ¿No?</h1>'
if __name__ == '__main__':
    app.run(debug=True)