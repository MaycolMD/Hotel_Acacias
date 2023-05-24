from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL

import json
from flask_cors import CORS
from database import DATABASE
from response import Response
app = Flask(__name__)
CORS(app)


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


@app.route('/api/huespedes')
def huespedes():
    db = DATABASE()
    try:
        huespedes = db.getHuespedes()
        if len(huespedes) > 0:
            response = Response("ok", huespedes, "")
        else:
            response = Response(
                "failed", [], "No hay huespedes")
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


@app.route('/api/buscador')
def buscador():
    tipo = request.args.get('tipo')
    fechaInicio = request.args.get('fechaInicio')
    fechaFin = request.args.get('fechaFin')
    adultos = int(request.args.get('adultos'))
    niños = int(request.args.get('niños'))
    bebes = int(request.args.get('bebes'))
    habitaciones = int(request.args.get('habitaciones'))

    db = DATABASE()
    huespedes = adultos + niños + bebes
    try:
        rooms = db.getHabitaciones(
            tipo, fechaInicio, fechaFin, huespedes, habitaciones)
        if len(rooms) > 0:
            response = Response("ok", rooms, "")
        else:
            response = Response(
                "failed", [], "No hay habitaciones")
    except Exception as e:
        response = Response(
            "failed", [], "Error al comunicarse con la DB: "+str(e))
    return json.dumps(response, default=vars), {"Content-Type": "application/json"}


@app.route('/api/obtenerid')
def obtener_id():
    db = DATABASE()
    tipo = request.args.get('tipo')
    fechaInicio = request.args.get('fechaInicio')
    fechaFin = request.args.get('fechaFin')
    try:
        id = db.verificar_id_habitacion(tipo,fechaInicio,fechaFin)
        if len(id) > 0:
            response = Response("ok", id, "")
        else:
            response = Response(
                "failed", [], "No hay disponibilidad")
    except:
        response = Response("failed", [], "Error al comunicarse con la DB")
    return json.dumps(response, default=vars), {"Content-Type": "application/json"}

@app.route('/api/reservar')
def obtener_id():
    db = DATABASE()
    tipo = request.args.get('tipo')
    f_in = request.args.get('fechaInicio')
    f_out = request.args.get('fechaFin')
    cantidad_habitacion = int(request.args.get('habitaciones'))
    ID_CLIENTE = int(request.args.get('id_cliente'))
    ID_HABITACION = int(request.args.get('id_hab'))
    NACIONALIDAD = request.args.get('nacionalidad')
    ORIGEN = request.args.get('origen')
    NOMBRES = request.args.get('nombres')
    APELLIDOS = request.args.get('apellidos')
    try:
        reserva = db.ingresar_datos_reserva(tipo, f_in, f_out, cantidad_habitacion, ID_CLIENTE, ID_HABITACION, NACIONALIDAD, ORIGEN, NOMBRES, APELLIDOS)
        if len(reserva) > 0:
            response = Response("ok", reserva, "")
        else:
            response = Response(
                "failed", [], "No hay disponibilidad")
    except:
        response = Response("failed", [], "Error al comunicarse con la DB")
    return json.dumps(response, default=vars), {"Content-Type": "application/json"}

if __name__ == '__main__':
    app.run(debug=True)
