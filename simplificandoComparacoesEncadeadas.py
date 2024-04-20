idade = int(input("Informe sua Idade: "))

# idade >= 0 and idade < 12
if 0 <= idade < 12:
    print("Criança!")

# idade >= 12 and idade < 18
elif 12 <= idade < 18:
    print("Adolecente!")

# idade >= 18 and idade < 60
elif 18 <= idade < 60:
    print("Adulto!")


elif idade >= 60:
    print("Idoso!")
