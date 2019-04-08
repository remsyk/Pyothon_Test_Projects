
class Pet:
# Create two variables kind and color; assign values
    kind = "pet"
    color = "red"

    def __init__(self, name, person):
    # In the constructor, initialize the pets name
        self.name = name
        self.person = person

    def do_tricks(self):
    # Print the name of the pet and that it is doing tricks
        print(self.name, "is doing tricks!")
    # Call the speak method
        self.speak()
    # Call the jump method
        self.jump()

    def speak(self):
        pass
    def jump(self):
        pass

# Owner action returns the name of the owner
    def own(self):
        print("My owner is:", self.person)


class Jumper(Pet):
    #'This is a mixin class for jump'
    def jump(self):
    # Create jump method that prints that a Pet is jumping and the pets name
        print(self.name, "is jumping!")


class Dog(Jumper):  # You will need to inherit for this to work
# Change kind to canine
    kind = "Canine"
    owner = "Billy"
    color = "Brown"

    def __str__(self):
    # Print the name and description of dog
        print(self.name, "is a normal dog with a normal face")

    def __call__(self, action):
    # Rollover action prints the name of the dog and that it is rolling over
        print(self.name, action)


class BigDog(Dog, Jumper):  # You will need to inherit for this to work
    # Change the color to tan
    color = "Tan"

    def __str__(self):
    # Print the name and description of BigDog
        print(self.name, "is a bigger than normal dog with a bigger than normal face" )

    def speak(self):
    # Print dogs name and what it says
        print(self.name, "says Woof!")


class SmallDog(Dog, Jumper):  # You will need to inherit for this to work
# Change the color to brindle
    color = "Brindle"

    def __str__(self):
    # Print the name and description of SmallDog
        print(self.name, "is a smaller than normal dog with a smaller than normal face")

    def speak(self):
    # Print dogs name and what it says
        print(self.name, "says Woof!")


class Cat(Jumper):  # You will need to inherit for this to work
# Change the kind to feline
    kind = "Feline"
    color = "Yellow"

    def __str__(self):
    # Print the name and description of cat
        print(self.name, "is a normal cat with a normal face")


    def speak(self):
    # Print cats name and what it says
        print(self.name, "says Meow!")


    def climb(self):
    # Prints the name of the cat and that it is climbing
        print(self.name, "is climbing the mantle")


class HouseCat(Cat, Jumper):  # You will need to inherit for this to work
    # Change the color to white
    color = "White"

    def __str__(self):
    # Print the name and description of cat
        print(self.name, "is a house cat with a house cat face")

    def speak(self):
    # Print cats name and what it says
        print(self.name, "says Meow!")


###########################################

# EXERCISE YOUR CODE

#    1. Instantiate each class(except jumper)
Pet = Pet('Animal', "Ricky")
Dog = Dog("Smitty", "Susan")
BigDog = BigDog('Andrew', "Andree3000")
SmallDog = SmallDog("Olive", "Dwayne The Rock Johnson")
Cat = Cat("Moon", "Lil Business")
HouseCat = HouseCat("Olie", "A Tree")

#    2. Create a list of the instantiated objects
objList = [Pet, Dog, BigDog, SmallDog, Cat, HouseCat]

#    3. Loop through the objects
for i in range(1, 6):
#    4. Print __str__
    objList[i].__str__()
#    5. print the kind of pet
    print(objList[i].kind)
#    6. Print the Color of the pet
    print(objList[i].color)
#    7. Have the pet do tricks
    objList[i].do_tricks()

#    8. if applicable, print rollover action and the owners name
    if hasattr(objList[i], "__call__"):
        objList[i].__call__("is rolling over!")
    objList[i].own()

#    9. If applicable, have the pet climb
    if hasattr(objList[i], 'climb'):
        objList[i].climb()

#   10. To separate each pet print underscores
    print("___________________________________")
