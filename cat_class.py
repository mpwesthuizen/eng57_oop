from animal_class import *

class Cat(Animal):
#special method '__init__'
#super() inherits __init__(self,parameters) from the parent class 'animals'.
    def __init__(self, age=0):
        super().__init__(self, 'Cartoon alley cat', True, "Black and White", "Sylvester")
        self.age = age

    def purr(self):
        return 'purr purr purr'

    def eat(self, food):
        if food == "fish" or food == 'mouse':
            return 'purr nom nom nom purr'
        elif food == "meat":
            return 'nom nom nom'
        else:
            return '*pushes away in disgust* MEOW'

    def pounce(self, object):
        return 'sneaks up on ' + object + ' and pounces on ' + object