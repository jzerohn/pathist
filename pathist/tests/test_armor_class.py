import unittest
from pathist.common.armor_class import ArmorClass

class TestArmorClassMethods(unittest.TestCase):

    def test_armor_class_ac_getter(self):
        armclass = ArmorClass(7, natural_armor=3, dexterity_modifier=2)
        self.assertEqual(armclass.ac, 22)
        self.assertEqual(armclass.flat_footed, 20)
        self.assertEqual(armclass.touch, 12)

    def test_armor_class_ac_update(self):
        armclass = ArmorClass()
        self.assertEqual(armclass.ac, 10)
        self.assertEqual(armclass.ac, armclass.touch)
        self.assertEqual(armclass.ac, armclass.flat_footed)
        armclass.update_armor(7, natural_armor=3, dexterity_modifier=2)
        self.assertEqual(armclass.ac, 22)
        self.assertEqual(armclass.flat_footed, 20)
        self.assertEqual(armclass.touch, 12)

    def test_armor_class_value_error(self):
        with self.assertRaises(ValueError):
            ArmorClass(-1)


if __name__ == '__main__':
    unittest.main()