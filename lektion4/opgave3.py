""" Pakkeliste over typiske ting, som man skal have med på ferie """
pakkelisten = []
antal = 0
maxantal = int(input("Hvor mange ting skal du have med på ferie?:  "))

print("Skriv q, når du er færdig med at vælge. ")
while antal < maxantal:
    huskeliste = input("Hvad vil du have med på din ferie?: ")
    if antal == 3 and huskeliste == "q":
        break
    else:
        antal += 1
        pakkelisten.append(huskeliste)

print("\nDin pakkeliste indholder: ")
for pakkelist in pakkelisten:
    print("\t" + pakkelist)