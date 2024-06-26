from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<center><h1>¿Que operacion quieres hacer?</h1></center><br>(/muntiplicacion) para multiplicar<br>(/suma) para sumar<br>(/resta)para restar<br>(?division) para dividir'

@app.route('/suma/<int:num1>,<int:num2>')
@app.route('/suma/<int:num1>,<int:num2>,<int:num3>')
@app.route('/suma/<int:num1>,<int:num2>,<int:num3>,<int:num4>')
def suma(num1, num2, num3=None, num4=None):
    if num3 is None and num4 is None:
        resultado = num1 + num2
        return f'<center><h1>{num1} + {num2} = {resultado}</h1></center>'
    elif num4 is None:
        resultado = num1 + num2 + num3
        return f'<center><h1>{num1} + {num2} + {num3} = {resultado}</h1></center>'
    else:
        resultado = num1 + num2 + num3 + num4
        return f'<center><h1>{num1} + {num2} + {num3} + {num4} = {resultado}</h1></center>'

@app.route('/resta/<int:num1>,<int:num2>')
@app.route('/resta/<int:num1>,<int:num2>,<int:num3>')
@app.route('/resta/<int:num1>,<int:num2>,<int:num3>,<int:num4>')
def resta(num1, num2, num3=None, num4=None):
    if num3 is None and num4 is None:
        resultado = num1 - num2
        return f'<center><h1>{num1} - {num2} = {resultado}</h1></center>'
    elif num4 is None:
        resultado = num1 - num2 - num3
        return f'<center><h1>{num1} - {num2} - {num3} = {resultado}</h1></center>'
    else:
        resultado = num1 - num2 - num3 - num4
        return f'<center><h1>{num1} - {num2} - {num3}  - {num4} = {resultado}</h1></center>'

@app.route('/division/<int:num1>,<int:num2>')
@app.route('/division/<int:num1>,<int:num2>,<int:num3>')
@app.route('/division/<int:num1>,<int:num2>,<int:num3>,<int:num4>')
def div(num1, num2, num3=None, num4=None):
    if num3 is None and num4 is None:
        resultado = num1 // num2
        return f'<center><h1>{num1} ÷ {num2} = {resultado}</h1></center>'
    elif num4 is None:
        resultado = num1 // num2 // num3
        return f'<center><h1>{num1} ÷ {num2} ÷ {num3} = {resultado}</h1></center>'
    else:
        resultado = num1 // num2 // num3 // num4
        return f'<center><h1>{num1} ÷ {num2} ÷ {num3} ÷ {num4} = {resultado}</h1></center>'

@app.route('/multiplicacion/<int:num1>,<int:num2>')
@app.route('/multiplicacion/<int:num1>,<int:num2>,<int:num3>')
@app.route('/multiplicacion/<int:num1>,<int:num2>,<int:num3>,<int:num4>')
def multi(num1, num2, num3=None, num4=None):
    if num3 is None and num4 is None:
        resultado = num1 * num2
        return f'<center><h1>{num1} × {num2} = {resultado}</h1></center>'
    elif num4 is None:
        resultado = num1 * num2 * num3
        return f'<center><h1>{num1} × {num2} × {num3} = {resultado}</h1></center>'
    else:
        resultado = num1 * num2 * num3 * num4
        return f'<center><h1>{num1} × {num2} × {num3} × {num4} = {resultado}</h1></center>'

if __name__ == '__main__':
    app.run()