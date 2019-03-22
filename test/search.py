#import datetime, calendar

lande = ["Danmark", "Tyskland", "Sverige", "Holland", "Polen", "Italien", "Norge"]
lande = [x.lower() for x in lande]
txtInput = input("Indtast lande navn: ").lower()

if any(txtInput in l for l in lande):
    print("Har fundet: ")
    for land in lande:
        if land.__contains__(txtInput):
            print("\t" + land.title())
else:
    print("Har ikke fundet nogen")


"""


def monday():
    return "mandag"

def tuesday():
    return "tirsdag"

def wednesday():
    return "onsdag"

def thursday():
    return "torsdag"

def friday():
    return "fridag"

def saturday():
    return "lørdag"

def sunday():
    return "søndag"

def default():
    return "Incorrect day"

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
}


def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()


print(switch(1).title())
print(switch(7).title())

idag = datetime.date.today()
print(idag)

dg = calendar.monthrange(idag.year, idag.month)[0]
print(dg)
"""