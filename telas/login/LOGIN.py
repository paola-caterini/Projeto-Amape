


from tkinter import *
from tkinter import ttk
#from sistemaAulas.dominio.admin import Admin
#from sistemaAulas.persistencia.admin_dao import AdminDAO



root = Tk()

class Application():
    def __init__(self):

       # self.usuario1=Admin(cpf='0111',nome_completo='Emerson oli',data_cadastro='25/05/1988',endereco='rua 5',telefone= '000007770',email='emerson@eu.com',nome_usuario='emerson',senha='amape')
       # AdminDAO.adicionar_admin(self.usuario1)

        


        self.root = root    
        self.tela()
       
        root.mainloop()
    def tela(self):
      
        #tela
        self.root.attributes('-zoomed',True) # maximizar
        self.root.title("AMAPE",)
        self.root.configure(background= '#0D1521')        
        self.root.minsize(width=700, height= 480)
        
        #label login
        self.lb_nome = Label(self.root, text="LOGIN", font = ('arial', 58, 'bold'), bg= '#0D1521')
        self.lb_nome.pack(anchor='center',pady=45,)

        #frames
        self.frame_usuario=Frame(self.root,bg= '#0D1521')
        self.frame_usuario.place(relx= 0.2, rely=0.3,height=65,relwidth=0.5)

        self.frame_senha=Frame(self.root,bg= '#0D1521')
        self.frame_senha.place(relx= 0.2, rely=0.5,height=65,relwidth=0.5)


        #icones
        self.img_usuario = PhotoImage(file='usuario.png')           
        self.img_senha = PhotoImage(file='trancar.png')
       


        self.ico_usuario = Label(self.frame_usuario,image=self.img_usuario,  bg= '#0D1521')
        self.ico_usuario.place(relx=0, rely=0,)

        self.ico_senha = Label(self.frame_senha,image=self.img_senha,  bg= '#0D1521')
        self.ico_senha.place(relx=0, rely=0)

        
        #entry
        self.usuario_entry = Entry(self.frame_usuario, font = ('verdana', 20, 'bold'))
        self.usuario_entry.place(relx=0.2, rely=0, relwidth=0.9,relheight=1)

        self.senha_entry = Entry(self.frame_senha,font = ('verdana', 20, 'bold'),show='*')
        self.senha_entry.place(relx=0.2, rely=0,relwidth=0.9,relheight=1)

        #botoes
        self.bt_entrar = Button(self.root, text= "ENTRAR", bd=2, bg = '#6634cb',fg = 'white',
                                activebackground='#8b67d5', activeforeground="white"
                                , font = ('verdana', 20, 'bold'),command=self.action_entrar)
        self.bt_entrar.place(relx= 0.3, rely=0.7, relwidth=0.4, relheight= 0.15)


        self.bt_esqueceu = Button(self.root, text= "Esqueceu a Senha ?", bd=0, bg = '#0D1521',fg = 'white',
                                activebackground='#0D1521', activeforeground="#8b67d5"
                                , font = ('verdana', 12, 'bold'),command=self.action_esqueceu)
        self.bt_esqueceu.place(relx= 0.3, rely=0.9, relwidth=0.4, relheight= 0.04)


    def action_entrar(self):
        print(f'Usuario: ',self.usuario_entry.get())
        print(f'Senha: ',self.senha_entry.get())


    def action_esqueceu(self):
        print("Esqueceu a Senha")
        
        

Application()