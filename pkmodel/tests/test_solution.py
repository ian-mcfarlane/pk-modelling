import unittest
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
        model = pk.ThreeCompartmentModel(protocol)
        solution = pk.Solution(model)
        self.assertEqual(solution.model, model)

