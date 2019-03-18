ordbog = {'hun':'she','han':'he', 'god morgen':'good morning'}
mereInput = True
while mereInput:
    dansk = input("Indtast dansk ord: ").title()
    engelsk = input("Indtast engelsk oversættelse: ").title()

# gemmer til en dictionary
    ordbog[dansk] = engelsk
    mereordpar = input("Vil du tilføje nye ordpar? (ja/ nej)")

    if mereordpar == 'nej':
        mereInput = False
        print("\n::::: Dansk-Engelsk ordbog :::::")

for dansk, engelsk in ordbog.items():
    print("\n" + dansk.title() + " --> " + engelsk.title())
