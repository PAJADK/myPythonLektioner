car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# opave 3

navne = {"Ole": "olesen", "Morten": "sørensen", "Louise": "due",
         "hanne": "peterson", "henrik": "olsen"}

for navn, efternavn in navne.items():
    print(navn.title())
    print(efternavn.title())
    print(navn.title() + " " + efternavn.title())

navne['kim'] = 'hansen'
print(navne)
print("******* Get ******* " + navne.get('Morten'))

usa = {"navn": "usa",
         "cities": ["new yourk", "washinton", "los angeles"]}

print(" ******** land er " + usa["navn"].upper())
for by in usa['cities']:
    print("\t" + by.title())

tyskland = {"navn": "tyskland",
         "cities": ["berlin", "hamburg", "flensbourg"]}

print(" ******** land er " + tyskland["navn"].title())
for by in tyskland['cities']:
    print("\t" + by.title())


countries = []
countries.append(usa)
countries.append(tyskland)

for country in countries:
    if country['navn'] == "usa":
        print(country['navn'].upper())
    else:
        print(country['navn'].title())
    for city in country['cities']:
        print("\t" + city.title())

# Opgave 6 - søgning
lande = ["Danmark", "Tyskland", "Sverige", ""]
x = input("Søg land her: ")
sub = x

for land in lande:
    if sub in land:
        print("Har fundet: " + sub.title())
        break
    else:
        print("ikke fundet")


"""


my_dict = dict({1: 'apple', 2: 'ball'})
print(my_dict.keys())

iphoneReleased = {
    "iphone": 2007,
    "iphone 3G": 2008,
    "iphone 3GS": 2009,
    "iphone 4": 2010,
    "iphone 4S": 2011,
    "iphone 5": 2012
}

for item in iphoneReleased:
    if "iphone 5" in iphoneReleased:
        print("Key found")
        break
    else:
        print("No keys found")

print("Values: ")

for year in iphoneReleased:
    releases= iphoneReleased[year]
    print(releases)

count = {}
for element in iphoneReleased:
    count[element] = count.get(element, 0) + 1
print(count)

# Map 
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

# Filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
"""
