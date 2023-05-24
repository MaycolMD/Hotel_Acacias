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
            host="localhost", user="root", password="", db="hotel_acacias"
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
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}" 
                        OR (R.`FECHA_CHECKIN` <= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        OR (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` >= "{f_out}"))
                        AND TIPO = "{tipo}");"""

        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()
            if tipo == "Uso compartido":
                if rooms[0][0] >= 10 - int(cantidad) + 1:
                    print("No hay disponibilidad")
                    return False
                else:
                    print("Disponible")
                    return True
            elif tipo == "Simple" or tipo == "Doble":
                if rooms[0][0] >= 15 - int(cantidad) + 1:
                    print("No hay disponibilidad")
                    return False
                else:
                    print("Disponible")
                    return True
        except Exception as e:
            raise

    def verificar_disponibilidad_uso_compartido(self, f_in, f_out, cantidad):
        query = f"""SELECT COUNT(ID_HABITACION)
                    FROM INVENTARIO_HABITACION
                    WHERE ID_HABITACION IN
                        (SELECT I.`ID_HABITACION`
                        FROM RESERVAS R CROSS JOIN INVENTARIO_HABITACION I
                        ON R.ID_HABITACION = I.ID_HABITACION
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}" 
                        OR (R.`FECHA_CHECKIN` <= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        OR (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` >= "{f_out}"))
                        AND TIPO = "Uso compartido");"""

        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()

            if rooms[0][0] >= 10 - int(cantidad) + 1:
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
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}" 
                        OR (R.`FECHA_CHECKIN` <= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        OR (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` >= "{f_out}"))
                        AND TIPO = "Simple");"""

        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()

            if rooms[0][0] >= 15 - int(cantidad) + 1:
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
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}" 
                        OR (R.`FECHA_CHECKIN` <= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        OR (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` >= "{f_out}"))
                        AND TIPO = "Doble");"""

        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()

            if rooms[0][0] >= 15 - int(cantidad) + 1:
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
            end_date = datetime.strptime(f_out, '%Y-%d-%m').date()
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
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}" 
                        OR (R.`FECHA_CHECKIN` <= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        OR (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` >= "{f_out}")));"""

        try:
            self.cursor.execute(query)
            park = self.cursor.fetchall()

            if park[0][0] >= 25:
                print("No hay disponibilidad")
                return False
            else:
                print("Disponible")
                return True
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
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}" 
                        OR (R.`FECHA_CHECKIN` <= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        OR (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` >= "{f_out}")
                        AND RE.HORARIO = "{hora}"));"""

        try:
            self.cursor.execute(query)
            mesa = self.cursor.fetchall()

            if mesa[0][0] >= 40 - int(cantidad) + 1:
                print("No hay disponibilidad")
                return False
            else:
                print("Disponible")
                return True
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

            if asiento[0][0] >= 20 - int(cantidad) + 1:
                print("No hay disponibilidad")
                return False
            else:
                print("Disponible")
                return True
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

            return paro_activo
        except Exception as e:
            raise

        # Buscador
    
    def getHabitaciones(self, tipo, f_in, f_out, huespedes, habitaciones):
        if tipo == "Seleccionar tipo":
            query = f"""SELECT
                            I.`TIPO` AS tipo,
                            COUNT(*) AS cantidad,
                            I.`DESCRIPCION` AS descripcion
                        FROM
                            hotel_acacias.inventario_habitacion I
                        WHERE
                            I.`ID_HABITACION` NOT IN (
                                SELECT 
                                    R.`ID_HABITACION`
                                FROM
                                    hotel_acacias.RESERVAS R
                                        CROSS JOIN
                                    hotel_acacias.INVENTARIO_HABITACION IH ON R.ID_HABITACION = IH.ID_HABITACION
                                WHERE
                                    (R.`FECHA_CHECKIN` >= '{f_in}'
                                    AND R.`FECHA_CHECKOUT` <= '{f_out}')
                            )
                        GROUP BY
                            I.`TIPO`,
                            I.`DESCRIPCION`;
                    """
        else:  
            query = f"""SELECT *
                        FROM INVENTARIO_HABITACION
                        WHERE ID_HABITACION NOT IN
                            (SELECT I.`ID_HABITACION`
                            FROM RESERVAS R CROSS JOIN INVENTARIO_HABITACION I
                            ON R.ID_HABITACION = I.ID_HABITACION
                            AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                            AND TIPO = "{tipo}")
                        AND TIPO = "{tipo}";
                    """
            
        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()
            if tipo == "Simple" and huespedes > habitaciones:
                print('No hay suficientes habitaciones de cama simple para los huespedes')
            elif tipo == "Doble" and huespedes > habitaciones*2:
                print('No hay suficientes habitaciones de cama doble para los huespedes')
            else:
                responseArray = []
                if tipo == "Seleccionar tipo":
                    if huespedes >= 2 and huespedes > habitaciones and huespedes <= habitaciones*2:
                        for room in rooms:
                            if room[0] != 'Simple':
                                res = Room(room[0], room[0], room[2], room[1])
                                responseArray.append(res)
                    elif huespedes > habitaciones*2:
                        for room in rooms:
                            if room[0] == 'Uso compartido':
                                res = Room(room[0], room[0], room[2], room[1])
                                responseArray.append(res)
                    else:
                        for room in rooms:
                            res = Room(room[0], room[0], room[2], room[1])
                            responseArray.append(res)
                else: 
                    if len(rooms) > habitaciones:
                        for room in rooms:
                            res = Room(room[0], room[1], room[3], room[2])
                            responseArray.append(res)
                    else:
                        print('No hay suficientes habitaciones disponibles')
                return responseArray        
        except Exception as e:
            raise

    def contar_disponibilidad_habitaciones(self, tipo, f_in, f_out):
        query = f"""SELECT COUNT(`ID_HABITACION`)
                    FROM INVENTARIO_HABITACION
                    WHERE TIPO = "{tipo}" 
                    AND NOT `ID_HABITACION` IN
                        (SELECT I.`ID_HABITACION`
                        FROM RESERVAS R CROSS JOIN INVENTARIO_HABITACION I
                        ON R.ID_HABITACION = I.ID_HABITACION
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}" 
                        OR (R.`FECHA_CHECKIN` <= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        OR (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` >= "{f_out}"))
                        AND TIPO = "{tipo}")"""
        try:
            self.cursor.execute(query)
            rooms = self.cursor.fetchall()
            responsive_item = rooms[0][0]
            print(responsive_item)
            return responsive_item
        except Exception as e:
            raise

    def contar_disponibilidad_parqueadero(self, f_in, f_out):
        query = f"""SELECT COUNT(`ID_PARQUEADERO`)
                    FROM PARQUEADERO
                    WHERE `ID_PARQUEADERO` IN
                        (SELECT P.`ID_PARQUEADERO`
                        FROM RESERVAS R CROSS JOIN PARQUEADERO P
                        ON R.`ID_RESERVA` = P.ID_RESERVA
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}" 
                        OR (R.`FECHA_CHECKIN` <= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        OR (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` >= "{f_out}")))"""
        try:
            self.cursor.execute(query)
            park = self.cursor.fetchall()
            responsive_item = 25 - park[0][0]
            print(responsive_item)
            return responsive_item
        except Exception as e:
            raise

    def contar_disponibilidad_restaurante(self, horario, f_in, f_out):
        query = f"""SELECT COUNT(`ID_MESA`)
                    FROM RESTAURANTE
                    WHERE `ID_MESA` IN
                        (SELECT RE.`ID_MESA`
                        FROM RESERVAS R CROSS JOIN RESTAURANTE RE
                        ON R.`ID_RESERVA` = RE.ID_RESERVA
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}" 
                        OR (R.`FECHA_CHECKIN` <= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        OR (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` >= "{f_out}"))
                        AND RE.`HORARIO` = "{horario}");"""
        
        try:
            self.cursor.execute(query)
            mesa = self.cursor.fetchall()
            responsive_item = 40 - mesa[0][0]
            print(responsive_item)
            return responsive_item
        except Exception as e:
            raise

    def contar_disponibilidad_transporte(self, hora):
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
            responsive_item = 20 - asiento[0][0]
            print(responsive_item)
            return responsive_item
        except Exception as e:
            raise
    
    def verificar_id_habitacion(self, tipo, f_in, f_out):
        query = f"""SELECT MIN(ID_HABITACION)
                    FROM INVENTARIO_HABITACION
                    WHERE TIPO = "{tipo}"
                    AND NOT `ID_HABITACION` IN
                        (SELECT I.`ID_HABITACION`
                        FROM RESERVAS R CROSS JOIN INVENTARIO_HABITACION I
                        ON R.ID_HABITACION = I.ID_HABITACION
                        AND (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}" 
                        OR (R.`FECHA_CHECKIN` <= "{f_in}" AND R.`FECHA_CHECKOUT` <= "{f_out}")
                        OR (R.`FECHA_CHECKIN` >= "{f_in}" AND R.`FECHA_CHECKOUT` >= "{f_out}")));"""

        try:
            self.cursor.execute(query)
            id = self.cursor.fetchall()
            responseArray = []
            guest = {'id':id[0]}
            responseArray.append(guest)
            return guest
        except Exception as e:
            raise
    
    def ingresar_datos_reserva(self, tipo, f_in, f_out, cantidad_habitacion, ID_CLIENTE, ID_HABITACION, NACIONALIDAD, ORIGEN, NOMBRES, APELLIDOS):
        if(not self.verificar_disponibilidad_habitacion(tipo, f_in, f_out, cantidad_habitacion)):
            print("No hay habitaciones disponibles")
            return
        
        if(self.verificar_disponibilidad_paro_armado(f_in, f_out)):
            print("Hay paro armado")
            return    

        query = f"""INSERT INTO RESERVAS
                    (ID_CLIENTE, ID_HABITACION, NACIONALIDAD, ORIGEN, NOMBRES, APELLIDOS, FECHA_CHECKIN, FECHA_CHECKOUT)
                    VALUES
                    ("{ID_CLIENTE}", "{ID_HABITACION}", "{NACIONALIDAD}", "{ORIGEN}", "{NOMBRES}", "{APELLIDOS}", "{f_in}", "{f_out}");"""
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            raise

        query2 = f"""SELECT LAST_INSERT_ID(`ID_RESERVA`)
                     FROM RESERVAS
                     WHERE `NOMBRES` = "{NOMBRES}";"""
        
        try:
            self.cursor.execute(query2)
            id_r = self.cursor.fetchall()
            id_reserva = id_r[0][0]
        except Exception as e:
            raise


    def ingresar_datos_parqueadero(self, id_reserva, f_in, f_out, check):
        if(not check):
            return
        
        if(not self.verificar_disponibilidad_parqueadero(f_in, f_out)):
            query2 = f"""DELETE FROM RESERVAS
                         WHERE `ID_RESERVA` = {id_reserva};"""
            try:
                self.cursor.execute(query2)
                self.connection.commit()
            except Exception as e:
                raise

            print("No hay parqueaderos disponibles")
            return
        
        query = f"""INSERT INTO PARQUEADERO
                    (ID_RESERVA)
                    VALUES
                    ({id_reserva});"""
        
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            raise

    def ingresar_datos_restaurante(self, id_reserva, horario, f_in, f_out, cantidad, check):
        if(not check):
            return
        
        if(not self.verificar_disponibilidad_restaurante(horario, f_in, f_out, cantidad)):
            query2 = f"""DELETE FROM RESERVAS
                         WHERE `ID_RESERVA` = {id_reserva};"""
            try:
                self.cursor.execute(query2)
                self.connection.commit()
            except Exception as e:
                raise

            query3 = f"""DELETE FROM PARQUEADERO
                         WHERE `ID_RESERVA` = {id_reserva};"""
            try:
                self.cursor.execute(query3)
                self.connection.commit()
            except Exception as e:
                raise

            print("No hay asientos en el restaurante disponibles")
            return
        
        query = f"""INSERT INTO RESTAURANTE
                    (HORARIO, ID_RESERVA)
                    VALUES
                    ({horario},{id_reserva});"""
        
        try:
            for i in range(cantidad):
                self.cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            raise

    def ingresar_datos_transporte(self, id_reserva, horario, cantidad, check):
        if(not check):
            return
        
        if(not self.verificar_disponibilidad_transporte(horario, cantidad)):
            query2 = f"""DELETE FROM RESERVAS
                         WHERE `ID_RESERVA` = {id_reserva};"""
            try:
                self.cursor.execute(query2)
                self.connection.commit()
            except Exception as e:
                raise

            query3 = f"""DELETE FROM PARQUEADERO
                         WHERE `ID_RESERVA` = {id_reserva};"""
            try:
                self.cursor.execute(query3)
                self.connection.commit()
            except Exception as e:
                raise

            query4 = f"""DELETE FROM RESTAURANTE
                         WHERE `ID_RESERVA` = {id_reserva};"""
            try:
                self.cursor.execute(query4)
                self.connection.commit()
            except Exception as e:
                raise

            print("No hay asientos en el bus disponibles")
            return
        
        query = f"""INSERT INTO TRANSPORTE
                    (HORARIO, ID_RESERVA)
                    VALUES
                    ({horario},{id_reserva});"""
        
        try:
            for i in range(cantidad):
                self.cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            raise

    def close(self):
        self.connection.close()


database = DATABASE()