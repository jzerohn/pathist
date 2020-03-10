from math import floor
from pathist.common.abilities_enum import CoreAbility

class Ability:

    def __init__ (self, stat, value):
        if not isinstance(stat, CoreAbility): 
            raise TypeError("stat must be from Enum CoreAbility")

        self._modifier = None
        self._stat = stat        
        self.value = value

    @property
    def stat(self):
        return self._stat

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError('value must be of type integer')
        if new_value < 1:
            raise ValueError('value must be greater than 0')

        self._value = new_value
        self._modifier = self.__compute_modifier(new_value)

    @property
    def modifier(self):
        return self._modifier

    def __compute_modifier(self, value):
        return floor(value / 2 - 5)