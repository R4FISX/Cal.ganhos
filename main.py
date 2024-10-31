import tkinter as tk
from tkinter import messagebox

# Funções de cálculo
def calcular_cash():
    try:
        vendas = float(entry_vendas.get())
        cash = (vendas // 15) * 1000  # Divisão inteira para calcular o cash
        label_resultado_cash.config(text=f"Valor total em Cash: R$ {int(cash)}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para vendas.")

def calcular_comissao():
    try:
        vendas = float(entry_vendas.get())
        percentual = float(entry_percentual.get()) / 100  # Obtém o percentual do campo de entrada manual
        comissao = vendas * percentual
        label_resultado_comissao.config(text=f"Valor total da Comissão: R$ {comissao:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para vendas e percentual de comissão.")

# Função principal para inicializar a interface
def iniciar_interface():
    janela = tk.Tk()
    janela.title("Calculadora de Ganhos")
    janela.geometry("500x500")
    janela.configure(bg="#0047ab")  # Fundo azul

    # Título centralizado
    label_titulo = tk.Label(janela, text="Calculadora de Ganhos", font=("Arial", 24, "bold"), bg="#0047ab", fg="white")
    label_titulo.pack(pady=20)

    # Campo de entrada para vendas
    global entry_vendas
    entry_vendas = tk.Entry(janela, font=("Arial", 12), width=30)
    entry_vendas.pack(pady=10)

    # Label e campo de entrada manual para percentual de comissão
    global entry_percentual
    label_percentual = tk.Label(janela, text="Digite a % de Comissão:", font=("Arial", 10), bg="#0047ab", fg="white")
    label_percentual.pack(pady=5)
    entry_percentual = tk.Entry(janela, font=("Arial", 12), width=10)
    entry_percentual.pack(pady=5)
    entry_percentual.insert(0, "5")  # Valor padrão de 5%

    # Frame para botões de cálculo
    frame_botoes = tk.Frame(janela, bg="#0047ab")
    frame_botoes.pack(pady=20)

    # Botão para calcular ganhos em Cash
    botao_cash = tk.Button(frame_botoes, text="Calcular ganhos em Cash", command=calcular_cash, font=("Arial", 10), width=20)
    botao_cash.grid(row=0, column=0, padx=10)

    # Botão para calcular ganhos em Reais
    botao_reais = tk.Button(frame_botoes, text="Calcular ganhos em Reais", command=calcular_comissao, font=("Arial", 10), width=20)
    botao_reais.grid(row=0, column=1, padx=10)

    # Label para exibir o valor total em Cash
    global label_resultado_cash
    label_resultado_cash = tk.Label(janela, text="Valor total em Cash: R$ 0.00", font=("Arial", 12), bg="#0047ab", fg="white", wraplength=400)
    label_resultado_cash.pack(pady=5)

    # Label para exibir o valor total da comissão
    label_comissao = tk.Label(janela, text="Comissão", font=("Arial", 16, "bold"), bg="#0047ab", fg="white")
    label_comissao.pack(pady=10)

    global label_resultado_comissao
    label_resultado_comissao = tk.Label(janela, text="Valor total da Comissão: R$ 0.00", font=("Arial", 12), bg="#0047ab", fg="white", wraplength=400)
    label_resultado_comissao.pack(pady=5)

    janela.mainloop()

# Execução da interface
if __name__ == "__main__":
    iniciar_interface()
