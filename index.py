from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime
import json
from database import DATABASE
from response import Response
app = Flask(__name__)

# Required
#app.config["MYSQL_USER"] = "user"
#app.config["MYSQL_PASSWORD"] = "password"
#app.config["MYSQL_DB"] = "database"

#mysql = MySQL(app)


# Página principal
@app.route('/')
def home():
    return render_template('index.html')

# Página reservas


@app.route('/booking')
def reserva():
    return render_template('reserva.html')

# Página buscar


@app.route('/search')
def search():
    return render_template('roomsearch.html')


@app.route('/api/disponibilidadHab')
def disponibilidad():
    db = DATABASE()
    try:
        habs = db.show_habitaciones_disponibles("2023-05-22", "2023-05-30")
        if len(habs) > 0:
            response = Response("ok", habs, "")
        else:
            response = Response(
                "failed", [], "No hay habitaciones disponibles")
    except:
        response = Response("failed", [], "Error al comunicarse con la DB")
    return json.dumps(response, default=vars), {"Content-Type": "application/json"}

@app.route('/api/paros')
def paros():
    db = DATABASE()
    try:
        paros = db.getAlertasDeParo()
        if len(paros) > 0:
            response = Response("ok", paros, "")
        else:
            response = Response(
                "failed", [], "No hay paros")
    except:
        response = Response("failed", [], "Error al comunicarse con la DB")
    return json.dumps(response, default=vars), {"Content-Type": "application/json"}


@app.route('/api/reservas')
def reservas():
    db = DATABASE()
    try:
        reservas = db.getReservas()
        if len(reservas) > 0:
            response = Response("ok", reservas, "")
        else:
            response = Response(
                "failed", [], "No hay reservas")
    except:
        response = Response("failed", [], "Error al comunicarse con la DB")
    return json.dumps(response, default=vars), {"Content-Type": "application/json"}

@app.route('/api/reservasActivas')
def reservasActivas():
    db = DATABASE()
    try:
        reservas = db.getReservas()
        if len(reservas) > 0:
            response = Response("ok", reservas, "")
        else:
            response = Response(
                "failed", [], "No hay reservas")
    except:
        response = Response("failed", [], "Error al comunicarse con la DB")
    return json.dumps(response, default=vars), {"Content-Type": "application/json"}

# Guardar paro armado desde JSON de la petición
# @app.route('/guardar_json_paro', methods=['POST'])
# def guardar_json_paro():
    # Obtener el JSON
#    data = request.get_json()

    # Extraer los valores de fechaInicio, fechaFin y contexto del JSON
#    fecha_inicio = data['fechaInicio']
#    fecha_fin = data['fechaFin']
#    contexto = data['contexto']

    # Guardar los valores en la base de datos
#    cur = mysql.connection.cursor()
#    query = "INSERT INTO tabla_paros (fechaInicio, fechaFin, contexto) VALUES (%s, %s, %s)"
#    cur.execute(query, (fecha_inicio, fecha_fin, contexto))
#    mysql.connection.commit()
#    cur.close()

#    return 'JSON guardado en la base de datos'


if __name__ == '__main__':
    app.run(debug=True)