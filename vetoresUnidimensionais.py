"""
numeros = [0 for i in range(5)]

for x in range(0, 5):
    numeros[x] = int(input(f"Digite {x + 1}º Nome: "))


for x in range(0, 5):
    print(numeros[x])
"""

nomes: [str] = [0 for j in range(0, 5)]

for j in range(0, 5):
    nomes[j] = input(f"Infome o {j + 1}º nome: ")


for j in range(0, 5):
    print(f"{j + 1}º Nome: {nomes[j]}")