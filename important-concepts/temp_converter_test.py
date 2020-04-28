import unittest
from temp_converter import cels_to_fahr, fahr_to_cels

class TestTempConverter(unittest.TestCase):
    def test_ctf(self):
        # Tests standard inputs
        self.assertAlmostEqual(cels_to_fahr(0), 32.0)
        self.assertAlmostEqual(cels_to_fahr(20), 20 * 9 / 5 + 32)
        self.assertAlmostEqual(cels_to_fahr(70), 70 * 9 / 5 + 32)

    def test_values(self):
        # Tests for impossibly cold temperatures
        self.assertRaises(ValueError, cels_to_fahr, -273.16)

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, cels_to_fahr, 3+5j)
        self.assertRaises(TypeError, cels_to_fahr, True)
        self.assertRaises(TypeError, cels_to_fahr, "34")

    def test_ftc(self):
        # Tests for standard inputs
        self.assertAlmostEqual(fahr_to_cels(32.0), 0)
        self.assertAlmostEqual(fahr_to_cels(32.0), 32 / 9 * 5 - 32 / 9 * 5)
        self.assertAlmostEqual(fahr_to_cels(1.99), 1.99 / 9 * 5 - 32 / 9 * 5)
        self.assertAlmostEqual(fahr_to_cels(14.3), 14.3 / 9 * 5 - 32 / 9 * 5)



