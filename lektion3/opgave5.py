usa = {"navn": "usa",
         "cities": ["new yourk", "washinton", "los angeles"]}

# print(" ******** land er " + usa["navn"].upper())
# for by in usa['cities']:
#     print("\t" + by.title())

tyskland = {"navn": "tyskland",
         "cities": ["berlin", "hamburg", "flensbourg"]}

# print(" ******** land er " + tyskland["navn"].title())
# for by in tyskland['cities']:
#     print("\t" + by.title())

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

