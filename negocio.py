import time
import logging

TARIFA_MOVIMIENTO = 0.05  # €/s
TARIFA_PARADO = 0.02      # €/s

class Taximetro:
    def __init__(self):
        self.inicio = None
        self.ultimo_cambio = None
        self.estado_actual = None  # "movimiento" o "parado"
        self.acumulado = 0.0
        logging.info("Taximetro inicializado")

    def iniciar_trayecto(self):
        self.inicio = time.time()
        self.ultimo_cambio = self.inicio
        self.estado_actual = "parado"
        self.acumulado = 0.0
        logging.info("Trayecto iniciado")

    def cambiar_estado(self, nuevo_estado):
        logging.info(f"Cambio de estado: {self.estado_actual} -> {nuevo_estado}")
        ahora = time.time()
        self._acumular_tarifa(ahora)
        self.estado_actual = nuevo_estado
        self.ultimo_cambio = ahora
        

    def finalizar_trayecto(self):
        ahora = time.time()
        self._acumular_tarifa(ahora)
        total = round(self.acumulado, 2)
        logging.info(f"Trayecto finalizado - Precio total: {total}€")
        self._reset()
        return total

    def _acumular_tarifa(self, ahora):
        tiempo = ahora - self.ultimo_cambio
        if self.estado_actual == "movimiento":
            self.acumulado += tiempo * TARIFA_MOVIMIENTO
        elif self.estado_actual == "parado":
            self.acumulado += tiempo * TARIFA_PARADO
        logging.info(f"Estado: {self.estado_actual} - {tiempo:.2f}s - Coste: {self.acumulado:.2f}€ ")

    def _reset(self):
        self.inicio = None
        self.ultimo_cambio = None
        self.estado_actual = None
        logging.info("Taximetro reiniciado")
