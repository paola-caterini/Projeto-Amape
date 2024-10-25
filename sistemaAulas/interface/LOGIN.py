import sqlite3
from time import sleep
from tkinter import *
from tkinter import ttk, messagebox
import base64

from click import command

from sistemaAulas.config import DB_PATH
from sistemaAulas.controladores.admin_controller import AdminController

#from sistemaAulas.config import DB_PATH
#from sistemaAulas.controladores.admin_controller import AdminController
#from  sistemaAulas import main


root = Tk()

class Cores_imagens():

    corFundo='#0D1521'
    cor_texto_titulo='yellow'
    cor_texto_pesquisa='blue'
    ########################################################################
    img_cadastro = PhotoImage(file='bt_Cadastro.png')
    img_Aulas = PhotoImage(file='bt_Aulas.png')
    img_Home = PhotoImage(file='bt_Home.png')
    img_Relatorios = PhotoImage(file='bt_Relatorios.png')
    img_Sol = PhotoImage(file='bt_Sol.png')
    img_log_out = PhotoImage(file='Log_out.png')
    img_LOGO = PhotoImage(file='LOGO.png')
    img_avatar = PhotoImage(file='Avatar.png')
    ########################################################################
    img_UserAdd = PhotoImage(file='bt_UserAdd.png')
    img_Edit = PhotoImage(file='bt_Edit.png')
    img_Lixeira = PhotoImage(file='bt_Lixeira.png')
    img_Refresh = PhotoImage(file='bt_Refresh.png')
    img_Printer = PhotoImage(file='bt_Printer.png')
    img_Search = PhotoImage(file='bt_Search.png')
    img_Moradores = PhotoImage(file='bt_Moradores.png')
    img_Professores = PhotoImage(file='bt_Professores.png')
    img_Usuarios = PhotoImage(file='bt_usuarios.png')

    

class Funçao(Cores_imagens):


    def conecta_bd(self):
        self.conn = sqlite3.connect("../sistema_aulas.db")
        self.cursor = self.conn.cursor();
        print("Conectando ao banco de dados")


    def desconecta_bd(self):
        self.conn.close();
        print("Desconectando ao banco de dados")



    #########tela home##########
    def bt_FrameLogin_entrar(self):
        #messagebox.showinfo("Sucesso", "Login bem-sucedido!")

        self.frameTela_Login.destroy()

        self.telaHome()
        '''
        nome_usuario=self.usuario_entry.get()
        senha=self.senha_entry.get()
        admin_controller = AdminController(DB_PATH)
        # Autenticar um administrador
        if admin_controller.autenticar_admin(nome_usuario, senha):
            print("Admin autenticado com sucesso!")
            #messagebox.showinfo("Sucesso", "Login bem-sucedido!")

            self.frameTela_Login.destroy()

            self.telaHome()

        else:
            print("Falha na autenticação do admin.")
            messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")
        '''

    def bt_frameLogin_esqueceu(self):
        print("Esqueceu a Senha")
        #messagebox.showinfo("iiiiiii","Esqueceu a Senha!!!")
        self.re=messagebox.askyesno("iiiiiii","Esqueceu a Senha!!!")
        print(self.re)

    def bt_frameHome_sol(self):

        if (self.corFundo =='#0D1521'):

            self.corFundo='#7EA8E7'
            self.img_cadastro = PhotoImage(file='bt_Cadastro_claro.png')
            self.img_Aulas = PhotoImage(file='bt_Aulas_claro.png')
            self.img_Home = PhotoImage(file='bt_Home_claro.png')
            self.img_Relatorios = PhotoImage(file='bt_Relatorios_claro.png')
            self.img_Sol = PhotoImage(file='bt_Lua.png')
            self.img_log_out = PhotoImage(file='Log_out_claro.png')

            self.frameTela_Home.destroy()
            self.telaHome()
        else:
            self.corFundo ='#0D1521'
            self.img_cadastro = PhotoImage(file='bt_Cadastro.png')
            self.img_Aulas = PhotoImage(file='bt_Aulas.png')
            self.img_Home = PhotoImage(file='bt_Home.png')
            self.img_Relatorios = PhotoImage(file='bt_Relatorios.png')
            self.img_Sol = PhotoImage(file='bt_Sol.png')
            self.img_log_out = PhotoImage(file='Log_out.png')

            self.frameTela_Home.destroy()
            self.telaHome()

    def bt_frameHome_sair(self):
        self.frameTela_Home.destroy()
        self.telaLogin()

    def bt_frameUsuarios_sair(self):
        self.frameTela_Usuarios.destroy()
        self.telaLogin()

    def bt_FrameHome_Cadastro(self):
        #messagebox.showinfo("Sucesso", "Login bem-sucedido!")

        self.frameTela_Home.destroy()

        self.telaUsuarios()


#########fim tela home##############



