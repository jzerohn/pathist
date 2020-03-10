import unittest
from pathist.common import character

class TestCharacterMethods(unittest.TestCase):

    def test_print(self):
        c = character.Character("Joe")
        self.assertEqual(c.print(), "My name is Joe")

if __name__ == '__main__':
    unittest.main()