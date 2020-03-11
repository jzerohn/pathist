from pathist.common import utility
from pathist.common.ability import Ability
from pathist.common.abilities_enum import CoreAbility
from pathist.common.character import Character
from pathist.common.armor_class import ArmorClass
import json

def run():

    ac = ArmorClass(10)
    abl = [Ability(CoreAbility.ST, 12),
    Ability(CoreAbility.KO, 12), Ability(CoreAbility.GE, 12),
    Ability(CoreAbility.IN, 12), Ability(CoreAbility.WI, 12),
    Ability(CoreAbility.CH, 12)]

    char = Character(22, abl, ac)

    print(char.toJson())