#########tela Usuarios#################################

    def bt_FrameUsuario_Usuario(self):
        self.frameTela_Usuarios.destroy()
        self.telaUsuarios()

    def bt_FrameUsuario_Moradores(self):
        self.frameTela_Usuarios.destroy()
        self.telaMoradores()

    def bt_FrameUsuario_professores(self):
        self.frameTela_Usuarios.destroy()
        self.telaProfessores()

    def limpa_usuarios(self):
        self.codigo_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.nome_entry.delete(0, END)

    def variaveis_usuarios(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
    def OnDoubleClick_usuarios(self, event):
        #self.limpa_usuarios()
        self.listaUsuarios.selection()

        for n in self.listaUsuarios.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def add_usuarios(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def altera_usuarios(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ? """,
                            (self.nome, self.fone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def deleta_usuarios(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_cliente()
        self.select_lista()

    def lista_usuarios(self,):
        self.listaUsuarios.delete(*self.listaUsuarios.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro FROM administradores
            ORDER BY nome_completo ASC; """)
        for i in lista:
            self.listaUsuarios.insert("", END, values=i)
        self.desconecta_bd()
    def busca_Usuarios(self):
        self.conecta_bd()
        self.listaUsuarios.delete(*self.listaUsuarios.get_children())

        self.entry_Tab_usuario .insert(END, '%')
        nome =  self.entry_Tab_usuario .get()
        print(nome)
        self.cursor.execute(
            """  SELECT cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro FROM administradores
            WHERE nome_completo LIKE '%s' ORDER BY nome_completo ASC""" % nome)
        buscanome = self.cursor.fetchall()
        for i in buscanome:
            self.listaUsuarios.insert("", END, values=i)
        #self.limpa_usuarios()
        self.desconecta_bd()


###############tela Moradores###################
    def limpa_moradores(self):
        self.codigo_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.nome_entry.delete(0, END)

    def variaveis_moradores(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
    def OnDoubleClick_moradores(self, event):
        #self.limpa_usuarios()
        self.listaMoradores.selection()

        for n in self.listaMoradores.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def add_moradores(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def altera_moradores(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ? """,
                            (self.nome, self.fone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def deleta_moradores(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_cliente()
        self.select_lista()

    def lista_moradores(self,):
        self.listaMoradores.delete(*self.listaMoradores.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT matricula, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo, responsavel_nome, responsavel_cpf, documento_permissao, profissao, tipo_necessidade, grau_necessidade
            FROM moradores
            ORDER BY nome_completo ASC; """)
        for i in lista:
            self.listaMoradores.insert("", END, values=i)
        self.desconecta_bd()
    def busca_moradores(self):
        self.conecta_bd()
        self.listaMoradores.delete(*self.listaMoradores.get_children())

        self.entry_Tab_moradores .insert(END, '%')
        nome =  self.entry_Tab_moradores .get()
        print(nome)
        self.cursor.execute(
            """  SELECT matricula, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo, responsavel_nome, responsavel_cpf, documento_permissao, profissao, tipo_necessidade, grau_necessidade
            FROM moradores
            WHERE nome_completo LIKE '%s' ORDER BY nome_completo ASC""" % nome)
        buscanome = self.cursor.fetchall()
        for i in buscanome:
            self.listaMoradores.insert("", END, values=i)
        #self.limpa_usuarios()
        self.desconecta_bd()


##########tela professores#########
    def limpa_professores(self):
        self.codigo_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.nome_entry.delete(0, END)

    def variaveis_professores(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
    def OnDoubleClick_professores(self, event):
        #self.limpa_usuarios()
        self.listaProfessores.selection()

        for n in self.listaProfessores.selection():
            col1, col2, col3, col4 = self.listaProfessores.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def add_professores(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def altera_professores(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ? """,
                            (self.nome, self.fone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def deleta_professores(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_cliente()
        self.select_lista()

    def lista_professores(self,):
        self.listaProfessores.delete(*self.listaProfessores.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email, data_cadastro FROM professores
            ORDER BY nome_completo ASC; """)
        for i in lista:
            self.listaProfessores.insert("", END, values=i)
        self.desconecta_bd()
    def busca_professores(self):
        self.conecta_bd()
        self.listaProfessores.delete(*self.listaProfessores.get_children())

        self.entry_Tab_professores .insert(END, '%')
        nome =  self.entry_Tab_professores .get()
        print(nome)
        self.cursor.execute(
            """  SELECT cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email, data_cadastro FROM professores
            WHERE nome_completo LIKE '%s' ORDER BY nome_completo ASC""" % nome)
        buscanome = self.cursor.fetchall()
        for i in buscanome:
            self.listaProfessores.insert("", END, values=i)
        #self.limpa_usuarios()
        self.desconecta_bd()


######################################################################################


class Telas(Funçao):
    
    def __init__(self):

        self.root = root

        self.telaInicial()

        root.mainloop()

    def telaInicial(self):
      
        #tela inicial
        #self.root.attributes('-zoomed',True)     ################ maximizar Tela
        self.root.title("AMAPE",)
        self.root.configure(background= self.corFundo)        
        self.root.minsize(width=1024, height=600)
        self.telaLogin()
        #self.telaHome()
       # self.telaUsuarios()
            
    def telaLogin(self):

        self.frameTela_Login=Frame(self.root,bg= '#0D1521')
        self.frameTela_Login.place(relheight=1,relwidth=1)
        #--------------------------------------------------------------------------------------------------------------------------------------------
        #label login
        self.lb_nome = Label(self.frameTela_Login, text="LOGIN", font = ('arial', 58, 'bold'), bg= '#0D1521')
        self.lb_nome.pack(anchor='center',pady=45,)

        #frames login
        self.frame_usuario=Frame(self.frameTela_Login,bg= '#0D1521')
        self.frame_usuario.place(relx= 0.2, rely=0.3,height=65,relwidth=0.5)

        self.frame_senha=Frame(self.frameTela_Login,bg= '#0D1521')
        self.frame_senha.place(relx= 0.2, rely=0.5,height=65,relwidth=0.5)


        #icones em convertidos em base64 para evitar erro.
        self.img_usuario = PhotoImage(data=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAABApJREFUeJztms1rH0UYx79Pg220LwiCEWpsJK0trY2CBQ8WxNb24KFU6L/QN1/w7sGDlJ4UBLUWwT/CUzWperEgimhjBFtobRELKbSkpia/JISPh0lEfua3M7szu9PQ/Vxn9rvP99nZnZln1tQQwCZJ+yUdlDQiaUjSY5LuSFqQdEnSr5JGJX1hZrNNxVYrwFbgI+Au4UwDZ4DB3PFXBugH3gXmShjvpgOcBtbm9lMK4AlgPMJ4Nz8Cw7l9BQGMADcSml/mBrAzt79CcE/+zxrMLzMJbMntc0Vw73zKYd+LH4D+VHGvSSUk6W1JuxPq9WKPpHcauE84uKku9Gv/M/AasAN4EFgP7ALeAn4J1JgFhnL7/hfcPO9jBjgB9Bx1QB/wemAyzzTpsSfAJvyLnBngxRKa+wKSMAU8VKe30GBfDXhaxyvovhGge6QOT2UD/cQT5EXAKuj2ARMe7Q9i408xC4x42j81M8qKmtmipM883Z4vq9tNigQMedrPR2iPedo3R2hLkkoPzW6AjqR1BV36zWyuovZGSX8VdJkxs/VVtJdJMQIWEmj0YtHT3hd7gxQJmPG0Pxmh7bt2KkJbUpoEXPa074vQ9l17NUJbUpoETHjaj1Ow+uvF0jXHPN0ultXtJkUCRj3tI5JKL4QknZT0tKfPVxV004Lb0Ex7Fiwd4KUSmvuXriliGoiaAZKBK2D66AAni14HYA1uMzQboHe2SY+FAIMBT2yZcdw6fyeuiLIBtx1+k/DtcId7aTssSbjqbVOcyu33fwAPAN83YP4CULTyzAcwTL1F0WvAo7l9FoJ7tydrMH8d2JXbXxDA48B3Cc1fAAZy+yoF7gt/mrAprRcd4BSr7WjsvwBbcOuEqRLGp4GzNDDVRdcDQsEVMF+RtFeukrNZ0iNyW9o7chubnyR9Lemcmf3dVGwtLS0t9y1JZgHgYbmfn7ZLGpBU13L1pqRJSb9JGjOz6JpgFMBBYBSYj1jsVGV+6d4Hchh/ChjLYLoXXwJbmzJ/ALid2fBK3AJertv8YWAhs9EiFoBDZTwFfwSBZyR9K2lD2cQ1zF1JL5jZeEjnoATgdmMTkrZFBNYklyTtNjPvsV3oucAJrR7zkpuOj4Z09I6Apaf/h/xz+6KkzyV9IzdX18GA3HHZIfkPRiclDYaMgkJwc72PK4DvR4lkAM8CVwPiip8VgI89N7kNxJwAV41rGH+R5UOfTsg34DlP+3tm9ntY2OkwsyuS3vd088XuB1eNLWJ79E2qx7bDE9s1n0bIR3BOUlFRcp2ZzZeIOxm4D3TR7zfzZlZ4iBKSgMI/vMyssbriSsTGl/Jn6VVJm4DcAeSmTUDuAHLTJiB3ALlpE5A7gNy0CcgdQG7u+wT8A2lUGKvItXv5AAAAAElFTkSuQmCC'))
        self.img_senha = PhotoImage(data=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAABOpJREFUeJztm9urFlUYh5/laWtqdBYrUSksMcPIENSozBILUyrpQqKgQIISMiqKotsuyptuKiP8A6KTZVESCbUpyrK9tegkWlDtoIOpbY/76WK2ZjrzrfXNN998ij2Xa63vt37vu/fMrPWumUBNqJcA84HZwBRgAjB2sHsn8CPwNdANrA8hbKnLW9tQR6sr1F6bp0e9Tz2l03E0jTpEvUf9tUTgR9OnLleHdDquJNRJancFgR/Nh+rETsfXEPVq9fc2BH+I39SrOh1nLuqNan8bgz9Ev3pDp+P9D+pc9e8agj/EbnV2Fd5DBcGPAz4Hxrdupyn6gBkhhF9aEakiAeuAhYnD+4G3gNeBzcDPg+3jgenAokGtUYl6b4QQFqW7rRj1lsR/2QPqc+q5CZrnqavVg4nai+uINc/oEHVzgsGdZUyqC9U/E/S32Ik1gro4wdwu9fIW5phpdsOLUf9loL6aYOzWCua5LWGel6uIqRlTY9S9EVNrK5xvXWSuPda5Z1AXJPxVLq1wvhkJ811XRrvszeOKSH9vCKGnpPYxhBA2AV9Ghs0so102AVMi/etK6jbizUj/RWVEyyZgXKT/25K6jfgu0n9OGdGyCRgd6e8rqduInyL9p5YRLZuAYZH+PSV1W9GMecrlxKiytJFSWUvgFXV/xZrDK9YDSiRA7SJ+vY0pZ6clTlW7Qgh7m/lRU5eAOh/oBaY287uamAr0qNdWrqwG9WHTt6idZEB90ip3iOrTHQ6qDM9UFfxjnY6kBR6NxdewJKbOATYAQyvJZv0MAPNCCBuKBhQmQB1GdsO7uA3G6uQrYHoI4WBeZ6PH4B2kBd8PrAHWAtuAph5DJegCJgE3AXcCIyPjpwK3k3lMR92UcI11qxOaDqEi1InqRwk+P21WeFqC6Mdqavm6baij1E8S/OauXYqelfMi8+4HloUQ+ltyXwGDHpaReWrENXmNRQmIVXxeCiHE9ue1EUL4BogVRnNjKkrA+RGxt2OmOkDMU+69qigBp0fEtkft1M+2SP+ZeY1FCRgREWtHwaNVYvej3JjaVQ8oRJ0J3E92GHqotLYb6AFWhRA+q9vTMZidtzViVkndm9V9DXT3qktKas+KeM5966y2kpg6BlhN48rOCGC1Giu6VkadNcErgTMSxp0FzG2zl8PUmYBmymRj40Oqoc4EbARMGDcANLd2b4HaEhBC2Aq8kDD0+RDCtjbbOUzd5wL3AqvI3zLvAZ4CVtRpqNZ1QAhhH/CA+gRwIf9Wmg4A34cQdtXpBzqwEAIYDHRTJ+Y+mpP+aOz/BBS05xYQj6CraiMVEPN0IK+xKAF/RcQ6VgdsQOxV+h15jUUJiO33F0Tt1M/1kf5teY1FCYitxJZ6HH28oE4GlkaGbWxGcFJClfUDs6PyjqIOV99P8Du5WeGeBNF31bPbFFuKx3Hqewk+C9ccjY7G7ibbv8fYATxLdjK0lfaXy0YCF5CdDC0n7eWou0IIL+Z1NErAUOALYFoJk8cTvcBlRWeDhQuhwR+sJNuenqgMACuLgofISjCE8A7weNWuauSREML6lhTMXo9Zk3CjOd7IveZbScLJ+47QEYlYov7Q2fgast12f0Nkdhz9kNV8F1wVfeqDauxliWMo/dmc2WNyDtnzeDbZs/k04sdqrbIP+INszdENvAZ0N7rTN+IfINN/ij5RpEEAAAAASUVORK5CYII='))
       
        self.ico_usuario = Label(self.frame_usuario,image=self.img_usuario,  bg= '#0D1521')
        self.ico_usuario.place(relx=0, rely=0,)

        self.ico_senha = Label(self.frame_senha,image=self.img_senha,  bg= '#0D1521')
        self.ico_senha.place(relx=0, rely=0)

        
        #entry login
        self.usuario_entry = Entry(self.frame_usuario, font = ('verdana', 20, 'bold'))
        self.usuario_entry.place(relx=0.2, rely=0, relwidth=0.9,relheight=1)

        self.senha_entry = Entry(self.frame_senha,font = ('verdana', 20, 'bold'),show='*')
        self.senha_entry.place(relx=0.2, rely=0,relwidth=0.9,relheight=1)

        #botoes login
        self.bt_entrar = Button(self.frameTela_Login, text= "ENTRAR", bd=2, bg = '#6634cb',fg = 'white',activebackground='#8b67d5', activeforeground="white", font = ('verdana', 20, 'bold'),command=self.bt_FrameLogin_entrar)
        self.bt_entrar.place(relx= 0.3, rely=0.7, relwidth=0.4, relheight= 0.15)


        self.bt_esqueceu = Button(self.frameTela_Login, text= "Esqueceu a Senha ?", bd=0, bg = '#0D1521',fg = 'white',highlightthickness=0,activebackground='#0D1521', activeforeground="#8b67d5", font = ('verdana', 12, 'bold'),command=self.bt_frameLogin_esqueceu)
        self.bt_esqueceu.place(relx= 0.3, rely=0.9, relwidth=0.4, relheight= 0.04)
        #-------------------------------------------------------------------------------------------------------------------------------------

    def telaHome(self):

        self.frameTela_Home=Frame(self.root,bg =self.corFundo)#0D1521
        self.frameTela_Home.place(relheight=1,relwidth=1)
        #--------------------------------------------------------------------------------------------------------------------------------------------
        #botoes 

        self.bt_Home = Button(self.frameTela_Home,image=self.img_Home, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_Home.place(relx= 0, rely=0, relwidth=0.09, relheight= 0.2)

        self.bt_Cadastro = Button(self.frameTela_Home,image=self.img_cadastro, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0,command=self.bt_FrameHome_Cadastro)
        self.bt_Cadastro.place(relx= 0.1, rely=0, relwidth=0.2, relheight= 0.2)

        self.bt_Aulas = Button(self.frameTela_Home,image=self.img_Aulas, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_Aulas.place(relx= 0.31, rely=0, relwidth=0.2, relheight= 0.2)
        
        self.bt_Relatorios = Button(self.frameTela_Home,image=self.img_Relatorios, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_Relatorios.place(relx= 0.52, rely=0, relwidth=0.2, relheight= 0.2)

        self.bt_Sol = Button(self.frameTela_Home,image=self.img_Sol, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0,command=self.bt_frameHome_sol)
        self.bt_Sol.place(relx= 0.73, rely=0, relwidth=0.09, relheight= 0.2)

        self.bt_Avatar = Button(self.frameTela_Home,image=self.img_avatar, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_Avatar.place(relx= 0.82, rely=0, relwidth=0.09, relheight= 0.2)

        self.bt_Sair = Button(self.frameTela_Home,image=self.img_log_out, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0,command=self.bt_frameHome_sair)
        self.bt_Sair.place(relx= 0.91, rely=0, relwidth=0.09, relheight= 0.2)
      
        #LOGO
        self.bt_LOGO = Button(self.frameTela_Home,image=self.img_LOGO, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)#activebackground='#0D1521',
        self.bt_LOGO.place(relx=0.28,rely=0.48,relwidth=0.43,relheight=0.2)
              
        #-------------------------------------------------------------------------------------------------------------------------------------

    def telaUsuarios(self):
        self.frameTela_Usuarios=Frame(self.root,bg =self.corFundo)#0D1521
        self.frameTela_Usuarios.place(relheight=1,relwidth=1)
        #--------------------------------------------------------------------------------------------------------------------------------------------
        #botoes superior

        self.bt_Home = Button(self.frameTela_Usuarios,image=self.img_Home, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_Home.place(relx= 0, rely=0, relwidth=0.09, relheight= 0.2)

        self.bt_Moradores = Button(self.frameTela_Usuarios,image=self.img_Moradores, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0,command=self.bt_FrameUsuario_Moradores)
        self.bt_Moradores.place(relx= 0.1, rely=0, relwidth=0.2, relheight= 0.2)

        self.bt_Professores = Button(self.frameTela_Usuarios,image=self.img_Professores, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0,command=self.bt_FrameUsuario_professores)
        self.bt_Professores.place(relx= 0.31, rely=0, relwidth=0.2, relheight= 0.2)
        
        self.bt_Usuarios = Button(self.frameTela_Usuarios,image=self.img_Usuarios, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0,command=self.bt_FrameUsuario_Usuario)
        self.bt_Usuarios.place(relx= 0.52, rely=0, relwidth=0.2, relheight= 0.2)

        self.bt_Sol = Button(self.frameTela_Usuarios,image=self.img_Sol, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0,command=self.bt_frameHome_sol)
        self.bt_Sol.place(relx= 0.73, rely=0, relwidth=0.09, relheight= 0.2)

        self.bt_Avatar = Button(self.frameTela_Usuarios,image=self.img_avatar, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_Avatar.place(relx= 0.82, rely=0, relwidth=0.09, relheight= 0.2)

        self.bt_Sair = Button(self.frameTela_Usuarios,image=self.img_log_out, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0,command=self.bt_frameUsuarios_sair)
        self.bt_Sair.place(relx= 0.91, rely=0, relwidth=0.09, relheight= 0.2)

        self.label_TabelaUsuarios=Label(self.frameTela_Usuarios, text="Tabela Usuarios",font =('arial', 28, 'bold'),fg =self.cor_texto_titulo,bg =self.corFundo)
        self.label_TabelaUsuarios.place(relx=0.35,rely=0.2,relwidth=0.29,relheight=0.06)

        #--------------------------------------------------------------------------------------------------------------------------------------------
        #botoes da tabela

        self.bt_UserAdd = Button(self.frameTela_Usuarios,image=self.img_UserAdd,bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_UserAdd.place(relx= 0.02, rely=0.26, relwidth=0.06, relheight= 0.09)

        self.bt_Edit = Button(self.frameTela_Usuarios,image=self.img_Edit,bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_Edit.place(relx= 0.1, rely=0.26, relwidth=0.06, relheight= 0.09)

        self.bt_Lixeira = Button(self.frameTela_Usuarios,image=self.img_Lixeira,bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_Lixeira.place(relx= 0.18, rely=0.26, relwidth=0.06, relheight= 0.09)

        self.bt_Refresh = Button(self.frameTela_Usuarios,image=self.img_Refresh,bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0,command=self.bt_FrameUsuario_Usuario)
        self.bt_Refresh.place(relx= 0.26, rely=0.26, relwidth=0.06, relheight= 0.09)

        self.bt_Printer = Button(self.frameTela_Usuarios,image=self.img_Printer,bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_Printer.place(relx= 0.34, rely=0.26, relwidth=0.06, relheight= 0.09)

        self.bt_Search = Button(self.frameTela_Usuarios,image=self.img_Search,highlightthickness=0,border=0,command=self.busca_Usuarios)
        self.bt_Search.place(relx= 0.9, rely=0.26, relwidth=0.06, relheight= 0.09)

        self.entry_Tab_usuario = Entry(self.frameTela_Usuarios,highlightthickness=0,border=0,font = ('verdana', 28, 'bold'),fg=self.cor_texto_pesquisa)
        self.entry_Tab_usuario.place(relx= 0.5, rely=0.26, relwidth=0.4, relheight= 0.09)
      
        #########################################################################################
        #listagem tabela

        self.frame_2 = Frame(self.frameTela_Usuarios, bd=4, bg='grey')
        self.frame_2.place(relx=0.01, rely=0.37, relwidth=0.98, relheight=0.6)

        self.listaUsuarios = ttk.Treeview(self.frame_2, height=3,column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8","col9"))

        self.listaUsuarios.heading("#0", text="")
        self.listaUsuarios.heading("#1", text="CPF")
        self.listaUsuarios.heading("#2", text="Nome")
        self.listaUsuarios.heading("#3", text="Data Nascimento")
        self.listaUsuarios.heading("#4", text="Endereço")
        self.listaUsuarios.heading("#5", text="Telefone")
        self.listaUsuarios.heading("#6", text="Email")
        self.listaUsuarios.heading("#7", text="Nome Usuario")
        self.listaUsuarios.heading("#8", text="Senha")
        self.listaUsuarios.heading("#9",text="Data Cadastro")
        self.listaUsuarios.column("#0", width=0)
        self.listaUsuarios.column("#1", width=125)
        self.listaUsuarios.column("#2", width=200)
        self.listaUsuarios.column("#3", width=150)
        self.listaUsuarios.column("#4", width=200)
        self.listaUsuarios.column("#5", width=125)
        self.listaUsuarios.column("#6", width=200)
        self.listaUsuarios.column("#7", width=125)
        self.listaUsuarios.column("#8", width=125)
        self.listaUsuarios.column("#9", width=200)
        self.listaUsuarios.place(relx=0, rely=0, relwidth=0.98, relheight=0.95)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')        
        self.scroolLista.place(relx=0.98, rely=0, relwidth=0.02, relheight=1)

        self.scroolLista2 = Scrollbar(self.frame_2, orient='horizontal',relief="solid")
        self.scroolLista2.place(relx=0, rely=0.95, relwidth=0.98, relheight=0.05)

        self.listaUsuarios.configure(xscrollcommand=self.scroolLista2.set,yscrollcommand=self.scroolLista.set)
        self.scroolLista.config(command=self.listaUsuarios.yview)
        self.scroolLista2.config(command=self.listaUsuarios.xview)

        self.listaUsuarios.bind("<Double-1>", self.OnDoubleClick_usuarios(self))


        #stylo tabela

        style=ttk.Style()
        style.theme_use('default')
        style.configure("Treeview",background='grey',foreground=self.cor_texto_titulo,rowheight=25,fieldbackground=self.corFundo)
        style.map(self.listaUsuarios,"Treeview", background=[('select','red')])

        self.lista_usuarios()

              
        #-------------------------------------------------------------------------------------------------------------------------------------

    def telaMoradores(self):
        self.frameTela_Moradores = Frame(self.root, bg=self.corFundo)  # 0D1521
        self.frameTela_Moradores.place(relheight=1, relwidth=1)
        # --------------------------------------------------------------------------------------------------------------------------------------------
        # botoes superior

        self.bt_Home = Button(self.frameTela_Moradores, image=self.img_Home, bg=self.corFundo,
                          activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Home.place(relx=0, rely=0, relwidth=0.09, relheight=0.2)

        self.bt_Moradores = Button(self.frameTela_Moradores, image=self.img_Moradores, bg=self.corFundo,
                               activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Moradores.place(relx=0.1, rely=0, relwidth=0.2, relheight=0.2)

        self.bt_Professores = Button(self.frameTela_Moradores, image=self.img_Professores, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Professores.place(relx=0.31, rely=0, relwidth=0.2, relheight=0.2)

        self.bt_Usuarios = Button(self.frameTela_Moradores, image=self.img_Usuarios, bg=self.corFundo,
                              activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Usuarios.place(relx=0.52, rely=0, relwidth=0.2, relheight=0.2)

        self.bt_Sol = Button(self.frameTela_Moradores, image=self.img_Sol, bg=self.corFundo, activebackground=self.corFundo,
                         highlightthickness=0, border=0, command=self.bt_frameHome_sol)
        self.bt_Sol.place(relx=0.73, rely=0, relwidth=0.09, relheight=0.2)

        self.bt_Avatar = Button(self.frameTela_Moradores, image=self.img_avatar, bg=self.corFundo,
                            activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Avatar.place(relx=0.82, rely=0, relwidth=0.09, relheight=0.2)

        self.bt_Sair = Button(self.frameTela_Moradores, image=self.img_log_out, bg=self.corFundo,
                          activebackground=self.corFundo, highlightthickness=0, border=0,
                          command=self.bt_frameUsuarios_sair)
        self.bt_Sair.place(relx=0.91, rely=0, relwidth=0.09, relheight=0.2)

        self.label_TabelaMoradores = Label(self.frameTela_Moradores, text="Tabela Moradores", font=('arial', 28, 'bold'),
                                      fg=self.cor_texto_titulo, bg=self.corFundo)
        self.label_TabelaMoradores.place(relx=0.35, rely=0.2, relwidth=0.32, relheight=0.06)

    # --------------------------------------------------------------------------------------------------------------------------------------------
    # botoes da tabela

        self.bt_UserAdd = Button(self.frameTela_Moradores, image=self.img_UserAdd, bg=self.corFundo,
                             activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_UserAdd.place(relx=0.02, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Edit = Button(self.frameTela_Moradores, image=self.img_Edit, bg=self.corFundo,
                          activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Edit.place(relx=0.1, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Lixeira = Button(self.frameTela_Moradores, image=self.img_Lixeira, bg=self.corFundo,
                             activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Lixeira.place(relx=0.18, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Refresh = Button(self.frameTela_Moradores, image=self.img_Refresh, bg=self.corFundo,
                             activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Refresh.place(relx=0.26, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Printer = Button(self.frameTela_Moradores, image=self.img_Printer, bg=self.corFundo,
                             activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Printer.place(relx=0.34, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Search = Button(self.frameTela_Moradores, image=self.img_Search, highlightthickness=0, border=0,
                            command=self.busca_moradores)
        self.bt_Search.place(relx=0.9, rely=0.26, relwidth=0.06, relheight=0.09)

        self.entry_Tab_moradores = Entry(self.frameTela_Moradores, highlightthickness=0, border=0,
                                   font=('verdana', 28, 'bold'), fg=self.cor_texto_pesquisa)
        self.entry_Tab_moradores.place(relx=0.5, rely=0.26, relwidth=0.4, relheight=0.09)

    #########################################################################################
    # listagem tabela

        self.frame_2 = Frame(self.frameTela_Moradores, bd=4, bg='grey')
        self.frame_2.place(relx=0.01, rely=0.37, relwidth=0.98, relheight=0.6)

        self.listaMoradores = ttk.Treeview(self.frame_2, height=3,
                                 column=( "matricula", "cpf", "nome_completo", "filiacao", "data_nascimento", "endereco", "telefone", "email","tipo", "responsavel_nome", "responsavel_cpf", "documento_permissao", "profissao", "tipo_necessidade", "grau_necessidade"))

        self.listaMoradores.heading("#0", text="")
        self.listaMoradores.heading("#1", text="Matricula")
        self.listaMoradores.heading("#2", text="CPF")
        self.listaMoradores.heading("#3", text="Nome")
        self.listaMoradores.heading("#4", text="Filiaçao")
        self.listaMoradores.heading("#5", text="Data Nascimento")
        self.listaMoradores.heading("#6", text="Endereço")
        self.listaMoradores.heading("#7", text="Telefone")
        self.listaMoradores.heading("#8", text="Email")
        self.listaMoradores.heading("#9", text="Tipo")
        self.listaMoradores.heading("#10", text="Nome Responsavel")
        self.listaMoradores.heading("#11", text="CPF Responsavel")
        self.listaMoradores.heading("#12", text="Documento Permissao")
        self.listaMoradores.heading("#13", text="Profissao")
        self.listaMoradores.heading("#14", text="Tipo Necessidade")
        self.listaMoradores.heading("#15", text="Grau de Necessidade")
        self.listaMoradores.column("#0", width=0)
        self.listaMoradores.column("#1", width=200)
        self.listaMoradores.column("#2", width=150)
        self.listaMoradores.column("#3", width=200)
        self.listaMoradores.column("#4", width=200)
        self.listaMoradores.column("#5", width=150)
        self.listaMoradores.column("#6", width=200)
        self.listaMoradores.column("#7", width=200)
        self.listaMoradores.column("#8", width=200)
        self.listaMoradores.column("#9", width=200)
        self.listaMoradores.column("#10", width=200)
        self.listaMoradores.column("#11", width=200)
        self.listaMoradores.column("#12", width=200)
        self.listaMoradores.column("#13", width=200)
        self.listaMoradores.column("#14", width=200)
        self.listaMoradores.column("#15", width=200)
        self.listaMoradores.place(relx=0, rely=0, relwidth=0.98, relheight=0.95)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.scroolLista.place(relx=0.98, rely=0, relwidth=0.02, relheight=1)

        self.scroolLista2 = Scrollbar(self.frame_2, orient='horizontal', relief="solid")
        self.scroolLista2.place(relx=0, rely=0.95, relwidth=0.98, relheight=0.05)

        self.listaMoradores.configure(xscrollcommand=self.scroolLista2.set, yscrollcommand=self.scroolLista.set)
        self.scroolLista.config(command=self.listaMoradores.yview)
        self.scroolLista2.config(command=self.listaMoradores.xview)

        self.listaMoradores.bind("<Double-1>", self.OnDoubleClick_moradores)

    # stylo tabela

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background='grey', foreground=self.cor_texto_titulo, rowheight=25,
                    fieldbackground=self.corFundo)
        style.map(self.listaMoradores, "Treeview", background=[('select', 'red')])


        self.lista_moradores()

        # -------------------------------------------------------------------------------------------------------------------------------------

    def telaProfessores(self):
        self.frameTela_Professores = Frame(self.root, bg=self.corFundo)  # 0D1521
        self.frameTela_Professores.place(relheight=1, relwidth=1)
        # --------------------------------------------------------------------------------------------------------------------------------------------
        # botoes superior

        self.bt_Home = Button(self.frameTela_Professores, image=self.img_Home, bg=self.corFundo,
                              activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Home.place(relx=0, rely=0, relwidth=0.09, relheight=0.2)

        self.bt_Moradores = Button(self.frameTela_Professores, image=self.img_Moradores, bg=self.corFundo,
                                   activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Moradores.place(relx=0.1, rely=0, relwidth=0.2, relheight=0.2)

        self.bt_Professores = Button(self.frameTela_Professores, image=self.img_Professores, bg=self.corFundo,
                                     activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Professores.place(relx=0.31, rely=0, relwidth=0.2, relheight=0.2)

        self.bt_Usuarios = Button(self.frameTela_Professores, image=self.img_Usuarios, bg=self.corFundo,
                                  activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Usuarios.place(relx=0.52, rely=0, relwidth=0.2, relheight=0.2)

        self.bt_Sol = Button(self.frameTela_Professores, image=self.img_Sol, bg=self.corFundo,
                             activebackground=self.corFundo, highlightthickness=0, border=0,
                             command=self.bt_frameHome_sol)
        self.bt_Sol.place(relx=0.73, rely=0, relwidth=0.09, relheight=0.2)

        self.bt_Avatar = Button(self.frameTela_Professores, image=self.img_avatar, bg=self.corFundo,
                                activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Avatar.place(relx=0.82, rely=0, relwidth=0.09, relheight=0.2)

        self.bt_Sair = Button(self.frameTela_Professores, image=self.img_log_out, bg=self.corFundo,
                              activebackground=self.corFundo, highlightthickness=0, border=0,
                              command=self.bt_frameUsuarios_sair)
        self.bt_Sair.place(relx=0.91, rely=0, relwidth=0.09, relheight=0.2)

        self.label_TabelaProfessores = Label(self.frameTela_Professores, text="Tabela Professores", font=('arial', 28, 'bold'),
                                          fg=self.cor_texto_titulo, bg=self.corFundo)
        self.label_TabelaProfessores.place(relx=0.35, rely=0.2, relwidth=0.35, relheight=0.06)

        # --------------------------------------------------------------------------------------------------------------------------------------------
        # botoes da tabela

        self.bt_UserAdd = Button(self.frameTela_Professores, image=self.img_UserAdd, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_UserAdd.place(relx=0.02, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Edit = Button(self.frameTela_Professores, image=self.img_Edit, bg=self.corFundo,
                              activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Edit.place(relx=0.1, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Lixeira = Button(self.frameTela_Professores, image=self.img_Lixeira, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Lixeira.place(relx=0.18, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Refresh = Button(self.frameTela_Professores, image=self.img_Refresh, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Refresh.place(relx=0.26, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Printer = Button(self.frameTela_Professores, image=self.img_Printer, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Printer.place(relx=0.34, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Search = Button(self.frameTela_Professores, image=self.img_Search, highlightthickness=0, border=0,
                                command=self.busca_professores)
        self.bt_Search.place(relx=0.9, rely=0.26, relwidth=0.06, relheight=0.09)

        self.entry_Tab_professores = Entry(self.frameTela_Professores, highlightthickness=0, border=0,
                                       font=('verdana', 28, 'bold'), fg=self.cor_texto_pesquisa)
        self.entry_Tab_professores.place(relx=0.5, rely=0.26, relwidth=0.4, relheight=0.09)

        #########################################################################################
        # listagem tabela

        self.frame_2 = Frame(self.frameTela_Professores, bd=4, bg='grey')
        self.frame_2.place(relx=0.01, rely=0.37, relwidth=0.98, relheight=0.6)

        self.listaProfessores = ttk.Treeview(self.frame_2, height=3, column=("cpf", "nome_completo", "especialidade", "data_nascimento", "endereco", "telefone", "email", "data_cadastro"))

        self.listaProfessores.heading("#0", text="")
        self.listaProfessores.heading("#1", text="CPF")
        self.listaProfessores.heading("#2", text="Nome")
        self.listaProfessores.heading("#3", text="Especialidade")
        self.listaProfessores.heading("#4", text="Data Nascimento")
        self.listaProfessores.heading("#5", text="Endereço")
        self.listaProfessores.heading("#6", text="Telefone")
        self.listaProfessores.heading("#7", text="Email")
        self.listaProfessores.heading("#8", text="Data Cadastro")
        self.listaProfessores.column("#0", width=0)
        self.listaProfessores.column("#1", width=150)
        self.listaProfessores.column("#2", width=200)
        self.listaProfessores.column("#3", width=200)
        self.listaProfessores.column("#4", width=200)
        self.listaProfessores.column("#5", width=200)
        self.listaProfessores.column("#6", width=200)
        self.listaProfessores.column("#7", width=200)
        self.listaProfessores.column("#8", width=200)

        self.listaProfessores.place(relx=0, rely=0, relwidth=0.98, relheight=0.95)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.scroolLista.place(relx=0.98, rely=0, relwidth=0.02, relheight=1)

        self.scroolLista2 = Scrollbar(self.frame_2, orient='horizontal', relief="solid")
        self.scroolLista2.place(relx=0, rely=0.95, relwidth=0.98, relheight=0.05)

        self.listaProfessores.configure(xscrollcommand=self.scroolLista2.set, yscrollcommand=self.scroolLista.set)
        self.scroolLista.config(command=self.listaProfessores.yview)
        self.scroolLista2.config(command=self.listaProfessores.xview)

        self.listaProfessores.bind("<Double-1>", self.OnDoubleClick_professores)

        # stylo tabela

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background='grey', foreground=self.cor_texto_titulo, rowheight=25,
                        fieldbackground=self.corFundo)
        style.map(self.listaProfessores, "Treeview", background=[('select', 'red')])

        self.lista_professores()
        # -------------------------------------------------------------------------------------------------------------------------------------

    def telaAulas(self):
        self.frameTela_Aulas = Frame(self.root, bg=self.corFundo)  # 0D1521
        self.frameTela_Aulas.place(relheight=1, relwidth=1)
        # --------------------------------------------------------------------------------------------------------------------------------------------
        # botoes superior

        self.bt_Home = Button(self.frameTela_Aulas, image=self.img_Home, bg=self.corFundo,
                              activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Home.place(relx=0, rely=0, relwidth=0.09, relheight=0.2)



        self.bt_Aulas = Button(self.frameTela_Aulas, image=self.img_Professores, bg=self.corFundo,
                                     activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Aulas.place(relx=0.31, rely=0, relwidth=0.2, relheight=0.2)

        self.bt_Alunos = Button(self.frameTela_Aulas, image=self.img_Usuarios, bg=self.corFundo,
                                  activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Alunos.place(relx=0.52, rely=0, relwidth=0.2, relheight=0.2)

        self.bt_Sol = Button(self.frameTela_Aulas, image=self.img_Sol, bg=self.corFundo,
                             activebackground=self.corFundo, highlightthickness=0, border=0,
                             command=self.bt_frameHome_sol)
        self.bt_Sol.place(relx=0.73, rely=0, relwidth=0.09, relheight=0.2)

        self.bt_Avatar = Button(self.frameTela_Aulas, image=self.img_avatar, bg=self.corFundo,
                                activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Avatar.place(relx=0.82, rely=0, relwidth=0.09, relheight=0.2)

        self.bt_Sair = Button(self.frameTela_Aulas, image=self.img_log_out, bg=self.corFundo,
                              activebackground=self.corFundo, highlightthickness=0, border=0,
                              command=self.bt_frameUsuarios_sair)
        self.bt_Sair.place(relx=0.91, rely=0, relwidth=0.09, relheight=0.2)

        self.label_TabelaAulas = Label(self.frameTela_Aulas, text="Tabela Aulas", font=('arial', 28, 'bold'),
                                          fg=self.cor_texto_titulo, bg=self.corFundo)
        self.label_TabelaAulas.place(relx=0.35, rely=0.2, relwidth=0.29, relheight=0.06)

        # --------------------------------------------------------------------------------------------------------------------------------------------
        # botoes da tabela

        self.bt_UserAdd = Button(self.frameTela_Aulas, image=self.img_UserAdd, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_UserAdd.place(relx=0.02, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Edit = Button(self.frameTela_Aulas, image=self.img_Edit, bg=self.corFundo,
                              activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Edit.place(relx=0.1, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Lixeira = Button(self.frameTela_Aulas, image=self.img_Lixeira, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Lixeira.place(relx=0.18, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Refresh = Button(self.frameTela_Aulas, image=self.img_Refresh, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Refresh.place(relx=0.26, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Printer = Button(self.frameTela_Aulas, image=self.img_Printer, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Printer.place(relx=0.34, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Search = Button(self.frameTela_Aulas, image=self.img_Search, highlightthickness=0, border=0,
                                command=self.busca_Usuario)
        self.bt_Search.place(relx=0.9, rely=0.26, relwidth=0.06, relheight=0.09)

        self.entry_Tab_aulas = Entry(self.frameTela_Aulas, highlightthickness=0, border=0,
                                       font=('verdana', 28, 'bold'), fg=self.cor_texto_pesquisa)
        self.entry_Tab_aulas.place(relx=0.5, rely=0.26, relwidth=0.4, relheight=0.09)

        #########################################################################################
        # listagem tabela

        self.frame_2 = Frame(self.frameTela_Aulas, bd=4, bg='grey')
        self.frame_2.place(relx=0.01, rely=0.37, relwidth=0.98, relheight=0.6)

        self.listaAulas = ttk.Treeview(self.frame_2, height=3, column=(
        "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))

        self.listaAulas.heading("#0", text="")
        self.listaAulas.heading("#1", text="CPF")
        self.listaAulas.heading("#2", text="Nome")
        self.listaAulas.heading("#3", text="Data Nascimento")
        self.listaAulas.heading("#4", text="Endereço")
        self.listaAulas.heading("#5", text="Telefone")
        self.listaAulas.heading("#6", text="Email")
        self.listaAulas.heading("#7", text="Nome Usuario")
        self.listaAulas.heading("#8", text="Senha")
        self.listaAulas.heading("#9", text="Data Cadastro")
        self.listaAulas.column("#0", width=0)
        self.listaAulas.column("#1", width=125)
        self.listaAulas.column("#2", width=200)
        self.listaAulas.column("#3", width=150)
        self.listaAulas.column("#4", width=200)
        self.listaAulas.column("#5", width=125)
        self.listaAulas.column("#6", width=200)
        self.listaAulas.column("#7", width=125)
        self.listaAulas.column("#8", width=125)
        self.listaAulas.column("#9", width=200)
        self.listaAulas.place(relx=0, rely=0, relwidth=0.98, relheight=0.95)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.scroolLista.place(relx=0.98, rely=0, relwidth=0.02, relheight=1)

        self.scroolLista2 = Scrollbar(self.frame_2, orient='horizontal', relief="solid")
        self.scroolLista2.place(relx=0, rely=0.95, relwidth=0.98, relheight=0.05)

        self.listaAulas.configure(xscrollcommand=self.scroolLista2.set, yscrollcommand=self.scroolLista.set)
        self.scroolLista.config(command=self.listaAulas.yview)
        self.scroolLista2.config(command=self.listaAulas.xview)

        self.listaAulas.bind("<Double-1>", self.OnDoubleClick)

        # stylo tabela

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background='grey', foreground=self.cor_texto_titulo, rowheight=25,
                        fieldbackground=self.corFundo)
        style.map(self.listaAulas, "Treeview", background=[('select', 'red')])

        # -------------------------------------------------------------------------------------------------------------------------------------

    def telaAlunos(self):
        self.frameTela_Alunos = Frame(self.root, bg=self.corFundo)  # 0D1521
        self.frameTela_Alunos.place(relheight=1, relwidth=1)
        # --------------------------------------------------------------------------------------------------------------------------------------------
        # botoes superior

        self.bt_Home = Button(self.frameTela_Alunos, image=self.img_Home, bg=self.corFundo,
                              activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Home.place(relx=0, rely=0, relwidth=0.09, relheight=0.2)



        self.bt_Aulas = Button(self.frameTela_Alunos, image=self.img_Professores, bg=self.corFundo,
                                     activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Aulas.place(relx=0.31, rely=0, relwidth=0.2, relheight=0.2)

        self.bt_Alunos = Button(self.frameTela_Alunos, image=self.img_Usuarios, bg=self.corFundo,
                                  activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Alunos.place(relx=0.52, rely=0, relwidth=0.2, relheight=0.2)

        self.bt_Sol = Button(self.frameTela_Alunos, image=self.img_Sol, bg=self.corFundo,
                             activebackground=self.corFundo, highlightthickness=0, border=0,
                             command=self.bt_frameHome_sol)
        self.bt_Sol.place(relx=0.73, rely=0, relwidth=0.09, relheight=0.2)

        self.bt_Avatar = Button(self.frameTela_Alunos, image=self.img_avatar, bg=self.corFundo,
                                activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Avatar.place(relx=0.82, rely=0, relwidth=0.09, relheight=0.2)

        self.bt_Sair = Button(self.frameTela_Alunos, image=self.img_log_out, bg=self.corFundo,
                              activebackground=self.corFundo, highlightthickness=0, border=0,
                              command=self.bt_frameUsuarios_sair)
        self.bt_Sair.place(relx=0.91, rely=0, relwidth=0.09, relheight=0.2)

        self.label_TabelaAlunos = Label(self.frameTela_Alunos, text="Tabela Alunos", font=('arial', 28, 'bold'),
                                          fg=self.cor_texto_titulo, bg=self.corFundo)
        self.label_TabelaAlunos.place(relx=0.35, rely=0.2, relwidth=0.29, relheight=0.06)

        # --------------------------------------------------------------------------------------------------------------------------------------------
        # botoes da tabela

        self.bt_UserAdd = Button(self.frameTela_Alunos, image=self.img_UserAdd, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_UserAdd.place(relx=0.02, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Edit = Button(self.frameTela_Alunos, image=self.img_Edit, bg=self.corFundo,
                              activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Edit.place(relx=0.1, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Lixeira = Button(self.frameTela_Alunos, image=self.img_Lixeira, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Lixeira.place(relx=0.18, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Refresh = Button(self.frameTela_Alunos, image=self.img_Refresh, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Refresh.place(relx=0.26, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Printer = Button(self.frameTela_Alunos, image=self.img_Printer, bg=self.corFundo,
                                 activebackground=self.corFundo, highlightthickness=0, border=0)
        self.bt_Printer.place(relx=0.34, rely=0.26, relwidth=0.06, relheight=0.09)

        self.bt_Search = Button(self.frameTela_Alunos, image=self.img_Search, highlightthickness=0, border=0,
                                command=self.busca_Usuario)
        self.bt_Search.place(relx=0.9, rely=0.26, relwidth=0.06, relheight=0.09)

        self.entry_Tab_alunos = Entry(self.frameTela_Alunos, highlightthickness=0, border=0,
                                       font=('verdana', 28, 'bold'), fg=self.cor_texto_pesquisa)
        self.entry_Tab_alunos.place(relx=0.5, rely=0.26, relwidth=0.4, relheight=0.09)

        #########################################################################################
        # listagem tabela

        self.frame_2 = Frame(self.frameTela_Alunos, bd=4, bg='grey')
        self.frame_2.place(relx=0.01, rely=0.37, relwidth=0.98, relheight=0.6)

        self.listaAlunos = ttk.Treeview(self.frame_2, height=3, column=(
        "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))

        self.listaAlunos.heading("#0", text="")
        self.listaAlunos.heading("#1", text="CPF")
        self.listaAlunos.heading("#2", text="Nome")
        self.listaAlunos.heading("#3", text="Data Nascimento")
        self.listaAlunos.heading("#4", text="Endereço")
        self.listaAlunos.heading("#5", text="Telefone")
        self.listaAlunos.heading("#6", text="Email")
        self.listaAlunos.heading("#7", text="Nome Usuario")
        self.listaAlunos.heading("#8", text="Senha")
        self.listaAlunos.heading("#9", text="Data Cadastro")
        self.listaAlunos.column("#0", width=0)
        self.listaAlunos.column("#1", width=125)
        self.listaAlunos.column("#2", width=200)
        self.listaAlunos.column("#3", width=150)
        self.listaAlunos.column("#4", width=200)
        self.listaAlunos.column("#5", width=125)
        self.listaAlunos.column("#6", width=200)
        self.listaAlunos.column("#7", width=125)
        self.listaAlunos.column("#8", width=125)
        self.listaAlunos.column("#9", width=200)
        self.listaAlunos.place(relx=0, rely=0, relwidth=0.98, relheight=0.95)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.scroolLista.place(relx=0.98, rely=0, relwidth=0.02, relheight=1)

        self.scroolLista2 = Scrollbar(self.frame_2, orient='horizontal', relief="solid")
        self.scroolLista2.place(relx=0, rely=0.95, relwidth=0.98, relheight=0.05)

        self.listaAlunos.configure(xscrollcommand=self.scroolLista2.set, yscrollcommand=self.scroolLista.set)
        self.scroolLista.config(command=self.listaAlunos.yview)
        self.scroolLista2.config(command=self.listaAlunos.xview)

        self.listaAlunos.bind("<Double-1>", self.OnDoubleClick)

        # stylo tabela

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background='grey', foreground=self.cor_texto_titulo, rowheight=25,
                        fieldbackground=self.corFundo)
        style.map(self.listaAlunos, "Treeview", background=[('select', 'red')])

        # -------------------------------------------------------------------------------------------------------------------------------------


Telas()