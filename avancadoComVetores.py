"""
# Declarando vetores no formato Lista

frutas = ["Abacaxi", "Uva", "Banana", 10, 55.33]

#print(frutas[2])

# Imprime o tamanhanho do vetor
#print(len(frutas))

# Percorrendo vetores de tamanho dinamicos
for i in range(0, len(frutas)):
    print(frutas[i])

print("----------------------------------------")


# Inclusão de elementos em um vetor já declarado
# Inclusão no fim da lista
frutas.append("Mamão")

for i in range(0, len(frutas)):
    print(frutas[i])

"""

# Incusão de valores em lista vasia dinamicamente
valores = []

valor = int(input("Digite um valor: "))

while valor >= 0:
    valores.append(valor)
    valor = int(input("Digite um valor: "))


for i in range(0, len(valores)):
    print(valores[i])