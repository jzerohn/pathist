import unittest
from pathist.common import character

class TestCharacterMethods(unittest.TestCase):

    def test_id(self):
        c = character.Character()
        self.assertEqual(len(c.id), 12)
        self.assertIsInstance(c.id, str)

    def test_name(self):
        c = character.Character("Joe")
        self.assertEqual(c.name, "Joe")

if __name__ == '__main__':
    unittest.main()