import numpy as np              # Importa a biblioteca numpy, que será usada para gerar números aleatórios
import tkinter as tk            # Importa o tkinter para criar a interface gráfica
from tkinter import messagebox  # Importa a biblioteca de caixas de mensagens do tkinter

class JogoAdivinhacao:         # Definição da classe principal que irá controlar o jogo
    def __init__(self, root):  # Método construtor que inicializa os elementos do jogo
        self.root = root       # A variável 'root' será a janela principal da interface gráfica
        self.root.title("Jogo de Adivinhação")  # Define o título da janela principal
        
        self.numero_oculto = np.random.randint(0, 51)  # Gera um número aleatório entre 0 e 50 (inclusivo)
        self.tentativas_totais = 10  # Número total de tentativas do jogador
        self.tentativas_feitas = 0   # Inicializa o contador de tentativas feitas

        # Cria um rótulo (label) para mostrar o título na interface
        self.label_titulo = tk.Label(self.root, text="Bem-vindo ao jogo de adivinhação!", font=("Arial", 14))
        self.label_titulo.pack(pady=10)  # Exibe o título com um espaço vertical de 10 pixels

        # Cria um rótulo para mostrar as instruções do jogo
        self.label_instrucoes = tk.Label(self.root, text="Adivinhe o número entre 0 e 50.", font=("Arial", 12))
        self.label_instrucoes.pack(pady=5)  # Exibe as instruções com um espaço vertical de 5 pixels

        # Cria um rótulo para pedir o palpite do jogador
        self.label_palpite = tk.Label(self.root, text="Digite seu palpite:", font=("Arial", 12))
        self.label_palpite.pack(pady=5)  # Exibe a solicitação do palpite com um espaço de 5 pixels

        # Cria um campo de entrada (Entry) para o jogador digitar o seu palpite
        self.entry_palpite = tk.Entry(self.root, font=("Arial", 12))
        self.entry_palpite.pack(pady=5)  # Exibe o campo de entrada com um espaço de 5 pixels

        # Cria um botão que, quando clicado, chama a função 'adivinhar'
        self.button_adivinhar = tk.Button(self.root, text="Adivinhar", font=("Arial", 12), command=self.adivinhar)
        self.button_adivinhar.pack(pady=10)  # Exibe o botão com um espaço de 10 pixels

        # Cria um rótulo para mostrar quantas tentativas restantes o jogador tem
        self.label_tentativas = tk.Label(self.root, text=f"Tentativas restantes: {self.tentativas_totais}", font=("Arial", 12))
        self.label_tentativas.pack(pady=5)  # Exibe as tentativas restantes com um espaço de 5 pixels

    # Função que é chamada quando o jogador clica no botão para adivinhar
    def adivinhar(self):
        try:
            # Tenta converter a entrada do jogador em um número inteiro
            palpite = int(self.entry_palpite.get())
            
            # Verifica se o palpite está dentro do intervalo permitido (0 a 50)
            if palpite < 0 or palpite > 50:
                messagebox.showwarning("Entrada inválida", "Por favor, insira um número entre 0 e 50.")
                return  # Sai da função caso o número seja inválido

            # Incrementa o contador de tentativas feitas
            self.tentativas_feitas += 1
            tentativas_restantes = self.tentativas_totais - self.tentativas_feitas  # Calcula as tentativas restantes
            self.label_tentativas.config(text=f"Tentativas restantes: {tentativas_restantes}")  # Atualiza o rótulo de tentativas restantes
            
            # Verifica se o palpite está correto
            if palpite == self.numero_oculto:
                messagebox.showinfo("Parabéns!", f"Você acertou o número {self.numero_oculto} em {self.tentativas_feitas} tentativas!")
                self.resetar_jogo()  # Reinicia o jogo caso o jogador tenha acertado
            elif palpite < self.numero_oculto:
                messagebox.showinfo("Dica", "O número oculto é maior que o seu palpite.")  # Dica se o palpite for menor
            else:
                messagebox.showinfo("Dica", "O número oculto é menor que o seu palpite.")  # Dica se o palpite for maior

            # Verifica se o jogador já usou todas as tentativas
            if self.tentativas_feitas >= self.tentativas_totais:
                messagebox.showinfo("Fim de Jogo", f"Você não conseguiu adivinhar o número. Era {self.numero_oculto}.")
                self.resetar_jogo()  # Reinicia o jogo caso as tentativas se esgotem
        except ValueError:  # Caso o jogador insira um valor não numérico
            messagebox.showwarning("Entrada inválida", "Por favor, insira um número inteiro válido.")

    # Função para reiniciar o jogo
    def resetar_jogo(self):
        self.numero_oculto = np.random.randint(0, 51)  # Gera um novo número aleatório entre 0 e 50
        self.tentativas_feitas = 0  # Reseta o contador de tentativas feitas
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas_totais}")  # Atualiza o rótulo de tentativas
        self.entry_palpite.delete(0, tk.END)  # Limpa o campo de entrada do palpite

# Cria a janela principal do jogo
root = tk.Tk()

# Cria a instância do jogo e passa a janela principal como parâmetro
jogo = JogoAdivinhacao(root)

# Inicia o loop principal do Tkinter, que mantém a janela aberta
root.mainloop()
