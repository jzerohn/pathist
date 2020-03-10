import unittest
from pathist.common import utility

class TestUtilityFunctinos(unittest.TestCase):

    def test_ac_size_modifier(self):
        self.assertEqual(utility.ac_size_modifier("Large"), -1)
        self.assertIsNone(utility.ac_size_modifier("ego"))
        with self.assertRaises(ValueError):
            utility.ac_size_modifier(42)

if __name__ == '__main__':
    unittest.main()