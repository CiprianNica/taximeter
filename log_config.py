import logging
import logging.config
import os
from datetime import datetime


def config():
    '''
    configuraciones trazabilidad archivo y consola
    '''
    # crear la carpeta de logs(si no existe)
    os.makedirs('logs', exist_ok=True)
    logs_archivo = f"logs/taximetro_{datetime.now().strftime('%d%m%Y')}.log"

    logging.basicConfig(
        level = logging.INFO,
        format = '%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(logs_archivo, mode='a', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )