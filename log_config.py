import logging
import logging.config
import os

# crear la carpeta de logs(si no existe)
os.makedirs('logs', exist_ok=True)

def config():
    '''
    configuraciones trazas
    '''
    logging.basicConfig(
        level = logging.INFO,
        filename = 'logs/taximetro.log',
        filemode = 'a',
        format = '%(asctime)s - %(levelname)s - %(message)s'
    )