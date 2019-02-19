car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# opave 3

navne = {"Ole": "olesen", "Morten": "sørensen", "Louise": "due",
         "hanne": "peterson", "henrik": "olsen"}

for navn, efternavn in sorted(navne.items()):
    print(navn.title())
    print(efternavn.title())
    print(navn.title() + " " + efternavn.title())

navne['kim'] = 'hansen'
print(navne)
print("******* Get ******* " + navne.get('Morten'))
lands = {"land": "usa",
         "byer": ["new yourk", "washinton", "los angeles"]}
for by in lands['byer']:
    print("\t" + by.title())

print(lands["byer"])
print(lands.get('byer'))

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

""" Map """
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

""" Filter"""
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
