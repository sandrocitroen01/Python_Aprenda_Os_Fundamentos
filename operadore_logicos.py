# Definindo as variáveis
a = 3
b = 5

# Operadores lógicos

# "and" - Ambas as condições precisam ser verdadeiras
print(a == 3 and b == 5)  # True: Ambas as condições são verdadeiras
print(a == 3 and b == 4)  # False: A segunda condição é falsa

# "or" - Pelo menos uma condição precisa ser verdadeira
print(a == 3 or b == 4)   # True: A primeira condição é verdadeira
print(a == 4 or b == 4)   # False: Ambas as condições são falsas

# "not" - Inverte o valor da condição
print(not(a == 3))  # False: a == 3 é True, então "not" inverte para False
print(not(b == 3))  # True: b == 3 é False, então "not" inverte para True
