import tkinter as tk
import random
import string
import webbrowser

def gerar_senha():
    tamanho = int(entrada_tamanho.get())
    chars = string.ascii_letters + string.digits + '!@#$%&*()-+=,.;:/?[{<>}]qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    rnd = random.SystemRandom()
    senha = "".join(rnd.choice(chars) for i in range(tamanho))
    senha_gerada.delete(0, tk.END)
    senha_gerada.insert(0, senha)

def abrir_link(event):
    webbrowser.open_new("https://leonardostella.lesttech.com.br/")

janela = tk.Tk()

janela.title("Gerador de Senha")

tk.Label(janela, text="Tamanho da senha: ").grid(row=0, column=0)

entrada_tamanho = tk.Entry(janela)
entrada_tamanho.grid(row=0, column=1)

botao_gerar = tk.Button(janela, text="Gerar senha", command=gerar_senha)
botao_gerar.grid(row=1, column=0, columnspan=2)

senha_gerada = tk.Entry(janela, width=30)
senha_gerada.grid(row=2, column=0, columnspan=2)

texto_desenvolvido_por = tk.Label(janela, text="Desenvolvido por Leonardo Stella", fg="blue", cursor="hand2")
texto_desenvolvido_por.grid(row=3, column=0, columnspan=2)
texto_desenvolvido_por.bind("<Button-1>", abrir_link)
texto_desenvolvido_por.bind("<Enter>", lambda event: texto_desenvolvido_por.config(font=("Arial", 10, "underline")))
texto_desenvolvido_por.bind("<Leave>", lambda event: texto_desenvolvido_por.config(font=("Arial", 10)))

janela.mainloop()
