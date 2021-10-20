import unittest
import pkmodel as pk


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_create(self):
        """
        Tests Protocol creation.
        """
        model = pk.Protocol(1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8)
        self.assertEqual(model.Q_p1, 1.1)
        self.assertEqual(model.V_c, 2.2)
        self.assertEqual(model.V_p1, 3.3)
        self.assertEqual(model.CL, 4.4)
        self.assertEqual(model.X, 5.5)
        self.assertEqual(model.dose_on, 6)
        self.assertEqual(model.dose_off, 7)
        self.assertEqual(model.k_a, 8.8)

