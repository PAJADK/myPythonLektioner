#Opgave 1 - definition af lister og loops.

forfattere =['Karen Blixen', 'Hans Christian Andersen', 'Benny Andersen', 'Vita Andersen', 'Peter Høeg']
print(forfattere)
#Tilføj en forfatter
forfattere.append('Inger Christensen')
print("********** Tilføj en forfatter ***********")
print(forfattere)

#slet en forfatter
del forfattere[1]
print("********** Slette forfatter nr 2 ***********")
print(forfattere)

for forfatter in forfattere:
    print(forfatter)

#Opgave 3 - længden af en liste
antal_forfattere = len(forfattere)
print(antal_forfattere)

forfattere.sort(reverse=True)
print(forfatter)


for number in range(1,11):
    print(number)
print(" ************ stat ********** ")

squares = []
for value in range(1,6):
 square = value**2
 squares.append(square)
 print(squares)

min_numbers = []
num = 3
tal_3_tabellen = 99 // num + 1
for min_number in range(1, tal_3_tabellen):
    min_number= min_number *num
    min_numbers.append(min_number)
    print(min_number)

print(" ************ end ********** ")
print(min_numbers)
print(min(min_numbers))
print(max(min_numbers))
print(sum(min_numbers))
print("  ********** Gennemsnittet ********** ")
print(sum(min_numbers)// len(min_numbers))

#slicing af lister
forfattere =['Karen Blixen', 'Hans Christian Andersen', 'Benny Andersen', 'Vita Andersen', 'Peter Høeg']
print(forfattere[0:3])
print(forfattere[3:5])



"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

names = ['Morten', 'Anders', 'flemming', 'Ole']
print(names[2].title())

message = "Hvordan går det {0}".format(names[0])
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(0,'bmw')
print(motorcycles)

motorcycles.sort(reverse=True)
print(motorcycles)

motorcycles.remove('bmw')
print(motorcycles)

del motorcycles[0]
print("motor ***************  del")
print(motorcycles)


popped_motorcycle = motorcycles.pop()
print("motor ***************  ")
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
motorcycles.sort()
print(motorcycles)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")


"""
