from biblioteket import Materiale, Bog, Film

m = Materiale(2, "min bog", 3, 1, 1989)
udlaan = m.udlaan(1)
bog1 = Bog(2, "min bog", 3, 1, 1989, 560, "lars larsen")
film1 = Film(45, "die hard 3", 15, 2, 2007, "John wien", 90)

print(bog1.tostring())
print(udlaan)