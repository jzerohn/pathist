import random
import string

class Character:

    def __init__ (self, name = None):
        self._id = self.__random_id(12)

        if not name:
            self._name = self._id
        else:
            self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def __random_id(self, size):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(size))