import unittest
from pathist.common import ability
from pathist.common.abilities_enum import CoreAbility

class TestAttributeMethods(unittest.TestCase):

    # Old test before conversion to string rep
    # def test_attribute_stat_getter(self):
    #     a = ability.Ability(CoreAbility.ST, 19)
    #     self.assertEqual(a.stat, CoreAbility.ST)

    def test_attribute_stat_getter(self):
        a = ability.Ability(CoreAbility.ST, 19)
        self.assertEqual(a.stat, "STR")

    def test_attribute_stat_assertion(self):
        with self.assertRaises(Exception):
            ability.Ability("ST", 19)

    def test_attribute_value_getter(self):
        a = ability.Ability(CoreAbility.ST, 19)
        self.assertEqual(a.value, 19)

    def test_attribute_value_setter(self):
        a = ability.Ability(CoreAbility.ST, 19)
        a.value = 10
        self.assertEqual(a.value, 10)
        self.assertEqual(a.modifier, 0)

    def test_attribute_value_setter_assertion(self):
        a = ability.Ability(CoreAbility.ST, 19)

        with self.assertRaises(TypeError):
            a.value = "1"

        with self.assertRaises(ValueError):
            a.value = -1

    def test_attribute_modifier_getter(self):
        a = ability.Ability(CoreAbility.ST, 19)
        self.assertEqual(a.modifier, 4)    

if __name__ == '__main__':
    unittest.main()