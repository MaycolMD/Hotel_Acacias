from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime
import json

app = Flask(__name__)

# Required
app.config["MYSQL_USER"] = "user"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "database"

mysql = MySQL(app)

# Validate case of armed strike
cur = mysql.connection.cursor()
cur.execute("SELECT fechaInicio, fechaFin FROM tabla_paros")
data = cur.fetchall()
paro_activo = False
# Convertir todas las fechas en objetos datetime
for fecha_inicio, fecha_fin in data:
    fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d")
    fechaI = datetime.now()
    fechaF = datetime.now()

    # Hacer un between para validar que la fecha no esté en el paro armado
    if fecha_inicio_dt <= fechaI <= fecha_fin_dt: paro_activo = True
    if fecha_inicio_dt <= fechaF <= fecha_fin_dt: paro_activo = True

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

# Guardar paro armado desde JSON de la petición
@app.route('/guardar_json_paro', methods=['POST'])
def guardar_json_paro():
    # Obtener el JSON
    data = request.get_json()

    # Extraer los valores de fechaInicio, fechaFin y contexto del JSON
    fecha_inicio = data['fechaInicio']
    fecha_fin = data['fechaFin']
    contexto = data['contexto']

    # Guardar los valores en la base de datos
    cur = mysql.connection.cursor()
    query = "INSERT INTO tabla_paros (fechaInicio, fechaFin, contexto) VALUES (%s, %s, %s)"
    cur.execute(query, (fecha_inicio, fecha_fin, contexto))
    mysql.connection.commit()
    cur.close()

    return 'JSON guardado en la base de datos'

if __name__ == '__main__':
    app.run(debug = True)
