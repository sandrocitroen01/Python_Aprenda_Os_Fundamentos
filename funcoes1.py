"""
def print_text():  # Definindo a função chamada 'print_text'. Ela não recebe parâmetros.
    print("Aqui é um texto!")  # Quando chamada, essa função imprime a mensagem "Aqui é um texto!" na tela.
    
print_text()  # Chamando a função 'print_text', que executa o código dentro dela e imprime a mensagem.

"""

"""
def print_isto(x):  # Definindo a função chamada 'print_isto', que recebe um parâmetro 'x'.
    print(x)  # A função imprime o valor que foi passado como argumento na chamada da função.
    
print_isto(2222)  # Chamando a função 'print_isto' e passando o valor 2222 como argumento. Isso será impresso.

"""

"""
def potencia(x):  # Definindo a função chamada 'potencia', que recebe um parâmetro 'x'.
    p = x ** 2  # Calcula o quadrado de 'x' e armazena o resultado na variável 'p'.
    return p  # Retorna o valor de 'p', ou seja, o quadrado de 'x'.

valor = int(input("Digite um valor:"))  # Solicita ao usuário que insira um valor e converte para inteiro.
print(potencia(valor))  # Chama a função 'potencia' passando o valor inserido e imprime o resultado (o quadrado do valor).

"""

def potencia_n(y, n):  # Define a função chamada 'potencia_n', que recebe dois parâmetros: 'y' e 'n'.
    p = y ** n  # Calcula 'y' elevado à potência 'n' e armazena o resultado na variável 'p'.
    return p  # Retorna o valor de 'p', ou seja, 'y' elevado a 'n'.

n1 = int(input("Digite o número: "))  # Solicita ao usuário que insira o número base e converte para inteiro.
p1 = int(input("Digite a potência: "))  # Solicita ao usuário que insira a potência e converte para inteiro.

print(potencia_n(n1, p1))  # Chama a função 'potencia_n' passando 'n1' (número base) e 'p1' (potência) e imprime o resultado.
