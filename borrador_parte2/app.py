from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# modelo de predicción
model = pickle.load(open("!! Aquí poner nombre fichero .pkl con el modelo de predicción", 'rb'))

# Homepage
@app.route("/", methods = ["GET"]) # ruta
def man():
    return render_template("homepage.html") # aquí ponemos el html con la homepage

# Página insertar datos
@app.route("/data", methods=["POST"]) # ruta
def data():
    return render_template("data_page.html") # aquí ponemos el html con la pg donde insertamos los datos para predicción

# Página predicción --> esto hay que ver cómo es: NO CLASIFICACIÓN --> NÚMEROS
@app.route("/predict", methods=["POST"]) # ruta
def home():

    # Esto hay que cambiarlo ---> son los 4 datos de las flores para predecir que tipo es:
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]]) # los 4 datos de las flores
    pred = model.predict(arr)   # el modelo predice según los datos que insertamos
    return render_template("after.html", data = pred) 


if __name__ == "__main__":
    app.run(debug=True)