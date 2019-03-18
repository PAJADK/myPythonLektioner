from typing import List

def kvadrat(x: float) -> float:
    return x * x

print("resultatet er " + str(kvadrat(7)))



liste = [1, 2, 3, 4]

def minsum(liste: List[int]) -> str:
    for summen in liste:
        summen = sum(liste)
    return str(summen)

print("summen er : " + str(minsum(liste)))


