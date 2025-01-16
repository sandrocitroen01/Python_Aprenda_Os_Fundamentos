import numpy as np  # Importa a biblioteca 'numpy', usada para manipulação de arrays e funções matemáticas.
import matplotlib.pyplot as plt  # Importa a sub-biblioteca 'pyplot' de 'matplotlib', que é usada para criar gráficos.

x = np.linspace(0, 2, 1000)  # Cria um vetor 'x' com 1000 pontos igualmente distribuídos entre 0 e 2 (inclusivo).

y = 2 * x  # Cria o vetor 'y' aplicando a fórmula y = 2 * x. Isso cria uma linha reta.
y2 = x ** 2  # Cria o vetor 'y2' aplicando a fórmula y2 = x^2. Isso cria uma parábola.

# Primeiro gráfico
plt.figure()  # Cria uma nova figura para o primeiro gráfico. Isso permite desenhar gráficos separados.
plt.plot(x, y, '*r')  # Plota 'x' contra 'y' com pontos vermelhos ('*r').
plt.xlabel("Eixo x")  # Adiciona rótulo "Eixo x" ao eixo X.
plt.ylabel("Eixo y")  # Adiciona rótulo "Eixo y" ao eixo Y.
plt.title("Gráfico 1: y = 2 * x")  # Define o título do gráfico.
plt.grid(True)  # Adiciona uma grade ao gráfico para facilitar a visualização.
plt.show()  # Exibe o primeiro gráfico.

# Segundo gráfico
plt.figure()  # Cria uma nova figura para o segundo gráfico.
plt.plot(x, y2, '.b')  # Plota 'x' contra 'y2' com pontos azuis ('.b').
plt.xlabel("Eixo x")  # Adiciona rótulo "Eixo x" ao eixo X.
plt.ylabel("Eixo y")  # Adiciona rótulo "Eixo y" ao eixo Y.
plt.title("Gráfico 2: y = x^2")  # Define o título do gráfico.
plt.grid(True)  # Adiciona uma grade ao gráfico.
plt.show()  # Exibe o segundo gráfico.
