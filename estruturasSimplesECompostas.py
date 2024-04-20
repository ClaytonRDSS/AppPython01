# idade = -1

"""
if idade == 18:
    print("Você é daulto!")
elif idade < 18:
    print("Você é adolecente!")
elif idade > 50:
    print("Você é Idoso!")
"""
idade = int(input("Informe sua Idade: "))

if idade >= 0 and idade <= 12:
    print("Criança!")
elif idade >= 13 and idade <=17:
    print("Adolecente!")
elif idade >= 18 and idade < 60:
    print("Adulto!")
elif idade >= 60:
    print("Idoso!")