import numpy as np  # Importa a biblioteca 'numpy', usada para manipulação de arrays e funções matemáticas.
import matplotlib.pyplot as plt  # Importa a sub-biblioteca 'pyplot' de 'matplotlib', que é usada para criar gráficos.

x = np.linspace(0, 2, 1000)  # Cria um vetor 'x' com 1000 pontos igualmente distribuídos entre 0 e 2 (inclusivo).

y = 2 * x  # Cria o vetor 'y' aplicando a fórmula y = 2 * x. Isso cria uma linha reta.
y2 = x ** 2  # Cria o vetor 'y2' aplicando a fórmula y2 = x^2. Isso cria uma parábola.

# Cria uma figura com duas subplots (1 linha, 2 colunas)
fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # Cria um conjunto de subgráficos: 1 linha e 2 colunas, com tamanho 12x6 polegadas.

# Primeiro gráfico na primeira subplot
axes[0].plot(x, y, '*r')  # Plota 'x' contra 'y' com pontos vermelhos ('*r') na primeira subplot (axes[0]).
axes[0].set_xlabel("Eixo x")  # Adiciona rótulo "Eixo x" ao eixo X da primeira subplot.
axes[0].set_ylabel("Eixo y")  # Adiciona rótulo "Eixo y" ao eixo Y da primeira subplot.
axes[0].set_title("Gráfico 1: y = 2 * x")  # Define o título do gráfico da primeira subplot.
axes[0].grid(True)  # Adiciona uma grade ao gráfico da primeira subplot.

# Segundo gráfico na segunda subplot
axes[1].plot(x, y2, '.b')  # Plota 'x' contra 'y2' com pontos azuis ('.b') na segunda subplot (axes[1]).
axes[1].set_xlabel("Eixo x")  # Adiciona rótulo "Eixo x" ao eixo X da segunda subplot.
axes[1].set_ylabel("Eixo y")  # Adiciona rótulo "Eixo y" ao eixo Y da segunda subplot.
axes[1].set_title("Gráfico 2: y = x^2")  # Define o título do gráfico da segunda subplot.
axes[1].grid(True)  # Adiciona uma grade ao gráfico da segunda subplot.

# Ajusta o espaçamento entre os gráficos
plt.tight_layout()  # Ajusta automaticamente o espaçamento entre os gráficos para que não se sobreponham.

# Mostra os gráficos
plt.show()  # Exibe os gráficos na tela.
