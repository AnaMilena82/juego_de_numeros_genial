from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"


numero_aleatorio = random.randint(1, 100) 		# random number between 1-100
intentos = 0
ganadores =[]

@app.route('/', methods = ['GET'])    
def get_adivinarnumero():
    global intentos
    intentos = 0
    
    return render_template("index.html", mostrar_juego_nuevo=False)

@app.route('/', methods = ['POST'])    
def pos_adivinarnumero():
    global intentos
    if intentos == 5:
        mensaje = 'Tú pierdes. ¡Inténtalo de nuevo!'
        intentos = 0
        return render_template('index.html', mensaje=mensaje,mostrar_juego_nuevo=True, mostrar_input_nombre=False, intentos=intentos)
    
    numero_adivinado = int(request.form['numero'])
    
    intentos +=1
    if numero_adivinado == numero_aleatorio:
        mensaje = '¡Felicidades! Has adivinado el número. en {} intentos.'.format(intentos)
        return render_template('index.html', mensaje=mensaje, mostrar_juego_nuevo=False, mostrar_input_nombre=True, intentos=intentos)
    
    elif numero_adivinado < numero_aleatorio:
        mensaje = 'número enviado es demasiado bajo.'
    else:
        mensaje = 'número enviado es demasiado alto.'
    return render_template('index.html', mensaje=mensaje, mostrar_juego_nuevo=False, mostrar_input_nombre=False, intentos=intentos)


@app.route('/marcador')
def marcador():
    return render_template('marcador.html', ganadores=ganadores)

@app.route('/guardar_nombre', methods=['POST'])
def guardar_nombre():
    nombre_ganador = request.form['nombre']
    intentos_ganador = request.form.get('intentos')
    if intentos_ganador is not None and intentos_ganador.isdigit():
        intentos_ganador = int(intentos_ganador)
        ganadores.append({'nombre': nombre_ganador, 'intentos': intentos_ganador})
        return redirect(url_for('marcador'))
    else:
        return "Error: el número de intentos no es válido"

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

