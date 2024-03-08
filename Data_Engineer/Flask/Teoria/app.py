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