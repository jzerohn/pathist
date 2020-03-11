import random
import string
import json
from pathist.common.armor_class import ArmorClass
from pathist.common.ability import Ability
from pathist.common import utility

class Character:

    def __init__ (self, hp, abilities, ac, id = None, name = None):

        if not isinstance(ac, ArmorClass):
            raise ValueError('ac must be of ArmorClass')

        if not isinstance(abilities, list):
            raise TypeError('abilities must be supplied as a list')

        ability_enums = []
        ability_dict = {}

        for blty in abilities:
            ability_enums.append(blty.stat)
            ability_dict[blty.stat] = blty
            if not isinstance(blty, Ability):
                raise TypeError('{} is not of class Ability'.format(blty))

        if (len(set(ability_enums)) != 6):
            raise ValueError('please supply six unique abilities')

        self.hp = hp
        self._ac = ac
        self._abilities = ability_dict

        if not id:
            self._id = self.__random_id(12)
        elif len(id) == 12:
            self._id = id
        else:
            raise ValueError('supplied invalid id')        

        if not name:
            self._name = self._id
        else:
            self._name = name        

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, new_value):
        self._hp = new_value

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def ac(self):
        return self._ac

    @property
    def abilites(self):
        return self._abilities

    def __random_id(self, size):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(size))

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)