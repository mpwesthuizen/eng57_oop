
class Dog():

    def __init__(self, name, age, coat, colour, tail):
        self.name = name
        self.age = age
        self.coat = coat
        self.colour = colour
        self.tail = bool(tail)


    def bark(self):
        return 'woof woof woof!'

    def eat(self, food):
        if "toxic" in food:
            return 'nom nom nom ... *starts vomitting*'
        else:
            return 'nom nom nom nom nom'

    def drink(self):
        return 'lap lap lap *the bowl was emptied*'

    def sleep(self):
        return 'zzzzZZzZZzzzz'

    def chase(self, object):
        return 'runs after' + object