from biblioteket import Bog, Film

bog1 = Bog(2, "min bog", 99, 3, 1989, 560, "lars larsen")
film1 = Film(45, "die hard 3", 15, 2, 2007, "John wien", 90)

minListe = [bog1, film1]

for m in minListe:
   print("\n" + m.tostring())
