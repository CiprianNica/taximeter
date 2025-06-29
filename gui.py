import tkinter as tk
from tkinter import messagebox
import time
from negocio import Taximetro

class TaximetroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxímetro Digital")
        self.root.geometry("400x300")

        self.taximetro = Taximetro()
        self.en_trayecto = False

        self.mostrar_bienvenida()

        self.label_estado = tk.Label(root, text="Estado: Esperando...", font=("Arial", 16))
        self.label_estado.pack(pady=10)

        self.label_total = tk.Label(root, text="Total del trayecto: €0.00", font=("Arial", 12))
        self.label_total.pack(pady=5)

        self.btn_inicio = tk.Button(root, text="Iniciar Trayecto", command=self.iniciar_trayecto)
        self.btn_inicio.pack(pady=5)

        self.btn_movimiento = tk.Button(root, text="Cambio a Movimiento", command=lambda: self.cambiar_estado("movimiento"), state="disabled")
        self.btn_movimiento.pack(pady=5)

        self.btn_parado = tk.Button(root, text="Cambio a Parado", command=lambda: self.cambiar_estado("parado"), state="disabled")
        self.btn_parado.pack(pady=5)

        self.btn_fin = tk.Button(root, text="Finalizar Trayecto", command=self.finalizar_trayecto, state="disabled")
        self.btn_fin.pack(pady=5)

        self.label_tiempo = tk.Label(root, text="", font=("Arial", 10))
        self.label_tiempo.pack(pady=5)

    def mostrar_bienvenida(self):
        mensaje = (
            "¡Bienvenido al Taxímetro Digital!\n\n"
            "- Presiona 'Iniciar Trayecto' para comenzar.\n"
            "- Usa los botones para registrar el estado.\n"
            "- Finaliza el trayecto cuando termines.\n\n"
            "Tarifas:\n"
            "- Movimiento: €0.05/s\n"
            "- Parado: €0.02/s"
        )
        messagebox.showinfo("Bienvenida", mensaje)

    def iniciar_trayecto(self):
        self.taximetro.iniciar_trayecto()
        self.en_trayecto = True
        self.label_estado.config(text="Estado: Parado")
        self.label_total.config(text="Total del trayecto: €0.00")
        self.toggle_botones(True)
        self.actualizar_tiempo()

    def cambiar_estado(self, nuevo_estado):
        self.taximetro.cambiar_estado(nuevo_estado)
        self.label_estado.config(text=f"Estado: {nuevo_estado.capitalize()}")

    def finalizar_trayecto(self):
        total = self.taximetro.finalizar_trayecto()
        self.label_total.config(text=f"Total del trayecto: €{total}")
        self.label_estado.config(text="Estado: Finalizado")
        messagebox.showinfo("Resumen", f"Trayecto finalizado.\n\nTotal a pagar: €{total}")
        self.toggle_botones(False)
        self.en_trayecto = False

    def toggle_botones(self, activo):
        estado = "normal" if activo else "disabled"
        self.btn_movimiento.config(state=estado)
        self.btn_parado.config(state=estado)
        self.btn_fin.config(state=estado)
        self.btn_inicio.config(state="disabled" if activo else "normal")

    def actualizar_tiempo(self):
        if self.en_trayecto and self.taximetro.inicio:
            segundos = int(time.time() - self.taximetro.inicio)
            self.label_tiempo.config(text=f"Tiempo transcurrido: {segundos}s")
            self.root.after(1000, self.actualizar_tiempo)
