from dog_class import *
from cat_class import *



# Initialise dog object (name, age, coat, colour, tail)
ferral_dog = Dog('???', '???', 'scruffy and tangled wire hair', 'dirty grey', tail=False)
print(ferral_dog.age)
print(ferral_dog.tail)

# call method .bark()
print(ferral_dog.bark())

# calling multiple arg function .eat()
print(ferral_dog.eat("toxic waste"))


# Initialise cat object (name, age, fur, colour, tail, claws)
house_cat= Cat('Precious', 3,'long and fluffy', 'cream', True)

print(house_cat.fur)
print(house_cat.claws)

# call method .purr()
print(house_cat.purr())

# polymorph with .eat()
print(house_cat.eat("fish"))