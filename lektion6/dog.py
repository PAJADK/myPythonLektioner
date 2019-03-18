class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hair = 'Black'

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('willi', 6)
print("My dog's name is " + my_dog.name.title() + " with " + my_dog.hair + " hair")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

class Races(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.races = 'Boxer'

    def raceing(self):
        print("My dog's races is: " + self.races)
my_races = Races('jojo', 8)
print("My dog's name is " + my_races.name.title() + " with " + my_dog.hair + " hair")
print("My dog is " + str(my_races.age) + " years old.")
my_races.raceing()


