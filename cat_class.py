class Cat():
#special method '__init__'
    def __init__(self, name, age, fur, colour, tail):
        self.name = name
        self.age = age
        self.fur = fur
        self.colour = colour
        self.tail = bool(tail)
        self.claws = True

# 5 methods
    def purr(self):
        return 'purr purr purr'

    def eat(self, food):
        if food == "fish" or food == 'chicken':
            return 'purr nom nom nom purr'
        elif food == "meat":
            return 'nom nom nom'
        else:
            return '*pushes away in disgust* MEOW'

    def drink(self):
        return 'lap lap lap *the bowl was emptied*'

    def sleep(self):
        return 'zzzzZZzZZzzzz'

    def pounce(self, object):
        return 'sneaks up on ' + object + ' and pounces on ' + object