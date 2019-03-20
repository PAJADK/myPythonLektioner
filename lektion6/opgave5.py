from biblioteket import Materiale, Bog, Film

m = Materiale(2, "min bog", 3, 0, 1989)
#m.udlaan(0)

bog1 = Bog(2, "min bog", 3, m.udlaan(1), 1989, 560, "lars larsen")
film1 = Film(45, "die hard 3", 3, m.udlaan(1), 2007, "John wien", 90)
kan_udlaane =m.kan_udlaane(m.udlaan(7))
#print(m.tostring())
print(bog1.tostring())
print(film1.tostring())
print(kan_udlaane)


