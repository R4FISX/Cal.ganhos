import tkinter as tk
from tkinter import messagebox

# Função para calcular o total de cash
def calcular_cash():
    try:
        vendas = float(entry_vendas.get())
        cash = (vendas // 15) * 1000  # Divisão inteira para calcular o cash
        label_resultado_cash.config(text=f"Total de Cash: {int(cash)}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

# Função para calcular a comissão de 5%
def calcular_comissao():
    try:
        vendas = float(entry_vendas.get())
        comissao = vendas * 0.05  # Calcula 5% das vendas
        label_resultado_comissao.config(text=f"Comissão de 5%: R$ {comissao:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

janela = tk.Tk()
janela.title("Calculadora de Ganhos e Comissão")
janela.geometry("400x200")

frame_cash = tk.Frame(janela)
frame_cash.grid(row=0, column=0, padx=10, pady=10)

# Título da calculadora de Cash
label_titulo_cash = tk.Label(frame_cash, text="Calculadora de Cash", font=("Arial", 12, "bold"))
label_titulo_cash.pack()

# Criar um rótulo e entrada para o valor das vendas
label_vendas = tk.Label(frame_cash, text="Valor Total de Vendas (R$):")
label_vendas.pack(pady=5)

entry_vendas = tk.Entry(frame_cash)
entry_vendas.pack(pady=5)

# Criar um botão para calcular o cash
botao_calcular_cash = tk.Button(frame_cash, text="Calcular Cash", command=calcular_cash)
botao_calcular_cash.pack(pady=5)

# Criar um rótulo para exibir o resultado do cash
label_resultado_cash = tk.Label(frame_cash, text="Total de Cash: 0")
label_resultado_cash.pack(pady=5)

# Frame para a segunda calculadora (Comissão)
frame_comissao = tk.Frame(janela)
frame_comissao.grid(row=0, column=1, padx=10, pady=10)

# Título da calculadora de Comissão
label_titulo_comissao = tk.Label(frame_comissao, text="Calculadora de Comissão", font=("Arial", 12, "bold"))
label_titulo_comissao.pack()

# Criar um botão para calcular a comissão
botao_calcular_comissao = tk.Button(frame_comissao, text="Calcular Comissão", command=calcular_comissao)
botao_calcular_comissao.pack(pady=5)

# Criar um rótulo para exibir o resultado da comissão
label_resultado_comissao = tk.Label(frame_comissao, text="Comissão de 5%: R$ 0.00")
label_resultado_comissao.pack(pady=5)

# Iniciar o loop da interface gráfica
janela.mainloop()
