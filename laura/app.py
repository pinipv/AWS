from flask import Flask, render_template, request
import pickle
import numpy as np

def load_model():
    with open(r'borrador_parte2\modelos\rf_model.pkl', "rb") as archivo_entrada:
        model = pickle.load(archivo_entrada)
        # print(list_models)
    return model

app = Flask(__name__)

# modelo de predicción
#model = pickle.load(open("!! Aquí poner nombre fichero .pkl con el modelo de predicción", 'rb'))

# Homepage 
@app.route("/", methods = ["GET"]) # ruta
def index():
    return render_template("homepage.html") # aquí ponemos el html con la homepage

# Página insertar datos 
@app.route("/data_input/", methods=["POST"]) # ruta
def data_input():
    return render_template("data_page.html") # aquí ponemos el html con la pg donde insertamos los datos para predicción

# Página con la predicción
@app.route('/data_input/predict/', methods=['GET', 'POST']) 
def predict():
        seasons={'spring':0, 
                'summer':1, 
                'fall':2,
                'winter':3
                }
        weathers={'clear':0, 
                    'few clouds':1, 
                    'partly cloudly':2
        }

        season = request.form['season']
        weather = request.form['weather']
        temp = request.form['temp']
        humidity = request.form['humidity']
        date = request.form['date']
        hour = request.form['hour']

        year, month, day = date.split('-')

        data= np.array([seasons[season.lower()],weathers[weather.lower()], int(temp), int(humidity),int( year),int(month), int(day),int( hour)])
        model = load_model()
        #Hago el reshape ya que al predecir una sola instancia por fallo y error solo me ha funcionado asi
        pred= model.predict(data.reshape(1,-1))
        #EL modelo devuelve una lista, recojo la primera y unica posicion y lo redondeo al mayor para que de un numero entero
        final_pred= round(pred[0]) 
        return render_template('predict.html', data=int(final_pred))

'''def predict():

    # Parámetros del usuario
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
'''

    

    
if __name__ == "__main__":
    app.run(debug=True) # MUY IMPORTANTE!!!!! debug = False antes de despliegue a servidor público