Iris Classification Web App

Overview:

This project is a web application that predicts the species of an Iris flower based on its sepal length, sepal width, petal length, and petal width. The application uses a machine learning model trained on the famous Iris dataset. The model is served using Flask, a lightweight web framework for Python.

Features:

User-friendly web interface to input flower measurements.

Real-time prediction of Iris species based on input data.

Trained using a RandomForestClassifier from the scikit-learn library.

Usage:

Open your web browser and navigate to https://iris-classification-5.onrender.com/  .

Enter the sepal length, sepal width, petal length, and petal width of the Iris flower.

Click the "Predict" button to see the predicted species of the Iris flower.

File Structure:

deploy.py: The Flask application that serves the web interface and handles predictions.

train_model.py: Script to train the RandomForestClassifier on the Iris dataset and save the model.

saved_model.pkl: The trained machine learning model.

templates/: Directory containing HTML templates for the web app.
index.html: Main page of the web app.

