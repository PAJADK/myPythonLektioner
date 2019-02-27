lande = ["Danmark", "Tyskland", "Sverige", "Holland", "Polen", "Italien", "Norge"]
lande = [x.lower() for x in lande]

txtInput = input("Indtast lande navn: ").lower()

if any(txtInput in s for s in lande):
    print("Har fundet: ")
    for land in lande:
        if land.__contains__(txtInput):
            print("\t" + land.title())
else:
    print("Landet findes ikke: ")