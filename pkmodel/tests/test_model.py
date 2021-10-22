import unittest
import pkmodel as pk


class TwoCompartmentModelTest(unittest.TestCase):
    """
    Tests the :class:`TwoCompartmentModel` class.
    """
    def test_create(self):
        """
        Tests TwoCompartmentModel creation.
        """
        protocol = pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False)
        model = pk.TwoCompartmentModel(protocol)
        self.assertEqual(model.protocol, protocol)


class ThreeCompartmentModelTest(unittest.TestCase):
    """
    Tests the :class:`ThreeCompartmentModel` class.
    """
    def test_create(self):
        """
        Tests ThreeCompartmentModel creation.
        """
        protocol = pk.Protocol("test", 3, 1.1, 2.2, 3.3, 4.4, 5.5, 0, 7, 8, False)
        model = pk.ThreeCompartmentModel(protocol)
        self.assertEqual(model.protocol, protocol)
