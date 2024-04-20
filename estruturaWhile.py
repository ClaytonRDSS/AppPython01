continuar = 'sim'
total = 0

while continuar == 'sim' or continuar == 's' or continuar == '':
    valor = float(input("Informe um valor: "))
    total = total + valor
    continuar = input("Deseja continuar? ")


print(f"Valor total da soma dos valores informados é: {total}")