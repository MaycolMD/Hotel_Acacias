import datetime
import json

import pymysql
from Huesped import Huesped

from habitacion import Habitacion
from Paro import Paro
from reserva import Reserva
from response import Response
from Room import Room


class DATABASE:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost", user="root", password="maycol", db="hotel_acacias"
        )

        self.cursor = self.connection.cursor()

    def getReservas(self):
        query = "Select * from reservas"
        try:
            self.cursor.execute(query)
            reservas = self.cursor.fetchall()
            responseArray = []
            for reserva in reservas:
                print(reserva)
                res = Reserva(reserva[0], reserva[1], reserva[2], reserva[3], reserva[4],
                              reserva[5], reserva[6], reserva[7], reserva[8], reserva[9])
                responseArray.append(res)
            return responseArray
        except Exception as e:
            raise

    def getReservasActivas(self):
        query = "Select * from reservas where ESTADO = 'ACTIVO'"
        try:
            self.cursor.execute(query)
            reservas = self.cursor.fetchall()
            responseArray = []
            for reserva in reservas:
                print(reserva)
                res = Reserva(reserva[0], reserva[1], reserva[2], reserva[3], reserva[4],
                              reserva[5], reserva[6], reserva[7], reserva[8], reserva[9])
                responseArray.append(res)
            return responseArray
        except Exception as e:
            raise

    def show_habitaciones_disponibles(self, f_in, f_out):
        query = f"""SELECT MIN(ID_HABITACION), TIPO
                    FROM INVENTARIO_HABITACION
                    WHERE NOT `ID_HABITACION` IN
                        (SELECT I.`ID_HABITACION`
                        FROM RESERVAS R CROSS JOIN INVENTARIO_HABITACION I
                        ON R.ID_HABITACION = I.ID_HABITACION
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}"))
                    GROUP BY TIPO;"""
        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()
            responseArray = []
            for room in rooms:
                hab = Habitacion(room[1], room[0])
                responseArray.append(hab)
            return responseArray
        except Exception as e:
            raise

    # Versión general de las 3 funciones de abajo
    def verificar_disponibilidad_habitacion(self, tipo, f_in, f_out, cantidad):
        query = f"""SELECT COUNT(ID_HABITACION)
                    FROM INVENTARIO_HABITACION
                    WHERE ID_HABITACION IN
                        (SELECT I.`ID_HABITACION`
                        FROM RESERVAS R CROSS JOIN INVENTARIO_HABITACION I
                        ON R.ID_HABITACION = I.ID_HABITACION
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        AND TIPO = "{tipo}");"""

        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()
            if tipo == "Uso compartido":
                if rooms[0][0] >= 10 - cantidad + 1:
                    print("No hay disponibilidad")
                else:
                    print("Disponible")
            elif tipo == "Simple" | tipo == "Doble":
                if rooms[0][0] >= 15 - cantidad + 1:
                    print("No hay disponibilidad")
                else:
                    print("Disponible")
        except Exception as e:
            raise

    def verificar_disponibilidad_uso_compartido(self, f_in, f_out, cantidad):
        query = f"""SELECT COUNT(ID_HABITACION)
                    FROM INVENTARIO_HABITACION
                    WHERE ID_HABITACION IN
                        (SELECT I.`ID_HABITACION`
                        FROM RESERVAS R CROSS JOIN INVENTARIO_HABITACION I
                        ON R.ID_HABITACION = I.ID_HABITACION
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        AND TIPO = "Uso compartido");"""

        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()

            if rooms[0][0] >= 10 - cantidad + 1:
                print("No hay disponibilidad")
            else:
                print("Disponible")
        except Exception as e:
            raise

    def verificar_disponibilidad_simple(self, f_in, f_out, cantidad):
        query = f"""SELECT COUNT(ID_HABITACION)
                    FROM INVENTARIO_HABITACION
                    WHERE ID_HABITACION IN
                        (SELECT I.`ID_HABITACION`
                        FROM RESERVAS R CROSS JOIN INVENTARIO_HABITACION I
                        ON R.ID_HABITACION = I.ID_HABITACION
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        AND TIPO = "Simple");"""

        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()

            if rooms[0][0] >= 15 - cantidad + 1:
                print("No hay disponibilidad")
            else:
                print("Disponible")
        except Exception as e:
            raise

    def verificar_disponibilidad_doble(self, f_in, f_out, cantidad):
        query = f"""SELECT COUNT(ID_HABITACION)
                    FROM INVENTARIO_HABITACION
                    WHERE ID_HABITACION IN
                        (SELECT I.`ID_HABITACION`
                        FROM RESERVAS R CROSS JOIN INVENTARIO_HABITACION I
                        ON R.ID_HABITACION = I.ID_HABITACION
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        AND TIPO = "Doble");"""

        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()

            if rooms[0][0] >= 15 - cantidad + 1:
                print("No hay disponibilidad")
            else:
                print("Disponible")
        except Exception as e:
            raise

    def insertarParo(self, f_in, f_out, context):
        try:
            # Create a cursor object to execute SQL queries
            cursor = self.connection.cursor()

            # SQL statement to insert the strike alert into the database
            sql = "INSERT INTO paros (start_date, end_date, context) VALUES (%s, %s, %s)"
            start_date = datetime.strptime(f_in, '%Y-%d-%m').date()
            end_date = datetime.strptime(f_in, '%Y-%d-%m').date()
            # Execute the SQL statement with the provided parameters
            cursor.execute(sql, (start_date, end_date, context))

            # Commit the changes to the database
            self.connection.commit()

            return Response("ok", [], "")

        except pymysql.Error as e:
            return Response("ok", [], "Error al registrar paro: " + e)

    def verificar_disponibilidad_parqueadero(self, f_in, f_out):
        query = f"""SELECT COUNT(ID_PARQUEADERO)
                    FROM PARQUEADERO
                    WHERE ID_PARQUEADERO IN
                        (SELECT P.ID_PARQUEADERO
                        FROM RESERVAS R CROSS JOIN PARQUEADERO P
                        ON R.`ID_RESERVA` = P.`ID_RESERVA`
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}"));"""

        try:
            self.cursor.execute(query)
            park = self.cursor.fetchall()

            if park[0][0] >= 25:
                print("No hay disponibilidad")
            else:
                print("Disponible")
        except Exception as e:
            raise

    def getAlertasDeParo(self):
        query = "Select * from paros"

        try:
            self.cursor.execute(query)
            paros = self.cursor.fetchall()
            responseArray = []
            for paro in paros:
                par = Paro(paro[0], paro[1], paro[2])
                responseArray.append(par)
            return responseArray
        except Exception as e:
            raise

    def getHuespedes(self):
        query = "SELECT NOMBRES, APELLIDOS, NACIONALIDAD, ORIGEN, ID_CLIENTE from reservas"
        try:
            self.cursor.execute(query)
            huespedes = self.cursor.fetchall()
            responseArray = []
            for huesped in huespedes:
                guest = Huesped(huesped[0], huesped[1],huesped[2], huesped[3], huesped[4])
                responseArray.append(guest)
            return responseArray
        except Exception as e:
            raise
    def verificar_disponibilidad_restaurante(self, hora, f_in, f_out, cantidad):
        query = f"""SELECT COUNT(ID_MESA)
                    FROM RESTAURANTE
                    WHERE ID_MESA IN
                        (SELECT RE.`ID_MESA`
                        FROM RESERVAS R CROSS JOIN RESTAURANTE RE
                        ON R.ID_RESERVA = RE.ID_RESERVA
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        AND RE.HORARIO = "{hora}");"""

        try:
            self.cursor.execute(query)
            mesa = self.cursor.fetchall()

            if mesa[0][0] >= 40 - cantidad + 1:
                print("No hay disponibilidad")
            else:
                print("Disponible")
        except Exception as e:
            raise
    
    # Hora esta en el formato datetime (YY-MM-DD HH-MM-SS)
    def verificar_disponibilidad_transporte(self, hora, cantidad):
        query = f"""SELECT COUNT(ID_BUS)
                    FROM TRANSPORTE
                    WHERE ID_BUS IN
                        (SELECT B.`ID_BUS`
                        FROM RESERVAS R CROSS JOIN TRANSPORTE B
                        ON R.ID_RESERVA = B.ID_RESERVA
                        AND B.HORARIO = "{hora}");"""

        try:
            self.cursor.execute(query)
            asiento = self.cursor.fetchall()

            if asiento[0][0] >= 20 - cantidad + 1:
                print("No hay disponibilidad")
            else:
                print("Disponible")
        except Exception as e:
            raise
    
    # Validate case of armed strike
    def verificar_disponibilidad_paro_armado(self, f_inicio, f_fin):
        query = f"SELECT inicio, fin FROM paros"

        try:
            self.cursor.execute(query)
            paros = self.cursor.fetchall()
            paro_activo = False

            for fecha_inicio, fecha_fin in paros:
                f_I = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                f_F = datetime.strptime(fecha_fin, "%Y-%m-%d")
                # Hacer un between para validar que la fecha no esté en el paro armado
                if f_I <= f_inicio <= f_F: paro_activo = True
                if f_I <= f_fin <= f_F: paro_activo = True

            if paro_activo:
                print("No hay disponibilidad")
            else:
                print("Disponible")
        except Exception as e:
            raise

        # Buscador
    def getHabitaciones(self, tipo, f_in, f_out, huespedes, habitaciones):
        query = f"""SELECT *
                    FROM hotel_acacias.INVENTARIO_HABITACION
                    WHERE ID_HABITACION NOT IN
                        (SELECT I.`ID_HABITACION`
                        FROM hotel_acacias.RESERVAS R CROSS JOIN hotel_acacias.INVENTARIO_HABITACION I
                        ON R.ID_HABITACION = I.ID_HABITACION
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        AND TIPO = "{tipo}")
                    AND TIPO = "{tipo}";"""

        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()
            if tipo == "Simple" and huespedes > habitaciones:
                print('No hay suficientes habitaciones de cama simple para los huespedes')
            elif tipo == "Doble" and huespedes >= habitaciones*2:
                print('No hay suficientes habitaciones de cama doble para los huespedes')
            else:
                if len(rooms) > habitaciones:
                    responseArray = []
                    for room in rooms:
                        res = Room(room[0], room[1], room[2], room[3])
                        responseArray.append(res)
                    return responseArray
                else:
                    print('No hay suficientes habitaciones disponibles')
        except Exception as e:
            raise

    def close(self):
        self.connection.close()


database = DATABASE()
