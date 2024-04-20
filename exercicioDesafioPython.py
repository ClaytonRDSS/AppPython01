
entrar = "sim"
historico = []

while entrar == "sim" or entrar == "s" or entrar == "":
    num1 = float(input("Informe o primeiro valor: "))

    repetir = True

    while repetir:
        print("Digite [1] para soma")
        print("Digite [2] para subtração")
        print("Digite [3] para multiplicação")
        print("Digite [4] para divisão")

        operacao = int(input("Informe o código da operação desejada: "))

        if operacao < 1 or operacao > 4:
            print("Desculpe, o valor digitado é inválido")
        else:
            repetir = False

    num2 = float(input("Informe o segundo valor: "))

    resultado = 0
    operador = ""

    if operacao == 1:
        resultado = num1 + num2
        operador = "+"
    elif operacao == 2:
        resultado = num1 - num2
        operador = "-"
    elif operacao == 3:
        resultado = num1 * num2
        operador ="x"
    elif operacao == 4:
        resultado = num1 / num2
        operador = "/"

    historico.append(f"{num1} {operador} {num2} =  {resultado} ")

    print(f"O resultado é: {resultado}")

    entrar = input("Deseja realizar um novo cálculo? ")

print("---------------------")
print("Hiostórico: ")
for i in range(0, len(historico)):
    print(historico[i])


