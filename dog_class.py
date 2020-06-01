from animal_class import *

class Dog(Animal):

    def __init__(self, age=0):
        super().__init__(self, "Irish setter", True, "red", "Clifford")
        self.age = age



    def bark(self):
        return 'woof woof woof!'

    def eat(self, food):
        if "toxic" in food:
            return 'nom nom nom ... *starts vomitting*'
        else:
            return 'nom nom nom nom nom'