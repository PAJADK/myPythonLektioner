from biblioteket import Bog, Film

bog1 = Bog(2, "min bog", 99, 3, 1989, 560, "lars larsen")
film1 = Film(45, "die hard 3", 15, 2, 2007, "John wien", 90)
print(bog1.tostring())
print(film1.tostring())
