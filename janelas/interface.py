import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from janelas.janaelasistema import Sismeta
from janelas.cadastro import Cadastra_Usuario
from diretorioCliente.banco_de_dados import consultar_dados,criar_tabela_extrato
import bcrypt

class Jenala(Tk):
    def __init__(self):
        super().__init__()

        # ---------- Configurações da janela ----------------------
        largura = 500
        altura = 200
        pos_x = self.winfo_screenwidth() // 2 - largura // 2
        pos_y = self.winfo_screenheight() // 2 - altura // 2
        self.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.title("Janela")
        self.resizable(False, False)
        self.wm_overrideredirect(True)
        self.funcao_login()
        # --------------------------------------------------------

    def funcao_login(self):    
        self.entry_login = ctk.CTkEntry(self, placeholder_text="Login...", width=200,font=("Arial",25),show="*")
        self.entry_login.pack(pady=20)
        self.button = ctk.CTkButton(self, text="Login...", command=self.login)
        self.button.pack(pady=20)

        self.label_x = Label(self, text="X", font=("Arial", 15), bg="black", fg="white")
        self.label_x.bind("<Button-1>", self.sair)
        self.label_x.place(x=477, y=5)

        self.label_cadastra_usuario = Label(self, text="Cadastrar Usuário", font=("Arial", 10), bg="black", fg="white")
        self.label_cadastra_usuario.bind("<Button-1>", self.cadastramento)
        self.label_cadastra_usuario.place(x=5, y=175)

    def cadastramento(self,s):
        self.destroy()
        self.cliente = Cadastra_Usuario(Jenala)
        
    def sair(self,s):
        self.quit()
        
    def login(self):
        for a in consultar_dados():
            hasf_senha = a[8]
            if bcrypt.checkpw(self.entry_login.get().encode('utf-8'), hasf_senha):
                self.destroy()
                Sismeta(a)
criar_tabela_extrato()
        
            
def rodar_mypp():
    app = Jenala()
    app['bg'] = 'black'
    app.mainloop()




