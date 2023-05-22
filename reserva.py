import datetime

class Reserva:
    def __init__(self, id_reserva, id_cliente, id_habitacion, nacionalidad, origen, nombres, apellidos, fecha_checkin, fecha_checkout, estado):
        self.ID_RESERVA = id_reserva
        self.ID_CLIENTE = id_cliente
        self.ID_HABITACION = id_habitacion
        self.NACIONALIDAD = nacionalidad
        self.ORIGEN = origen
        self.NOMBRES = nombres
        self.APELLIDOS = apellidos
        self.FECHA_CHECKIN = fecha_checkin.strftime('%Y-%m-%d')
        self.FECHA_CHECKOUT = fecha_checkout.strftime('%Y-%m-%d')
        self.ESTADO = estado