i: int

"""
for i in range(0, 10):
    print(i)
    
# Utilizando o FOR usando a palavra reservada PASSO representada pelo número de que vc deseja (2).
for i in range(10, 15, 2):
    print(i)
    
# Percorrendo do modo inverso 
for i in range(50, 0, -10):
    print(i)
"""
total = 0
total: float
media: float

qtdNotas = int(input("Informe a quantidades de notas para ser lidas: "))

for i in range(0, qtdNotas):
    nota = float(input(f"Informe a {i + 1}º nota: "))
    total = total + nota

media = total / qtdNotas

print(f"A média aritimetica das notas é: {media:.2f} ")

print('Final!')

