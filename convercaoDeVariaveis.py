print("CALCULADORA DE IMC")

# Tipagem de variáveis
nome: str
peso: float
altura: float

# A tipagem dinamica do python não permite que o calculo seja feito
# Mesmo a variável sendo tipada como float
# Lendo dados para variáveis com (input)
nome = input("Informe o nome: ")

# Dessa forma o Python entende na hora da incerssão do dado que é para converter o dado.
peso = float(input("Informe o Peso: "))
altura = float(input("Informe a Altura: "))

# Interpolação
print(f"Nome: {nome} - Peso: {peso} - Altura: {altura}")

# Convertendo o tipo da Variável para fazer o calculo
# Sabendo que só pode mudar a variável que representa uma expressão numérica
#peso = float(peso)
#altura = float(altura)

# Imprmindo o novo tipo da variável na tela
#print(type(peso))
#print(type(altura))

imc = peso / (altura * altura)

if imc <= 24:
    print(f" Seu IMC é de : {imc:.2f} Você está no Limite de Peso")
elif imc > 24:
    print(f" Seu IMC é de : {imc:.2f} Você está acima do Peso. Va malhar!")