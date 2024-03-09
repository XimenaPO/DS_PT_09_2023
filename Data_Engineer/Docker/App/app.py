from flask import Flask, request, render_template
import pickle
import os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

model = pickle.load(open('model.pkl', 'rb'))

print(model)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/user/<name>', methods=['GET'])
def user(name):
    return render_template('saludar.html', name=name)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    a = float(data.get('a'))
    b = float(data.get('b'))
    c = float(data.get('c'))
    d = float(data.get('d'))
    prediction = model.predict([[a,b,c,d]])
    
    return 'La predicción es {}'.format(prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)