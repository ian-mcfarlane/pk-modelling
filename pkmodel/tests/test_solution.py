import unittest
import matplotlib
import pkmodel as pk


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests Solution creation.
        """
        protocol = pk.Protocol("test", 3, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False)
        models = [pk.ThreeCompartmentModel(protocol)]
        solution = pk.Solution(models, True)
        self.assertEqual(solution.models[0], models[0])

    def test_graph(self):
        """
        Tests Solution graph method.
        """
        models = [
            pk.TwoCompartmentModel(pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 0, 7, 8, False)),
            pk.TwoCompartmentModel(pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 0, 8, False)),
            pk.TwoCompartmentModel(pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False)),
            pk.ThreeCompartmentModel(pk.Protocol("test", 3, 1.1, 2.2, 3.3, 4.4, 5.5, 0, 7, 8, False)),
            pk.ThreeCompartmentModel(pk.Protocol("test", 3, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 0, 8, False)),
            pk.ThreeCompartmentModel(pk.Protocol("test", 3, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False)),
        ]
        matplotlib.use("Agg")
        solution = pk.Solution(models, False)
        solution.graph()
