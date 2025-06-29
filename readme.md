
# Proyecto Taxímetro en Python

## Descripción

Este proyecto simula un taxímetro que permite:

- Iniciar y finalizar trayectos.
- Calcular la tarifa acumulada según el estado del taxi:
  - Parado: 0.02 €/segundo.
  - En movimiento: 0.05 €/segundo.
- Cambiar el estado entre parado y en movimiento durante el trayecto.
- Visualizar la tarifa total al finalizar.
- Iniciar nuevos trayectos sin cerrar la aplicación.
- Registrar toda la actividad con trazabilidad (logs) tanto en consola como en archivo.

La interfaz gráfica está implementada con `tkinter`, y la lógica de negocio está separada para facilitar el mantenimiento.

---

## Estructura del proyecto
```
taximetro/
├── logs/                 # Archivos de logs generados en ejecución
│   └── taximetro.log
├── venv/                 # Entorno virtual (no incluido en control de versiones)
├── negocio.py            # Lógica del taxímetro (negocio)
├── gui.py                # Interfaz gráfica
├── main.py               # Punto de entrada para ejecutar la aplicación
├── log_config.py         # Configuración centralizada del logging
├── requirements.txt      # Dependencias (actualmente vacío)
├── .gitignore            # Archivos y carpetas ignorados en Git
└── README.md             # Este archivo
```
## Configuración y uso

### 1. Crear y activar entorno virtual(en bash)

```
python3 -m venv venv

source venv/bin/activate   # para MacOS/Linux
venv\Scripts\activate      # para Windows

deactivate                 # desactivar
```

### 2. Instalar dependencias (si agregas alguna)
pip install -r requirements.txt

### 3. Ejecutar la aplicacion
```
python3 main.py       # la interfaz gráfica se abrirá y mostrará instrucciones para operar el taxímetro.
```

### 4. Trazabilidad (logging)

  - Todos los eventos importantes (inicio, cambios de estado, cálculos, finalización) se registran automáticamente.
  - Los logs se guardan en logs/taximetro.log.
  - Los logs también se muestran en consola para facilitar seguimiento en tiempo real.
  - La configuración de logging está centralizada en log_config.py.

### 5. gitignore

El proyecto incluye un .gitignore que excluye:

  - el entorno virtual venv/.
  - archivos temporales de Python.
  - carpetas y archivos de configuraciones de editores (VS Code, PyCharm).
  - archivos de sistema y compilación.


### Mejoras futuras (opcional)
  - Implementar rotación automática de logs para evitar archivos demasiado grandes.
  - Añadir persistencia de datos en base de datos o archivo.
  - Mejorar la interfaz con más detalles y controles.
  - Añadir pruebas unitarias para la lógica de negocio.