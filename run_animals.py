from dog_class import Dog
from cat_class import Cat



# Initialise dog object (name, age, coat, colour, tail)
clifford_dog = Dog(age=4)
print(clifford_dog.age)
print(clifford_dog.tail)

# call method .bark()
print(clifford_dog.bark())

# calling multiple arg function .eat()
print(clifford_dog.eat("toxic waste"))


# Initialise cat object (name, age, fur, colour, tail, claws)
sylvester_cat= Cat(age=10)

# call method .purr()
print(sylvester_cat.purr())

# .eat()
print(sylvester_cat.eat("fish"))