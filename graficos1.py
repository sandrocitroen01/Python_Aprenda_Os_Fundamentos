import numpy as np  # Importa a biblioteca 'numpy', que é usada para trabalhar com arrays e funções matemáticas.
import matplotlib.pyplot as plt  # Importa a biblioteca 'matplotlib.pyplot', que é usada para criar gráficos.

x = np.linspace(0, 2, 1000)  # Cria um vetor 'x' com 1000 pontos igualmente distribuídos entre 0 e 2 (inclusivo).

y = 2 * x  # Cria o vetor 'y' aplicando a fórmula y = 2 * x. Isso cria uma linha reta.
y2 = x ** 2  # Cria o vetor 'y2' aplicando a fórmula y2 = x^2. Isso cria uma parábola.

plt.plot(x, y, '*r')  # Cria um gráfico de linha com o vetor 'x' no eixo X e 'y' no eixo Y. O gráfico usa pontos vermelhos ('*r').
plt.plot(x, y2, '.b')  # Cria outro gráfico de linha com o vetor 'x' no eixo X e 'y2' no eixo Y. O gráfico usa pontos azuis ('.b').

plt.xlabel("Eixo x")  # Adiciona um rótulo no eixo X com o texto "Eixo x".
plt.ylabel("Eixo y")  # Adiciona um rótulo no eixo Y com o texto "Eixo y".
plt.title("Teste de Gráfico")  # Adiciona um título ao gráfico com o texto "Teste de Gráfico".

plt.show()  # Exibe o gráfico na tela.
