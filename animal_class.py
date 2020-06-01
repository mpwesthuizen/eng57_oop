
class Animal():
    def __init__(self, species_argument, tail, colour, name, limbs=4):
        self. species_param = species_argument
        self.limbs = limbs
        self.tail = bool(tail)
        self.colour = colour
        self.name = name

    def sleep(self):
        return 'zzzzZZzZZzzzz'

    def chase(self, object):
        return 'runs after' + object

    def drink(self):
        return 'lap lap lap *the bowl was emptied*'