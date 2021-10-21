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
        # Test protocol creation with expected parameters
        protocol = pk.Protocol(3, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, True)
        self.assertEqual(protocol.comps, 3)
        self.assertEqual(protocol.Q_p1, 1.1)
        self.assertEqual(protocol.V_c, 2.2)
        self.assertEqual(protocol.V_p1, 3.3)
        self.assertEqual(protocol.CL, 4.4)
        self.assertEqual(protocol.X, 5.5)
        self.assertEqual(protocol.dose_on, 6)
        self.assertEqual(protocol.dose_off, 7)
        self.assertEqual(protocol.k_a, 8.8)
        self.assertEqual(protocol.graph_preview, True)

        # Test protocol creation without optional arguments
        protocol = pk.Protocol(3, 1.1, 2.2, 3.3, 4.4, 5.5, 6)
        self.assertEqual(protocol.dose_off, 0)
        self.assertEqual(protocol.k_a, 0)
        self.assertEqual(protocol.graph_preview, False)

        # Test protocol raises exceptions for invalid inputs
        with self.assertRaises(AssertionError):
            protocol = pk.Protocol(200, 1.1, 2.2, 3.3, 4.4, 5.5, 6)
        with self.assertRaises(AssertionError):
            protocol = pk.Protocol(2, -1, 2.2, 3.3, 4.4, 5.5, 6)
        with self.assertRaises(AssertionError):
            protocol = pk.Protocol(2, 1.1, -2.2, 3.3, 4.4, 5.5, 6)
        with self.assertRaises(AssertionError):
            protocol = pk.Protocol(2, 1.1, 2.2, -3.3, 4.4, 5.5, 6)
        with self.assertRaises(AssertionError):
            protocol = pk.Protocol(2, 1.1, 2.2, 3.3, -4.4, 5.5, 6)
        with self.assertRaises(ValueError):
            protocol = pk.Protocol("hello", 1.1, 2.2, 3.3, -4.4, 5.5, 6)

    def test__eq__(self):
        """
        Tests Protocol equality function.
        """
        protocol1 = pk.Protocol(2, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False)
        protocol2 = pk.Protocol(3, 8.8, 7.7, 6.6, 5.5, 4.4, 3, 2, 1, True)
        self.assertEqual(protocol1, protocol1)
        self.assertNotEqual(protocol1, protocol2)

