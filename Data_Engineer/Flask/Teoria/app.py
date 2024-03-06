from flask import Flask 

app = Flask(__name__)

print(app)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"


## Siempre es bueno colocar lo siguiente al final de un archivo.. 
if __name__ == '__main__':
    app.run(debug=True)