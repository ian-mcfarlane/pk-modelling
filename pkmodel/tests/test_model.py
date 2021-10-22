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

    def test__eq__(self):
        """
        Tests model equality function.
        """
        model1 = pk.TwoCompartmentModel(pk.Protocol("model1", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False))
        self.assertEqual(model1, model1)
        model2 = pk.TwoCompartmentModel(pk.Protocol("model2", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False))
        self.assertNotEqual(model1, model2)


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

    def test__eq__(self):
        """
        Tests model equality function.
        """
        model1 = pk.ThreeCompartmentModel(pk.Protocol("model1", 3, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False))
        self.assertEqual(model1, model1)
        model2 = pk.ThreeCompartmentModel(pk.Protocol("model2", 3, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False))
        self.assertNotEqual(model1, model2)
