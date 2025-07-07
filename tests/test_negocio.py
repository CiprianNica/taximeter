import unittest, sys, os
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from negocio import Taximetro

class TestTaximetro(unittest.TestCase):

    @patch("negocio.time")
    def test_inicio_trayecto(self, mock_time):
        mock_time.time.return_value = 1000
        taxi = Taximetro()
        taxi.iniciar_trayecto()
        
        self.assertEqual(taxi.estado_actual, "parado")
        self.assertEqual(taxi.inicio, 1000)
        self.assertEqual(taxi.ultimo_cambio, 1000)
        self.assertEqual(taxi.acumulado, 0.0)

    @patch("negocio.time")
    def test_acumula_parado(self, mock_time):
        taxi = Taximetro()
        mock_time.time.side_effect = [1000, 1010]  # inicio, cambio

        taxi.iniciar_trayecto()          # estado = "parado"
        taxi.cambiar_estado("movimiento")  # 10s parado

        # 10s * 0.02 €/s = 0.20 €
        self.assertAlmostEqual(taxi.acumulado, 0.20, places=2)

    @patch("negocio.time")
    def test_acumula_movimiento_y_finaliza(self, mock_time):
        taxi = Taximetro()
        mock_time.time.side_effect = [
            1000,      # iniciar_trayecto
            1005,      # cambiar a movimiento (5s parado)
            1015,      # finalizar_trayecto (10s movimiento)
        ]

        taxi.iniciar_trayecto()                # estado = "parado"
        taxi.cambiar_estado("movimiento")      # estado cambia
        total = taxi.finalizar_trayecto()

        # 5s parado (0.02) + 10s movimiento (0.05) = 0.10 + 0.50 = 0.60 €
        self.assertAlmostEqual(total, 0.60, places=2)

if __name__ == "__main__":
    unittest.main()
