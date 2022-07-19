from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# modelo de predicción
model = pickle.load(open("!! Aquí poner nombre fichero .pkl con el modelo de predicción", 'rb'))

# Homepage 
@app.route("/", methods = ["GET"]) # ruta
def index():
    return render_template("homepage.html") # aquí ponemos el html con la homepage

# Página insertar datos 
@app.route("/data_input/", methods=["POST"]) # ruta
def data_input():
    return render_template("data_page.html") # aquí ponemos el html con la pg donde insertamos los datos para predicción

# Página con la predicción
@app.route('/predict/', methods=['GET', 'POST'])
def predict():

    # Usuario introduce los parámetros
    param_1 = request.form['parametro1']
    param_2 = request.form['parametro2']
    param_3 = request.form['parametro3']
    param_4 = request.form['parametro4']
    param_5 = request.form['parametro5']
    param_6 = request.form['parametro6']

    # array para predicción
    arr = np.array([[param_1, param_2, param_3, param_4, param_5, param_6]])

    # predicción
    pred = model.predict([arr])

    return render_template('predict.html', data=int(pred)) # aquí vamos a la página con la predicción

if __name__ == "__main__":
    app.run(debug=True) # MUY IMPORTANTE!!!!! debug = False antes de despliegue a servidor público