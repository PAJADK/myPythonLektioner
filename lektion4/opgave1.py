"""
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")


rentalCar = input("What kind of rental car you would like? ")
print("Let me see if I can find you a " + rentalCar.title() + ".")

dinnerGroup = input("how many people are in your dinner group? ")
dinnerGroup = int(dinnerGroup)
if dinnerGroup > 8:
    print("\nYou’ll have to wait for a table.")
else:
    print("\nYour table is ready.")
"""
multiples_of_ten = input("Please enter a number: ")
multiples_of_ten = int(multiples_of_ten)
if multiples_of_ten % 10 == 0:
    print(multiples_of_ten, "is a multiple of 10.")
else:
    print(multiples_of_ten, "is not a multiple of 10.")
