# Retorna Verdadeiro. Para o operador (end) ás duas expressões tem que ser verdadeira
print(10 > 5 and "abacaxi" == "abacaxi")

# Retorna Folso pq o Python é  Case Sensitive. Mesmo nome más, cadeia de caracter diferente
print(10 > 5 and "abacaxi" == "Abacaxi")

# Retorna Verdadeiro. Para o operador (or) uma das duas expressões tem que ser verdadeira
print(7 < 3 or 8 == 8)

# O not Modifica o resultado da expressão de verdadeiro para Falso e vise versa
print(not 9 >= 9)

# Resolve primeiro o (not) depois o (or)
print((not 9 >= 9) or 7 == 7)
