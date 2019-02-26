""" Pakkeliste over typiske ting, som man skal have med på ferie """

pakkelisten = []
antal = 0
maxantal = int(input("Hvor mange ting skal du have med på ferie?:  "))

print("Skriv quit, når du er færdig med at vælge pakkelisten. ")
while antal < maxantal:
    huskeliste = input("Hvad vil du have med på din ferie?: ")
    if antal >= 2 and huskeliste == "quit":
        break
    else:
        antal += 1
        pakkelisten.append(huskeliste)
print("\nDu har valgt følgende ting, som du vil have med på din ferie.")
for pakkelist in pakkelisten:
    print("\t" + pakkelist)