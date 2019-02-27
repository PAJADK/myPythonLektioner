ordbog = {'hun': 'she', 'han': 'he', 'god morgen': 'good morning', 'hvor':'where'}

inverted_ordbog = dict([[v, k] for k, v in ordbog.items()])
#print(inverted_ordbog)

mereInput = True
print("Skriv q, når du er færdig med ordbogen. ")
while mereInput:
    engelsk = input("Indtast engelsk ord: ")
    if engelsk == 'q':
        mereInput = False
    if engelsk != inverted_ordbog.keys():
        print(engelsk + " Findes ikke i ordbogen!")

    for key, value in inverted_ordbog.items():
        if key == engelsk:
            print("\n" + key.title() + " --> " + value)


