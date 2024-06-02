from flask import Flask, render_template, request
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('saved_model1.pkl', 'rb'))

# Map numerical prediction to class names
class_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

@app.route('/')
def home():
    result = ''
    return render_template('index.html', result=result)

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        
        # Ensure all fields are filled
        if not all([sepal_length, sepal_width, petal_length, petal_width]):
            result = 'Please fill out all fields.'
        else:
            prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
            result = class_names[prediction]
    except ValueError:
        result = 'Invalid input. Please enter valid numbers.'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
