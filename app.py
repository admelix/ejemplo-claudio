from flask import Flask, render_template, request
from sympy import *
from numpy import *

app = Flask(__name__)
#en el secret key puedes poner cualquier cosa. No necesariamente lo que puse entre comillas simples. 
app.config['SECRET_KEY'] = 'f4ab65a793836b7ae8cc6646bd0c6ccd'


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        expression = request.form.get('expression')
        result = simplify(expression)# calcula lo que el usuario ingresa usando sympy
        result1 = simplify(expression)
    else:
        result1 = None

    return render_template('index.html', result1=result1)#pinta en la pagina web el resultado


if __name__ == '__main__':
    app.run(debug=True)


