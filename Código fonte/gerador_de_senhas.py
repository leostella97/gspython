import tkinter as tk
from tkinter import messagebox
import secrets
import string
import webbrowser


def gerar_senha(_event=None):
    # validate input
    try:
        tamanho = int(entrada_tamanho.get())
    except (ValueError, TypeError):
        messagebox.showerror("Erro", "Informe um número inteiro válido para o tamanho da senha.")
        return

    # limit size to reasonable bounds
    if tamanho <= 0:
        messagebox.showerror("Erro", "O tamanho da senha deve ser maior que zero.")
        return
    if tamanho > 256:
        messagebox.showwarning("Aviso", "Tamanho muito grande, usando 256 como máximo.")
        tamanho = 256

    # use a concise, non-redundant character set
    chars = string.ascii_letters + string.digits + string.punctuation

    senha = "".join(secrets.choice(chars) for _ in range(tamanho))

    senha_gerada.delete(0, tk.END)
    senha_gerada.insert(0, senha)


def copiar_senha():
    senha = senha_gerada.get()
    if not senha:
        messagebox.showinfo("Info", "Não há senha para copiar. Gere uma senha primeiro.")
        return
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    messagebox.showinfo("Copiado", "Senha copiada para a área de transferência.")


def abrir_link(_event=None):
    webbrowser.open_new("https://leonardostella.lesttech.com.br/")


janela = tk.Tk()
janela.title("Gerador de Senha")
janela.resizable(False, False)

tk.Label(janela, text="Tamanho da senha: ").grid(row=0, column=0, padx=6, pady=6)

entrada_tamanho = tk.Entry(janela)
entrada_tamanho.grid(row=0, column=1, padx=6, pady=6)
entrada_tamanho.insert(0, "12")

botao_gerar = tk.Button(janela, text="Gerar senha", command=gerar_senha)
botao_gerar.grid(row=1, column=0, padx=6, pady=6)

botao_copiar = tk.Button(janela, text="Copiar", command=copiar_senha)
botao_copiar.grid(row=1, column=1, padx=6, pady=6)

senha_gerada = tk.Entry(janela, width=40)
senha_gerada.grid(row=2, column=0, columnspan=2, padx=6, pady=(0, 6))

texto_desenvolvido_por = tk.Label(janela, text="Desenvolvido por Leonardo Stella", fg="blue", cursor="hand2")
texto_desenvolvido_por.grid(row=3, column=0, columnspan=2, pady=(0, 6))
texto_desenvolvido_por.bind("<Button-1>", abrir_link)
texto_desenvolvido_por.bind("<Enter>", lambda event: texto_desenvolvido_por.config(font=("Arial", 10, "underline")))
texto_desenvolvido_por.bind("<Leave>", lambda event: texto_desenvolvido_por.config(font=("Arial", 10)))

# bind Enter to generate password
janela.bind('<Return>', gerar_senha)

janela.mainloop()
