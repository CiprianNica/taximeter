import customtkinter as ctk
import tkinter.messagebox as messagebox
import time
from negocio import Taximetro

# Configuramos tema y colores globales (opcional)
ctk.set_appearance_mode("light")  # "dark", "light", "system"
ctk.set_default_color_theme("blue")  # azul, verde, dark-blue


def crear_boton(parent, texto, comando, estado="normal", color="#007BFF"):
    '''configura boton'''
    
    colores_hover = {
        "#007BFF": "#0056b3",  # azul
        "#28a745": "#1e7e34",  # verde
        "#ffc107": "#d39e00",  # amarillo
        "#dc3545": "#a71d2a",  # rojo
    }
    return ctk.CTkButton(
        parent,
        text=texto,
        command=comando,
        state=estado,
        font=("Arial", 16, "bold"),
        fg_color=color,
        hover_color=colores_hover.get(color, "#0056b3"),
        width=220,
        height=50
    )


class TaximetroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxímetro Digital")
        self.root.geometry("450x350")

        self.taximetro = Taximetro()
        self.en_trayecto = False

        self.mostrar_bienvenida_personalizada()
        

        self.label_estado = ctk.CTkLabel(root, text="Estado: Esperando...", font=("Arial", 16))
        self.label_estado.pack(pady=10)

        self.label_total = ctk.CTkLabel(root, text="Total del trayecto: €0.00", font=("Arial", 12))
        self.label_total.pack(pady=5)

        self.btn_inicio = crear_boton(root, "Iniciar Trayecto", self.iniciar_trayecto)
        self.btn_inicio.pack(pady=5)

        self.btn_movimiento = crear_boton(root, "Cambio a Movimiento", lambda: self.cambiar_estado("movimiento"), estado="disabled")
        self.btn_movimiento.pack(pady=5)

        self.btn_parado = crear_boton(root, "Cambio a Parado", lambda: self.cambiar_estado("parado"), estado="disabled")
        self.btn_parado.pack(pady=5)

        self.btn_fin = crear_boton(self.root, "Finalizar Trayecto", self.finalizar_trayecto, estado="disabled")
        self.btn_fin.pack(pady=5)

        self.label_tiempo = ctk.CTkLabel(root, text="", font=("Arial", 12))
        self.label_tiempo.pack(pady=5)
    
    """ def ventana_personalizada(self, titulo, mensaje, es_bienvenida = False):
        ventana = ctk.CTkToplevel(self.root)
        ventana.title(titulo)
        ventana.geometry("500x350")
        ventana.resizable(False, False)

        label = ctk.CTkLabel(ventana, text=mensaje, font=("Arial", 16), wraplength=420, justify="left")
        label.pack(pady=20, padx=20)

        boton_ok = ctk.CTkButton(ventana, text="OK", command=ventana.destroy, width=120, font=('Arial', 14))
        boton_ok.pack(pady=10)

        ventana.transient(self.root)  # aparece encima de la ventana principal
        ventana.grab_set()   # bloquea la ventana principal hasta cerrar esta """
        
    def mostrar_bienvenida_personalizada(self):
        ventana = ctk.CTkToplevel(self.root)
        ventana.title("Bienvenida")
        ventana.geometry("450x480")
        ventana.resizable(True, True)

        mensaje = (
            "🟡 para comenzar presiona:\n\n"
            "\tINICIAR\n\n"
            "🔄 usa los botones para registrar el estado:\n\n"
            "\tMOVIMIENTO\n"
            "\tPARADO\n\n"
            "⛔ finaliza el trayecto cuando termines:\n"
            "\tFINALIZAR\n\n"
            "\n💰 TARIFAS:\n\n"
            "\tMovimiento: €0.05/s\n"
            "\tParado: €0.02/s"
        )

        titulo = ctk.CTkLabel(ventana, text="¡Bienvenido al Taxímetro Digital!", font=("Arial", 18, "bold"), text_color="#003366")
        titulo.pack(pady=(15, 10))

        texto = ctk.CTkLabel(ventana, text=mensaje, font=("Arial", 16), justify="left", wraplength=420)
        texto.pack(padx=20, pady=10)

        boton_ok = crear_boton(ventana, 'OK', ventana.destroy)
        boton_ok.pack(pady=15)
        
    def iniciar_trayecto(self):
        self.taximetro.iniciar_trayecto()
        self.en_trayecto = True
        self.label_estado.configure(text="Estado: Parado")
        self.label_total.configure(text="Total del trayecto: €0.00")
        self.toggle_botones(True)
        self.actualizar_tiempo()

    def cambiar_estado(self, nuevo_estado):
        self.taximetro.cambiar_estado(nuevo_estado)
        self.label_estado.configure(text=f"Estado: {nuevo_estado.capitalize()}")

    def finalizar_trayecto(self):
        total = self.taximetro.finalizar_trayecto()
        self.label_total.configure(text=f"Total del trayecto: €{total}")
        self.label_estado.configure(text="Estado: Finalizado")
        messagebox.showinfo("Resumen", f"Trayecto finalizado.\n\nTotal a pagar: €{total}")
        self.toggle_botones(False)
        self.en_trayecto = False

    def toggle_botones(self, activo):
        estado = "normal" if activo else "disabled"
        self.btn_movimiento.configure(state=estado)
        self.btn_parado.configure(state=estado)
        self.btn_fin.configure(state=estado)
        self.btn_inicio.configure(state="disabled" if activo else "normal")

    def actualizar_tiempo(self):
        if self.en_trayecto and self.taximetro.inicio:
            segundos = int(time.time() - self.taximetro.inicio)
            self.label_tiempo.configure(text=f"Tiempo transcurrido: {segundos}s")
            self.root.after(1000, self.actualizar_tiempo)


if __name__ == "__main__":
    root = ctk.CTk()
    app = TaximetroApp(root)
    root.mainloop()
