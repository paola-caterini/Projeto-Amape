import tkinter as tk
from tkinter import messagebox
from controladores.admin_controller import AdminController

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login de Administrador")
        
        self.controller = AdminController('caminho/para/seu/banco_de_dados.db')
        
        self.label_usuario = tk.Label(root, text="Nome de Usuário")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()
        
        self.label_senha = tk.Label(root, text="Senha")
        self.label_senha.pack()
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack()
        
        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.pack()
        
    def login(self):
        nome_usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        
        if self.controller.autenticar_admin(nome_usuario, senha):
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            # Aqui você pode abrir a interface principal do sistema
        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")

if __name__ == '__main__':
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()