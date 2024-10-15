


from tkinter import *
from tkinter import ttk, messagebox
import base64

from sistemaAulas.config import DB_PATH
from sistemaAulas.controladores.admin_controller import AdminController
#from  sistemaAulas import main





root = Tk()

class Application():
    def __init__(self):

        self.root = root

        self.tela()

        root.mainloop()
    def tela(self):
      
        #tela
        #self.root.attributes('-zoomed',True)     ################ maximizar Tela
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


        #icones em convertidos em base64 para evitar erro.
        self.img_usuario = PhotoImage(data=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAABApJREFUeJztms1rH0UYx79Pg220LwiCEWpsJK0trY2CBQ8WxNb24KFU6L/QN1/w7sGDlJ4UBLUWwT/CUzWperEgimhjBFtobRELKbSkpia/JISPh0lEfua3M7szu9PQ/Vxn9rvP99nZnZln1tQQwCZJ+yUdlDQiaUjSY5LuSFqQdEnSr5JGJX1hZrNNxVYrwFbgI+Au4UwDZ4DB3PFXBugH3gXmShjvpgOcBtbm9lMK4AlgPMJ4Nz8Cw7l9BQGMADcSml/mBrAzt79CcE/+zxrMLzMJbMntc0Vw73zKYd+LH4D+VHGvSSUk6W1JuxPq9WKPpHcauE84uKku9Gv/M/AasAN4EFgP7ALeAn4J1JgFhnL7/hfcPO9jBjgB9Bx1QB/wemAyzzTpsSfAJvyLnBngxRKa+wKSMAU8VKe30GBfDXhaxyvovhGge6QOT2UD/cQT5EXAKuj2ARMe7Q9i408xC4x42j81M8qKmtmipM883Z4vq9tNigQMedrPR2iPedo3R2hLkkoPzW6AjqR1BV36zWyuovZGSX8VdJkxs/VVtJdJMQIWEmj0YtHT3hd7gxQJmPG0Pxmh7bt2KkJbUpoEXPa074vQ9l17NUJbUpoETHjaj1Ow+uvF0jXHPN0ultXtJkUCRj3tI5JKL4QknZT0tKfPVxV004Lb0Ex7Fiwd4KUSmvuXriliGoiaAZKBK2D66AAni14HYA1uMzQboHe2SY+FAIMBT2yZcdw6fyeuiLIBtx1+k/DtcId7aTssSbjqbVOcyu33fwAPAN83YP4CULTyzAcwTL1F0WvAo7l9FoJ7tydrMH8d2JXbXxDA48B3Cc1fAAZy+yoF7gt/mrAprRcd4BSr7WjsvwBbcOuEqRLGp4GzNDDVRdcDQsEVMF+RtFeukrNZ0iNyW9o7chubnyR9Lemcmf3dVGwtLS0t9y1JZgHgYbmfn7ZLGpBU13L1pqRJSb9JGjOz6JpgFMBBYBSYj1jsVGV+6d4Hchh/ChjLYLoXXwJbmzJ/ALid2fBK3AJertv8YWAhs9EiFoBDZTwFfwSBZyR9K2lD2cQ1zF1JL5jZeEjnoATgdmMTkrZFBNYklyTtNjPvsV3oucAJrR7zkpuOj4Z09I6Apaf/h/xz+6KkzyV9IzdX18GA3HHZIfkPRiclDYaMgkJwc72PK4DvR4lkAM8CVwPiip8VgI89N7kNxJwAV41rGH+R5UOfTsg34DlP+3tm9ntY2OkwsyuS3vd088XuB1eNLWJ79E2qx7bDE9s1n0bIR3BOUlFRcp2ZzZeIOxm4D3TR7zfzZlZ4iBKSgMI/vMyssbriSsTGl/Jn6VVJm4DcAeSmTUDuAHLTJiB3ALlpE5A7gNy0CcgdQG7u+wT8A2lUGKvItXv5AAAAAElFTkSuQmCC'))
        self.img_senha = PhotoImage(data=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAABOpJREFUeJztm9urFlUYh5/laWtqdBYrUSksMcPIENSozBILUyrpQqKgQIISMiqKotsuyptuKiP8A6KTZVESCbUpyrK9tegkWlDtoIOpbY/76WK2ZjrzrfXNN998ij2Xa63vt37vu/fMrPWumUBNqJcA84HZwBRgAjB2sHsn8CPwNdANrA8hbKnLW9tQR6sr1F6bp0e9Tz2l03E0jTpEvUf9tUTgR9OnLleHdDquJNRJancFgR/Nh+rETsfXEPVq9fc2BH+I39SrOh1nLuqNan8bgz9Ev3pDp+P9D+pc9e8agj/EbnV2Fd5DBcGPAz4Hxrdupyn6gBkhhF9aEakiAeuAhYnD+4G3gNeBzcDPg+3jgenAokGtUYl6b4QQFqW7rRj1lsR/2QPqc+q5CZrnqavVg4nai+uINc/oEHVzgsGdZUyqC9U/E/S32Ik1gro4wdwu9fIW5phpdsOLUf9loL6aYOzWCua5LWGel6uIqRlTY9S9EVNrK5xvXWSuPda5Z1AXJPxVLq1wvhkJ811XRrvszeOKSH9vCKGnpPYxhBA2AV9Ghs0so102AVMi/etK6jbizUj/RWVEyyZgXKT/25K6jfgu0n9OGdGyCRgd6e8rqduInyL9p5YRLZuAYZH+PSV1W9GMecrlxKiytJFSWUvgFXV/xZrDK9YDSiRA7SJ+vY0pZ6clTlW7Qgh7m/lRU5eAOh/oBaY287uamAr0qNdWrqwG9WHTt6idZEB90ip3iOrTHQ6qDM9UFfxjnY6kBR6NxdewJKbOATYAQyvJZv0MAPNCCBuKBhQmQB1GdsO7uA3G6uQrYHoI4WBeZ6PH4B2kBd8PrAHWAtuAph5DJegCJgE3AXcCIyPjpwK3k3lMR92UcI11qxOaDqEi1InqRwk+P21WeFqC6Mdqavm6baij1E8S/OauXYqelfMi8+4HloUQ+ltyXwGDHpaReWrENXmNRQmIVXxeCiHE9ue1EUL4BogVRnNjKkrA+RGxt2OmOkDMU+69qigBp0fEtkft1M+2SP+ZeY1FCRgREWtHwaNVYvej3JjaVQ8oRJ0J3E92GHqotLYb6AFWhRA+q9vTMZidtzViVkndm9V9DXT3qktKas+KeM5966y2kpg6BlhN48rOCGC1Giu6VkadNcErgTMSxp0FzG2zl8PUmYBmymRj40Oqoc4EbARMGDcANLd2b4HaEhBC2Aq8kDD0+RDCtjbbOUzd5wL3AqvI3zLvAZ4CVtRpqNZ1QAhhH/CA+gRwIf9Wmg4A34cQdtXpBzqwEAIYDHRTJ+Y+mpP+aOz/BBS05xYQj6CraiMVEPN0IK+xKAF/RcQ6VgdsQOxV+h15jUUJiO33F0Tt1M/1kf5teY1FCYitxJZ6HH28oE4GlkaGbWxGcFJClfUDs6PyjqIOV99P8Du5WeGeBNF31bPbFFuKx3Hqewk+C9ccjY7G7ibbv8fYATxLdjK0lfaXy0YCF5CdDC0n7eWou0IIL+Z1NErAUOALYFoJk8cTvcBlRWeDhQuhwR+sJNuenqgMACuLgofISjCE8A7weNWuauSREML6lhTMXo9Zk3CjOd7IveZbScLJ+47QEYlYov7Q2fgast12f0Nkdhz9kNV8F1wVfeqDauxliWMo/dmc2WNyDtnzeDbZs/k04sdqrbIP+INszdENvAZ0N7rTN+IfINN/ij5RpEEAAAAASUVORK5CYII='))
       


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
        nome_usuario=self.usuario_entry.get()
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


    def action_esqueceu(self):
        print("Esqueceu a Senha")



Application()