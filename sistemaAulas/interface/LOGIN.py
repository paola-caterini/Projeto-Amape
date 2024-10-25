import sqlite3
from time import sleep
from tkinter import *
from tkinter import ttk, messagebox
import base64

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
    

class Funçao(Cores_imagens):

    def bt_FrameLogin_entrar(self):
        #messagebox.showinfo("Sucesso", "Login bem-sucedido!")

        self.frameTela_Login.destroy()

        self.telaHome()



        '''nome_usuario=self.usuario_entry.get()
        senha=self.senha_entry.get()
        admin_controller = AdminController(DB_PATH)
        # Autenticar um administrador
        if admin_controller.autenticar_admin(nome_usuario, senha):
            print("Admin autenticado com sucesso!")
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")


            exit(1)
        else:
            print("Falha na autenticação do admin.")
            messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")
            #main.main()
            exit(0)
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
        self.select_lista_usuarios()






###############################################################################################33

    def limpa_cliente(self):
        self.codigo_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.nome_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("../sistema_aulas.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")
    '''def montaTabelas(self):
        self.conecta_bd()
        ### Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)               
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    '''
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
    def OnDoubleClick(self, event):
        self.limpa_cliente()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ? """,
                            (self.nome, self.fone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_cliente()
        self.select_lista()

    def select_lista_usuarios(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro FROM administradores
            ORDER BY nome_completo ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
    def busca_Usuario(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.entry_tab_usuario.insert(END, '%')
        nome = self.entry_tab_usuario.get()
        self.cursor.execute(
            """  SELECT cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro FROM administradores
            WHERE nome_cliente LIKE '%s' ORDER BY nome_completo ASC""" % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values=i)
        #self.limpa_cliente()
        self.desconecta_bd()
    def images_base64(self):
        self.btnovo_base64 = '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'


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

        self.bt_Cadastro = Button(self.frameTela_Usuarios,image=self.img_cadastro, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        #self.bt_Cadastro.place(relx= 0.1, rely=0, relwidth=0.2, relheight= 0.2)

        self.bt_Aulas = Button(self.frameTela_Usuarios,image=self.img_Aulas, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        #self.bt_Aulas.place(relx= 0.31, rely=0, relwidth=0.2, relheight= 0.2)
        
        self.bt_Relatorios = Button(self.frameTela_Usuarios,image=self.img_Relatorios, bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        #self.bt_Relatorios.place(relx= 0.52, rely=0, relwidth=0.2, relheight= 0.2)

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

        self.bt_Refresh = Button(self.frameTela_Usuarios,image=self.img_Refresh,bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_Refresh.place(relx= 0.26, rely=0.26, relwidth=0.06, relheight= 0.09)

        self.bt_Printer = Button(self.frameTela_Usuarios,image=self.img_Printer,bg=self.corFundo,activebackground =self.corFundo,highlightthickness=0,border=0)
        self.bt_Printer.place(relx= 0.34, rely=0.26, relwidth=0.06, relheight= 0.09)

        self.bt_Search = Button(self.frameTela_Usuarios,image=self.img_Search,highlightthickness=0,border=0,command=self.busca_Usuario)
        self.bt_Search.place(relx= 0.9, rely=0.26, relwidth=0.06, relheight= 0.09)

        self.entry_Tab_usuario = Entry(self.frameTela_Usuarios,highlightthickness=0,border=0,font = ('verdana', 28, 'bold'),fg=self.cor_texto_pesquisa)
        self.entry_Tab_usuario.place(relx= 0.5, rely=0.26, relwidth=0.4, relheight= 0.09)
      
        #########################################################################################
        #listagem tabela

        self.frame_2 = Frame(self.frameTela_Usuarios, bd=4, bg='grey')
        self.frame_2.place(relx=0.01, rely=0.37, relwidth=0.98, relheight=0.6)

        self.listaCli = ttk.Treeview(self.frame_2, height=3,column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8","col9"))

        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="CPF")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Data Nascimento")
        self.listaCli.heading("#4", text="Endereço")
        self.listaCli.heading("#5", text="Telefone")
        self.listaCli.heading("#6", text="Email")
        self.listaCli.heading("#7", text="Nome Usuario")
        self.listaCli.heading("#8", text="Senha")
        self.listaCli.heading("#9",text="Data Cadastro")
        self.listaCli.column("#0", width=0)
        self.listaCli.column("#1", width=125)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=150)
        self.listaCli.column("#4", width=200)
        self.listaCli.column("#5", width=125)
        self.listaCli.column("#6", width=200)
        self.listaCli.column("#7", width=125)
        self.listaCli.column("#8", width=125)
        self.listaCli.column("#9", width=200)
        self.listaCli.place(relx=0, rely=0, relwidth=0.98, relheight=0.95)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')        
        self.scroolLista.place(relx=0.98, rely=0, relwidth=0.02, relheight=1)

        self.scroolLista2 = Scrollbar(self.frame_2, orient='horizontal',relief="solid")
        self.scroolLista2.place(relx=0, rely=0.95, relwidth=0.98, relheight=0.05)

        self.listaCli.configure(xscrollcommand=self.scroolLista2.set,yscrollcommand=self.scroolLista.set)
        self.scroolLista.config(command=self.listaCli.yview)
        self.scroolLista2.config(command=self.listaCli.xview)

        self.listaCli.bind("<Double-1>", self.OnDoubleClick)


        #stylo tabela

        style=ttk.Style()
        style.theme_use('default')
        style.configure("Treeview",background='grey',foreground=self.cor_texto_titulo,rowheight=25,fieldbackground=self.corFundo)
        style.map(self.listaCli,"Treeview", background=[('select','red')])
        
              
        #-------------------------------------------------------------------------------------------------------------------------------------





Telas()