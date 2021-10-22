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
        protocol = pk.Protocol("test", 3, 1.1, 2.2, 3.3, 4.4, 5.5, 0, 7, 8, False)
        self.assertEqual(protocol.label, "test")
        self.assertEqual(protocol.comps, 3)
        self.assertEqual(protocol.Q_p1, 1.1)
        self.assertEqual(protocol.V_c, 2.2)
        self.assertEqual(protocol.V_p1, 3.3)
        self.assertEqual(protocol.CL, 4.4)
        self.assertEqual(protocol.X, 5.5)
        self.assertEqual(protocol.dose_on, 6)
        self.assertEqual(protocol.dose_off, 7)
        self.assertEqual(protocol.k_a, 8)
        self.assertEqual(protocol.graph_preview, False)

        # Test protocol creation without optional arguments
        protocol = pk.Protocol("test", 3, 1.1, 2.2, 3.3, 4.4, 5.5, 6)
        self.assertEqual(protocol.dose_off, 0)
        self.assertEqual(protocol.k_a, 0)
        self.assertEqual(protocol.graph_preview, False)

        # Test protocol raises Value Errors for invalid inputs
        with self.assertRaises(ValueError):
            protocol = pk.Protocol("test", 200, 1.1, 2.2, 3.3, 4.4, 5.5, 6)
        with self.assertRaises(ValueError):
            protocol = pk.Protocol("test", 2, -1, 2.2, 3.3, 4.4, 5.5, 6)
        with self.assertRaises(ValueError):
            protocol = pk.Protocol("test", 2, 1.1, -2.2, 3.3, 4.4, 5.5, 6)
        with self.assertRaises(ValueError):
            protocol = pk.Protocol("test", 2, 1.1, 2.2, -3.3, 4.4, 5.5, 6)
        with self.assertRaises(ValueError):
            protocol = pk.Protocol("test", 2, 1.1, 2.2, 3.3, -4.4, 5.5, 6)
        with self.assertRaises(ValueError):
            protocol = pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, -5.5, 6)
        with self.assertRaises(ValueError):
            protocol = pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5.5, -6)
        with self.assertRaises(ValueError):
            protocol = pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 6, -7, 8)
        with self.assertRaises(ValueError):
            protocol = pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, -8)
        with self.assertRaises(ValueError):
            protocol = pk.Protocol("test", "hello", 1.1, 2.2, 3.3, 4.4, 5.5, 6)

    def test__eq__(self):
        """
        Tests Protocol equality function.
        """
        protocol1 = pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False)
        self.assertEqual(protocol1, protocol1)

        protocols = [
            pk.Protocol("test", 3, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False),
            pk.Protocol("test", 2, 1, 2.2, 3.3, 4.4, 5.5, 6, 7, 8, False),
            pk.Protocol("test", 2, 1.1, 2, 3.3, 4.4, 5.5, 6, 7, 8, False),
            pk.Protocol("test", 2, 1.1, 2.2, 3, 4.4, 5.5, 6, 7, 8, False),
            pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4, 5.5, 6, 7, 8, False),
            pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5, 6, 7, 8, False),
            pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 0, 7, 8, False),
            pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 0, 8, False),
            pk.Protocol("test", 2, 1.1, 2.2, 3.3, 4.4, 5.5, 6, 7, 0, False)
        ]
        for other_protocol in protocols:
            self.assertNotEqual(protocol1, other_protocol)

