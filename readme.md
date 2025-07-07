
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
├── tests/                
│   └── test_negocio.py   # Archivos de test unitario
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
La aplicación registra automáticamente toda la actividad relevante (inicio, cambios de estado, cálculos, finalización de trayectos) tanto en consola como en un archivo de texto plano.

  - Los archivos de log se guardan en la carpeta logs/.
  - Cada día se genera un nuevo archivo con el formato:
    ```logs/taximetro_DDMMYYYY.log``` (por ejemplo: ```taximetro_26072025.log```)
  - La configuración está centralizada en ```log_config.py```.


### 5. gitignore

El proyecto incluye un .gitignore que excluye:

  - el entorno virtual venv/.
  - archivos temporales de Python.
  - carpetas y archivos de configuraciones de editores (VS Code, PyCharm).
  - archivos de sistema y compilación.

### 6. Pruebas
El proyecto incluye pruebas unitarias para verificar el correcto funcionamiento del taxímetro. Las pruebas están implementadas con unittest y usan unittest.mock para simular el tiempo transcurrido, permitiendo comprobar con precisión la acumulación de tarifas en distintos estados (parado y movimiento).
Estas pruebas aseguran que la lógica del cálculo de tarifas y el flujo del trayecto (inicio, cambio de estado, finalización) se comportan como se espera.

Para ejecutarlas:
```
python tests/test_negocio.py
```


### Mejoras futuras (opcional)
  - Implementar rotación automática de logs para evitar archivos demasiado grandes.
  - Añadir persistencia de datos en base de datos o archivo.
  - Mejorar la interfaz con más detalles y controles.