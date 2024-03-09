<<<<<<< HEAD
from flask import Flask 
from config import BCRYPT_LOG_ROUNDS # esta es una forma de hacerlo. Juan prefiere otra

app = Flask(__name__)

print(app)

@app.route('/')
def index():
    print(BCRYPT_LOG_ROUNDS) # importado desde config, que es = a 12. NO SE IMPORTA ASÍ IGUAL!! 
    return "<h1>Hello World!</h1>"

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

    
@app.route("/user/<name>/<int:index>")
def index2(name, index):
    mylist = ['elemento1', 'elemento2', 'elemento3', 'elemento4']
    mydict = {'key': 'valor'}
    mytuple = ('tuple1', 'tuple2', 'tuple3', 'tuple4')
    return name, index, mylist, mydict, mytuple


## Siempre es bueno colocar lo siguiente al final de un archivo.. 
if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, jsonify, render_template
import numpy as np
from datetime import datetime

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
# app.config.from_pyfile("Data_Engineer/Flask/Teoria/config.py")

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/user/<name>")
def index4(name):
    index=1
    mylist = ['elemento1', 'elemento2', 'elemento3', 'elemento4']
    mydict = {'key': 'valor'}
    mytuple = ('tuple1', 'tuple2', 'tuple3', 'tuple4')
    return render_template("home.html", name=name, myindex=index, mylist=mylist, mydict=mydict, mytuple=mytuple)

@app.route('/nombres')
def nombres():
    nombres = ['Juan', 'Ana', 'Carlos', 'María']  # Esta lista puede ser obtenida de forma dinámica
    return render_template('nombres.html', nombres=nombres)

@app.route('/rodrigo')
def index1():
    return "<h1>Rodrigo estuvo aquí!</h1>"

print('esto no funciona')

@app.route(f"/user/{app.config['BCRYPT_LOG_ROUNDS']}/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

@app.route("/user/<name>/<int:ind>")
def index2(name, ind):
    mylist = ['2024/03/06', 'elemento2', False, 'elemento4']
    mydict = {'key': -ind}
    mytuple = (datetime.now().date().strftime('%Y/%m/%d'), None, 'tuple3', np.nan)
    return jsonify(name=name, myindex=ind, mylist=mylist, mydict=mydict, mytuple=mytuple)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=8910)
>>>>>>> upstream/main
