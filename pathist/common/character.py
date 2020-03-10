class Character:

    def __init__ (self, name):
        self.name = name

    def print(self):
        return "My name is {}".format(self.name)