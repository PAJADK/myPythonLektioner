from biblioteket import Materiale, Bog, Film

bog1 = Bog(2, "min bog", 99, 3, 1989, 560, "lars larsen")
film1 = Film(45, "die hard 3", 15, 2, 2007, "John wien", 90)

if isinstance(bog1, Bog):
   print("bog1 er en Bog")
else:
   print("bog1 er ikke en Bog")
if isinstance(film1, Film):
   print("film1 er en Film")
else:
   print("film1 er ikke en film")

if isinstance(film1, Materiale):
   print("film1 er Materiale")
else:
   print("film1 er ikke Materiale")

if isinstance(film1, Bog):
   print("film1 er en Bog")
else:
   print("film1 er ikke en Bog")