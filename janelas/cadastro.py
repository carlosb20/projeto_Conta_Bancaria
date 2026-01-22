from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
from diretorioCliente.banco_de_dados import consultar_dados,inserir_dados,update_dados
from diretorioBanco.contabancaria import ContaBancaria
from diretorioCliente.cliente import Cliente
from diretorioBanco.criptografasenha import criptografa
#from diretorioCliente.mascaramento import conta_bancaria_



class Cadastra_Usuario(Tk):
    def __init__(self, *args):
        super().__init__()
     

        largura = 800
        altura = 550
        pos_x = self.winfo_screenwidth() // 2 - largura // 2
        pos_y = self.winfo_screenheight() // 2 - altura // 2
        self.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.title("Janela")
        self['bg'] = 'black'
        self.resizable(False, False)
        self.wm_overrideredirect(True)
        self.configure(highlightbackground="white", highlightcolor="white", highlightthickness=1)

        # -------------------------- Criação da janela -----------------------------------

        self.var_nome = ctk.StringVar()
        self.var_cpf = ctk.StringVar()
        self.var_email = ctk.StringVar()
        self.var_telefone = ctk.StringVar()
        self.var_conta = ctk.StringVar()
        self.var_agencia = ctk.StringVar()
        self.var_login = ctk.StringVar()
        self.var_senha = ctk.StringVar()


        self.frame_pai = Frame(self, bg="black", width=800, height=500)
        self.frame_pai.configure(highlightbackground="white", highlightcolor="white", highlightthickness=1)
        self.frame_pai.pack(pady=25)
        
        self.cadastro_frame = Frame(self.frame_pai, bg="black", width=500, height=500)
        self.cadastro_frame.configure(highlightbackground="white", highlightcolor="white", highlightthickness=1)
        self.cadastro_frame.grid(row=0, column=0, padx=10,)

        self.cadastro_frame2 = Frame(self.frame_pai, bg="black", width=200, height=500)
        self.cadastro_frame2.configure(highlightbackground="white", highlightcolor="white", highlightthickness=1)
        self.cadastro_frame2.grid(row=0, column=1, padx=10)


        # -------------------------- Criação dos campos do cadastro -----------------------------------
        self.label_nome = Label(self.cadastro_frame, text="nome", font=("Arial", 20), bg="black", fg="white")
        self.label_nome.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nome = ctk.CTkEntry(self.cadastro_frame, width=200,font=("Arial",25))
        self.entry_nome.configure(textvariable=self.var_nome)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)
        # ------------------------------------------ CPF -------------------------------------------------------
        
        self.label_cpf = Label(self.cadastro_frame, text="CPF", font=("Arial", 20), bg="black", fg="white")
        self.label_cpf.grid(row=1, column=0, padx=10, pady=10)

        self.entry_cpf = ctk.CTkEntry(self.cadastro_frame, width=200,font=("Arial",25))
        self.entry_cpf.configure(textvariable=self.var_cpf)
        self.entry_cpf.grid(row=1, column=1, padx=10, pady=10)
        # ------------------------------------------ Email -------------------------------------------------------
        
        self.label_email = Label(self.cadastro_frame, text="Email", font=("Arial", 20), bg="black", fg="white")
        self.label_email.grid(row=2, column=0, padx=10, pady=10)

        self.entry_email = ctk.CTkEntry(self.cadastro_frame, width=200,font=("Arial",25))
        self.entry_email.configure(textvariable=self.var_email)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)
        # ------------------------------------------ Telefone -------------------------------------------------------
        
        self.label_telefone = Label(self.cadastro_frame, text="Telefone", font=("Arial", 20), bg="black", fg="white")
        self.label_telefone.grid(row=3, column=0, padx=10, pady=10)

        self.entry_telefone = ctk.CTkEntry(self.cadastro_frame, width=200,font=("Arial",25))
        self.entry_telefone.configure(textvariable=self.var_telefone)
        self.entry_telefone.grid(row=3, column=1, padx=10, pady=10)

        # -------------------------- CONTA -----------------------------------------------

        self.label_conta = Label(self.cadastro_frame, text="Conta", font=("Arial", 20), bg="black", fg="white")
        self.label_conta.grid(row=4, column=0, padx=10, pady=10)

        self.entry_conta = ctk.CTkEntry(self.cadastro_frame, width=200,font=("Arial",25))
        self.entry_conta.configure(textvariable=self.var_conta)
        self.entry_conta.grid(row=4, column=1, padx=10, pady=10)

        # -------------------------- AGENCIA -----------------------------------------------

        self.label_agengia = Label(self.cadastro_frame, text="Agencia", font=("Arial", 20), bg="black", fg="white")
        self.label_agengia.grid(row=5, column=0, padx=10, pady=10)

        self.entry_agencia = ctk.CTkEntry(self.cadastro_frame, width=200,font=("Arial",25))
        self.entry_agencia.configure(textvariable=self.var_agencia)
        self.entry_agencia.grid(row=5, column=1, padx=10, pady=10)

        # -------------------------- login -----------------------------------------------

        self.label_login = Label(self.cadastro_frame, text="Login", font=("Arial", 20), bg="black", fg="white")
        self.label_login.grid(row=6, column=0, padx=10, pady=10)

        self.entry_login = ctk.CTkEntry(self.cadastro_frame, width=200,font=("Arial",25))
        self.entry_login.configure(textvariable=self.var_login)
        self.entry_login.grid(row=6, column=1, padx=10, pady=10)

        # -------------------------- Senha -----------------------------------------------

        self.label_senha = Label(self.cadastro_frame, text="Senha", font=("Arial", 20), bg="black", fg="white")
        self.label_senha.grid(row=7, column=0, padx=10, pady=10)

        self.entry_senha = ctk.CTkEntry(self.cadastro_frame,width=200,font=("Arial",25))
        self.entry_senha.configure(textvariable=self.var_senha)
        self.entry_senha.grid(row=7, column=1, padx=10, pady=10)
        # ---------------------------------botao -------------------------------------------------------------

        self.button_cadastrar = ctk.CTkButton(self.cadastro_frame2, text="Cadastrar")
        self.button_cadastrar.bind("<Button-1>", self.cadastra_usuario_no_banco)
        self.button_cadastrar.grid(row=8, column=0, columnspan=2, padx=10, pady=40)

        self.button_limpa = ctk.CTkButton(self.cadastro_frame2, text="Limpar",command=lambda:self.limpa_entrys())
        self.button_limpa.grid(row=9, column=0, columnspan=2, padx=10, pady=40)

        self.button_voltar = ctk.CTkButton(self.cadastro_frame2, text="Voltar")
        self.button_voltar.bind("<Button-1>", self.deleta_janela)
        self.button_voltar.grid(row=10, column=0, columnspan=2, padx=10, pady=40)
        

        self.button_update = ctk.CTkButton(self.cadastro_frame2, text="Update", command=self.funcao_update)
        self.button_update.grid(row=11, column=0, columnspan=2, padx=10, pady=40)

        self.chamar_jenala_principal = args[0]

        

    def cadastra_usuario_no_banco(self,s):
        if (
        not self.entry_nome.get().strip() or
        not self.entry_cpf.get().strip() or
        not self.entry_email.get().strip() or
        not self.entry_telefone.get().strip() or
        not self.entry_conta.get().strip() or
        not self.entry_agencia.get().strip() or
        not self.entry_login.get().strip() or
        not self.entry_senha.get().strip()
    ):
            messagebox.showwarning("Atenção", "Preencha todos os campos")
        else:
            try:
                ca = Cliente(self.entry_nome.get(),self.entry_cpf.get(),self.entry_email.get(),self.entry_telefone.get())
                self.banco = ContaBancaria(ca,self.entry_conta.get(),self.entry_agencia.get(),criptografa(self.entry_senha.get()),criptografa(self.entry_senha.get()))
                inserir_dados(self.banco.cliente.nome,self.banco.cliente.cpf,self.banco.cliente.email,self.banco.cliente.telefone,self.banco.conta,self.banco.agencia,self.banco.login,self.banco.senha,self.banco.saldo)
                messagebox.showinfo("Atenção", "Cadastro realizado com sucesso")
                self.limpa_entrys()
                
            except Exception as e:
                print(e)
                messagebox.showwarning("Atenção", "Erro ao cadastrar")
            # 3030 3131    
       
    def deleta_janela(self,s):
        self.destroy()
        ca =self.chamar_jenala_principal()
        ca['bg'] = 'black'
        ca.mainloop()
    # -------------------------------------- funcao update --------------------------------   
    def funcao_update(self):
        self.label_login = LabelFrame(self.cadastro_frame2,width=150,height=200,text="Senha...", font=("Arial", 14), bg="black", fg="white",padx=6)
        self.label_login.grid(row=9,column=0,padx=8)

        self.entry_update = ctk.CTkEntry(self.label_login,placeholder_text="Senha...",width=100,font=("Arial",15),show='*')
        self.entry_update.pack(pady=10)

        self.bt_update = ctk.CTkButton(self.label_login,text="Busca usuario",width=80,font=("Arial",10))
        self.bt_update.bind("<Button-1>",self.progessa_dados)
        self.bt_update.pack(pady=10)

        self.bt_confimar = ctk.CTkButton(self.label_login, text="Confirma",width=80,font=("Arial",10))
        self.bt_confimar.bind("<Button-1>", self.update_dos_dados_do_usuario)
        self.bt_confimar.pack(pady=10)

        self.label_s = Label(self.label_login,text='x',bg='black',fg='white')
        self.label_s.bind("<Button-1>" , lambda _ : self.label_login.destroy())
        self.label_s.pack(anchor='e')
       
    def progessa_dados(self,s):
        import bcrypt
        self.lista_dados = []
        senha_digitada = self.entry_update.get().encode('utf-8')
        if not self.entry_update.get():
            messagebox.showwarning("Atencao","Digite uma senha")
        else:
            try:
                for a in consultar_dados():
                    senha_hash = a[8]  # hash salvo no banco (bytes)
                    if bcrypt.checkpw(senha_digitada, senha_hash):
                        self.lista_dados.append(a)
                        print("Login válido")
                        self.var_nome.set(a[1])
                        self.var_cpf.set(a[2])
                        self.var_email.set(a[3])
                        self.var_telefone.set(a[4])
                        self.var_conta.set(a[5])
                        self.var_agencia.set(a[6])
                        self.var_login.set('**************')
                        self.var_senha.set('**************')
                    else:
                        print("Login inválido")
                        self.entry_update.configure(border_color="red",border_width=2,placeholder_text="Senha incorreta")
            except Exception as e:
                print(e)
               
                
    def update_dos_dados_do_usuario(self,s):
        if self.entry_update.get():
            
            if not self.entry_login.get() == '**************' and not self.entry_senha.get() == '**************':
                update_dados(self.lista_dados[0][0],self.var_nome.get(),self.var_cpf.get(),self.var_email.get(),self.var_telefone.get(),self.var_conta.get(),self.var_agencia.get(),criptografa(self.var_login.get()),criptografa(self.var_senha.get()))
                messagebox.showinfo("Sucesso", "Atualizado com sucesso")
                self.entry_update.delete(0,END)
                self.limpa_entrys()
            else:
                messagebox.showwarning("Atencao","( ************ ) não e recomendado para login e senha")
        else:
            messagebox.showwarning("Atencao","Digite sua senha")
#===============================================================================================================   
        
    def limpa_entrys(self):
        self.entry_nome.delete(0,END)
        self.entry_cpf.delete(0,END)
        self.entry_email.delete(0,END)
        self.entry_telefone.delete(0,END)
        self.entry_conta.delete(0,END)
        self.entry_agencia.delete(0,END)
        self.entry_login.delete(0,END)
        self.entry_senha.delete(0,END)

