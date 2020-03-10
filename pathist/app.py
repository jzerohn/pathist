from pathist.common import utility
from pathist.common import armor_class

def run():
    print(utility.ac_size_modifier("Large"))

    ac = armor_class.ArmorClass(6, 3, 2)

    print("AC: {}, Touch: {}, FF: {}".format(ac.ac, ac.touch, ac.flat_footed))

    ac.update_armor(6, 3, 2, natural_armor=4, size_bonus=2)

    print("AC: {}, Touch: {}, FF: {}".format(ac.ac, ac.touch, ac.flat_footed))