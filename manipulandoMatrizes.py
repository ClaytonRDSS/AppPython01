pessoas = [[0 for i in range(3)] for j in range(4)]


# EXEMPLO DE MATRIZ
#    0   1   2
# 0 [0] [0] [0]
# 1 [0] [0] [0]
# 2 [0] [0] [0]
# 3 [0] [0] [0]

# RECUPERANDO VALORES DA MATRIZ
# print(pessoas[0][1]) linha/ coluna

"""
pessoas[0][0] = "Clayton"
pessoas[0][1] = "Masculino"
pessoas[0][2] = 36
"""
for i in range(0, 4):
    for j in range(0, 3):
        if j == 0:
            pessoas[i][j] = input("Digite seu Nome: ")
        elif j == 1:
            pessoas[i][j] = int(input("Digite sua idade: "))
        elif j == 2:
            pessoas[i][j] = input("Informe seu Sexo: ")

# Impressão dos dados da Matriz
for i in range(0, 4):
    print()
    for j in range(0, 3):
        if j == 0:
            print(f"Nome: {pessoas[i][j]}", end=" - ")
        elif j == 1:
            print(f"Idade: {pessoas[i][j]}", end=" - ")
        elif j == 2:
            print(f"Sexo: {pessoas[i][j]}", end=" - ")


