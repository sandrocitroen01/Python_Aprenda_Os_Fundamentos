"""
def soma(a, b):  # Definindo a função 'soma', que recebe dois parâmetros 'a' e 'b'.
    s = a + b  # Realiza a soma de 'a' e 'b' e armazena o resultado na variável 's'.
    return s  # Retorna o valor de 's', que é a soma de 'a' e 'b'.

n1 = int(input("Digite um valor inteiro: "))  # Solicita ao usuário que insira um valor inteiro para 'n1'.
n2 = int(input("Digite outro valor inteiro: "))  # Solicita ao usuário que insira outro valor inteiro para 'n2'.

print("A soma é: ", soma(n1, n2))  # Chama a função 'soma' passando os valores 'n1' e 'n2' e imprime o resultado.
"""

def soma(a, b):  # Definindo a função 'soma', que recebe dois parâmetros 'a' e 'b'.
    s = a + b  # Realiza a soma de 'a' e 'b' e armazena o resultado na variável 's'.
    return s  # Retorna o valor de 's', que é a soma de 'a' e 'b'.

def multiplica(a, b):  # Definindo a função 'multiplica', que recebe dois parâmetros 'a' e 'b'.
    m = a * b  # Realiza a multiplicação de 'a' e 'b' e armazena o resultado na variável 'm'.
    return m  # Retorna o valor de 'm', que é o produto de 'a' e 'b'.

def soma_multiplica(a, b):  # Definindo a função 'soma_multiplica', que recebe dois parâmetros 'a' e 'b'.
    s = soma(a, b)  # Chama a função 'soma' e armazena o resultado da soma em 's'.
    m = multiplica(a, b)  # Chama a função 'multiplica' e armazena o resultado da multiplicação em 'm'.
    return print("Soma = " + str(s) + ", Multiplica = " + str(m))  # Imprime o resultado da soma e da multiplicação.

soma_multiplica(2, 5)  # Chama a função 'soma_multiplica' passando os valores 2 e 5, e imprime os resultados.
