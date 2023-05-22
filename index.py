from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime
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
        rooms = db.getHabitaciones(tipo, fechaInicio, fechaFin, huespedes, habitaciones)
        if len(rooms) > 0:
            response = Response("ok", rooms, "")
        else:
            response = Response(
                "failed", [], "No hay habitaciones")
    except:
        response = Response("failed", [], "Error al comunicarse con la DB")
    return json.dumps(response, default=vars), {"Content-Type": "application/json"}

if __name__ == '__main__':
    app.run(debug=True)