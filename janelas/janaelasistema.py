from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import janelas.interface as janela_interface
from diretorioCliente.banco_de_dados import *
from tkinter import messagebox
from diretorioCliente.mascaramento import formata_dinheiro,mascarar_cpf,mascarar_email,mascarar_telefone
from datetime import datetime
data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class Sismeta(Tk):
    def __init__(self, *args):
        super().__init__()
        self.cliente = args[0]
        # ---------- Configurações da janela ----------------------
        largura = 1000
        altura = 550
        pos_x = self.winfo_screenwidth() // 2 - largura // 2
        pos_y = self.winfo_screenheight() // 2 - altura // 2
        self.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.title("Janela")
        self['bg'] = 'black'
        self.wm_overrideredirect(True)
        self.resizable(False, False)

        self.framesDados()
        # ------------------ fecha a janela --------------------------------------

        self.des_frame = None

        self.label_x = Label(self,text="X", font=("Arial", 15), bg="black", fg="white")
        self.label_x.bind("<Button-1>",self.janela_p)
        self.label_x.place(x=970, y=5)

        self.label_volta = Label(self,text="<", font=("Arial", 18), bg="black", fg="white")
        self.label_volta.bind("<Button-1>",self.jane)
        # self.label_volta.place(x=5, y=5)
        self.label_volta.place_forget()


    def framesDados(self):
        #--------------- frames -------------------------------------------------------
        self.frame_btn_entry = Frame(self, bg="black", width=500, height=500)
        self.frame_btn_entry.configure(highlightbackground="white", highlightcolor="white", highlightthickness=1)
        self.frame_btn_entry.pack(pady=150 , padx=50)

        # ------------------------------btn deposito ------------------------------------------

        self.btn_deposito = ctk.CTkButton(self.frame_btn_entry, text="Deposito",width=190)
        self.btn_deposito.configure(command=self.deposito)
        self.btn_deposito.grid(row=0, column=0,pady=30,padx=20)    

        #-----------------------------------btn saque ----------------------------------------------

        self.btn_saque = ctk.CTkButton(self.frame_btn_entry, text="Saque",width=190)
        self.btn_saque.configure(command=self.saque)
        self.btn_saque.grid(row=1, column=0,pady=20,padx=20)

        #---------------------------- extrato -----------------------------------------------

        self.btn_extrato = ctk.CTkButton(self.frame_btn_entry, text="Extrato",width=190)
        self.btn_extrato.configure(command=self.extrato_bancario)
        self.btn_extrato.grid(row=2, column=0,pady=20,padx=20)

        #---------------------------- transferencia -----------------------------------------------

        self.btn_transferencia = ctk.CTkButton(self.frame_btn_entry, text="Transferência",width=190)
        #self.label_sair.bind("<Button-1>", self.sair)
        self.btn_transferencia.configure(command=self.transferencia)
        self.btn_transferencia.grid(row=0, column=1,padx=70)
    
          
        self.btn_saldo = ctk.CTkButton(self.frame_btn_entry, text="Saldo",width=190)
        self.btn_saldo.configure(command=self.saldo)
        self.btn_saldo.grid(row=1, column=1,padx=70)

        
        self.btn_pagamento_conta = ctk.CTkButton(self.frame_btn_entry, text="Pagamento de contas",width=190)
        #self.label_sair.bind("<Button-1>", self.sair)
        self.btn_pagamento_conta.grid(row=2, column=1,padx=70)

    def jane(self,s):
        self.des_frame.destroy()
        self.framesDados()
        self.label_volta.place_forget()

# ---------------- funçao de deposito --------------------------------

    def deposito(self):
        self.frame_btn_entry.destroy()
        self.label_volta.place(x=5, y=5)
        self.frame_deposito = Frame(self,bg='black')
        self.des_frame = self.frame_deposito
        self.frame_deposito.place(relheight=0.50,relwidth=0.60,relx=0.20,rely=0.20) 

        self.txt_deposito = Label(self.frame_deposito,text='Deposito',font=('calibri',25),bg='black',fg='white')
        self.txt_deposito.pack(pady=10) 

        self.agencia_set = ctk.CTkEntry(self.frame_deposito,placeholder_text='Agencia',font=('arial',20))
        self.agencia_set.bind('<KeyRelease>',self.ativa_btn)
        self.agencia_set.place(x=225,y=70)

        self.conta_set = ctk.CTkEntry(self.frame_deposito,placeholder_text='Conta',font=('arial',20))
        self.conta_set.bind('<KeyRelease>',self.ativa_btn)
        self.conta_set.place(x=225,y=108)

        self.valor = ctk.CTkEntry(self.frame_deposito,placeholder_text='valor',font=('arial',20))
        self.valor.place(x=225,y=150)

        self.btn_enviar_deposito = ctk.CTkButton(self.frame_deposito,text='Enviar',state='disabled')
        self.btn_enviar_deposito.configure(command=self.enviar_dinheiro)
        self.btn_enviar_deposito.place(x=225,y=200)

        self.caixa_text = Frame(self.frame_deposito,bg='SkyBlue',width=400,height=40)
        self.caixa_text.place(x=90,y=250)

        self.text_titula = Label(self.caixa_text,font=('calibri',15,'bold'),bg='SkyBlue',fg='black')
        self.text_titula.place(x=0,y=0)

    def ativa_btn(self,s):
        agencia = self.agencia_set.get()
        conta = self.conta_set.get()
        ativo = True
        for a in consultar_dados():
            if a[5] == agencia and a[6] == conta :
                ativo = False
                self.btn_enviar_deposito.configure(state='normal')
                self.text_titula['text'] = f'Titular: {a[1]}'
        if ativo:
            self.btn_enviar_deposito.configure(state='disabled')
            self.text_titula['text'] = ''
        
    def enviar_dinheiro(self):
        if not self.agencia_set.get().split() or not self.conta_set.get().split() or not self.valor.get().split():
            messagebox.showerror('Erro','prencha os campo vazios')
                    
        else:
            
            agencia = self.agencia_set.get()
            conta = self.conta_set.get()
            cont = 0
            for a in consultar_dados():
                if a[5] == agencia and a[6] == conta :
                    valor = float(self.valor.get())
                    cont = valor
                    valor += a[9]
                    atualizar_dados_bancario(a[0],valor)
                    inserir_no_extrato(a[0],a[1],data,'Deposito',cont,valor)
                    self.agencia_set.delete(0,END)
                    self.conta_set.delete(0,END  )
                    self.valor.delete(0,END)
                       
# ----------------- função extrato ---------------------------------------------------

    def extrato_bancario(self):
        self.frame_btn_entry.destroy()
        self.label_volta.place_forget()
        self.label_volta.place(x=5, y=5)
        self.frame_extrato = Frame(self)
        self.des_frame = self.frame_extrato
        self.frame_extrato.place(relwidth=0.99,relheight=0.67,rely=0.1)

        colunas = ("cliente", "data", "descricao", "valor", "saldo")
        self.tree_extrato = ttk.Treeview(self.frame_extrato,columns=colunas,show="headings")

        # Cabeçalhos
        self.tree_extrato.heading("cliente", text="Cliente")
        self.tree_extrato.heading("data", text="Data")
        self.tree_extrato.heading("descricao", text="Descrição")
        self.tree_extrato.heading("valor", text="Valor")
        self.tree_extrato.heading("saldo", text="Saldo")

        # Alinhamento e largura
        self.tree_extrato.column("cliente", anchor="w", width=180)
        self.tree_extrato.column("data", anchor="center", width=100)
        self.tree_extrato.column("descricao", anchor="center", width=100)
        self.tree_extrato.column("valor", anchor="center", width=50)
        self.tree_extrato.column("saldo", anchor="center", width=50)

        self.scroll_y = ttk.Scrollbar(self.frame_extrato,orient="vertical",command=self.tree_extrato.yview)

        self.tree_extrato.configure(yscrollcommand=self.scroll_y.set)

        self.tree_extrato.pack(side="left", fill="both", expand=True)
        self.scroll_y.pack(side="right", fill="y")

        self.tree_extrato.tag_configure("negativo", background="PowderBlue")
        self.tree_extrato.tag_configure("positivo", background="PaleTurquoise") 
        
       
        lista_dados = list()
        for x in set_extrato(self.cliente[0]):
            lista_dados.append((x[1],x[3],x[4],formata_dinheiro(x[5]),formata_dinheiro(x[6])))
      
        for x in range(0,len(lista_dados)):
            self.tag = "negativo" if x % 2 else "positivo"
            self.tree_extrato.insert("","end",values=(lista_dados[x]),tags=self.tag)

# ------------------------ Saldo -------------------------------------

    def saldo(self):
        self.frame_btn_entry.destroy()
        self.label_volta.place_forget()
        self.label_volta.place(x=5, y=5)

        self.frame_saldo = Frame(self,bg='black')
        self.des_frame = self.frame_saldo
        self.frame_saldo.place(relheight=0.50,relwidth=0.60,relx=0.20,rely=0.20) 

        self.frame_d = Frame(self.frame_saldo,width=200,height=10)
        self.frame_d.place(x=100,y=5)

        self.frame_d.grid_columnconfigure(0, minsize=100)
        self.frame_d.grid_columnconfigure(1, minsize=300)

        for a in consultar_dados():
            if a[0] == self.cliente[0]:
                # ----------- Nome cliente --------------------------------
                self.label_cliente = Label(self.frame_d,text=f'Cliente: {a[1]}')
                self.label_cliente.config(font=('calibri',15))
                self.label_cliente.grid(row=0,column=0,sticky='w')

                # -------------- Cpf cliente -----------------------------

                self.label_cpf_c = Label(self.frame_d,text=f'Cpf: {mascarar_cpf(a[2])}')
                self.label_cpf_c.config(font=('calibri',15))
                self.label_cpf_c.grid(row=1,column=0,sticky='w')

                # -------------- Email -----------------------------------

                self.label_email= Label(self.frame_d,text=f'Email: {mascarar_email(a[3])}')
                self.label_email.config(font=('calibri',15))
                self.label_email.grid(row=2,column=0,sticky='w')

                # ------------- Telefone ---------------------------------

                self.label_telefone = Label(self.frame_d,text=f'Telefone: {mascarar_telefone(a[4])}')
                self.label_telefone.config(font=('calibri',15))
                self.label_telefone.grid(row=3,column=0,sticky='w')

                # -------------- Conta -----------------------------------

                self.label_conta= Label(self.frame_d,text=f'Conta: {a[5]}')
                self.label_conta.config(font=('calibri',15))
                self.label_conta.grid(row=4,column=0,sticky='w')

                # ------------------- Agencia ----------------------------

                self.label_agencia = Label(self.frame_d,text=f'Agencia: {a[6]}')
                self.label_agencia.config(font=('calibri',15))
                self.label_agencia.grid(row=5,column=0,sticky='w')

                # -------------- Saldo -----------------------------------

                self.label_saldo = Label(self.frame_d,text=f'Saldo: {formata_dinheiro(a[9])} R$')
                self.label_saldo.config(font=('calibri',15))
                self.label_saldo.grid(row=6,column=0,sticky='w')

# ------------------- função saque -------------------------------------------------   
    def saque(self):
        self.frame_btn_entry.destroy()
        self.label_volta.place(x=5, y=5)
        self.frame_saque = Frame(self,bg='black')
        self.des_frame = self.frame_saque
        self.frame_saque.configure(highlightbackground="white", highlightcolor="white", highlightthickness=1)
        self.frame_saque.place(relheight=0.50,relwidth=0.60,relx=0.20,rely=0.20) 

        self.txt_saque = Label(self.frame_saque,text='Saque')
        self.txt_saque.config(font=('calibri',20),bg='black',fg='white')
        self.txt_saque.place(x=270,y=8)

        self.entry_saque = ctk.CTkEntry(self.frame_saque)
        self.entry_saque.configure(font=('calibri',25))
        self.entry_saque.place(x=235,y=60)

        self.btSaque = ctk.CTkButton(self.frame_saque,text='Saque')
        self.btSaque.configure(command=self.sacar_dinheiro)
        self.btSaque.place(x=235,y=120)

        self.label_saque_text = Label(self.frame_saque,bg='black',foreground='white')
        self.label_saque_text.config(font=('calibri',15))
        self.label_saque_text.place(x=180,y=180)

    def sacar_dinheiro(self):

        valor = self.entry_saque.get()
        if not valor.split() or not valor.isdigit():
            messagebox.showerror('Erro!','Operação inválida')
        else:
            cont = 0
            for x in consultar_dados():
                if x[0] == self.cliente[0]:
                    if x[9] >= int(valor):
                        cont = int(valor)
                        valor = x[9] - int(valor)
                        atualizar_dados_bancario(x[0],valor)
                        inserir_no_extrato(x[0],x[1],data,'Saque',cont,valor)
                        self.label_saque_text['text'] = 'saque realizado com sucesso'
                        self.label_saque_text['fg'] = 'white'
                        self.label_saque_text.place(x=180,y=180)
                        self.entry_saque.delete(0,END)
                        self.label_saque_text.after(3000, lambda: self.label_saque_text.config(text=''))

                    else:
                        self.label_saque_text['text'] = 'Saldo insuficiente'
                        self.label_saque_text['fg'] = 'red'
                        self.label_saque_text.place(x=230,y=180)
                        self.label_saque_text.after(3000, lambda: self.label_saque_text.config(text=''))
       
# --------------------------- transferencia ------------------------------------------------------

    def transferencia(self):
        self.frame_btn_entry.destroy()
        self.label_volta.place(x=5, y=5)
        self.frame_transferencia = Frame(self,bg='black')
        self.des_frame = self.frame_transferencia
        self.frame_transferencia.configure(highlightbackground="white", highlightcolor="white", highlightthickness=1)
        self.frame_transferencia.place(relheight=0.60,relwidth=0.60,relx=0.20,rely=0.20)


        self.txt_trans = Label(self.frame_transferencia,text='Transferência',font=('calibri',25),bg='black',fg='white')
        self.txt_trans.pack(pady=10) 

        self.agencia_trans = ctk.CTkEntry(self.frame_transferencia,placeholder_text='Agencia',font=('arial',20))
        self.agencia_trans.bind('<KeyRelease>',self.ativa_btn_trans)
        self.agencia_trans.place(x=225,y=70)

        self.conta_trans = ctk.CTkEntry(self.frame_transferencia,placeholder_text='Conta',font=('arial',20))
        self.conta_trans.bind('<KeyRelease>',self.ativa_btn_trans)
        self.conta_trans.place(x=225,y=108)

        self.valor_trans = ctk.CTkEntry(self.frame_transferencia,placeholder_text='Valor',font=('arial',20))
        self.valor_trans.place(x=225,y=150)

        self.btn_enviar_trans= ctk.CTkButton(self.frame_transferencia,text='Enviar',state='disabled')
        self.btn_enviar_trans.configure(command=self.enviar_trandferencia)
        self.btn_enviar_trans.place(x=225,y=200)

        self.caixa_text_trans = Frame(self.frame_transferencia,bg='silver',width=400,height=30)
        self.caixa_text_trans.place(x=90,y=250)

        self.text_titula_trans = Label(self.caixa_text_trans,font=('calibri',15,'bold'),bg='silver',fg='black')
        self.text_titula_trans.place(x=0,y=0)

        self.label_trans_ok = Label(self.frame_transferencia)
        self.label_trans_ok.config(font=('calibri',13),bg='black',fg='red')
        self.label_trans_ok.place(x=160,y=290)

    def ativa_btn_trans(self,s):
        agencia = self.agencia_trans.get()
        conta = self.conta_trans.get()
        ativo = True
        for a in consultar_dados():
            if a[5] == agencia and a[6] == conta :
                ativo = False
                self.btn_enviar_trans.configure(state='normal')
                self.text_titula_trans['text'] = f'Titular: {a[1]}'
        if ativo:
            self.btn_enviar_trans.configure(state='disabled')
            self.text_titula_trans['text'] = ''

    def enviar_trandferencia(self):
        
        agencia_ = self.agencia_trans.get()
        conta_ = self.conta_trans.get()
        valor_trans =  self.valor_trans.get()
        if not agencia_ or not conta_ or not valor_trans.isdigit(): 
            messagebox.showerror('Erro!','Dados inválido')

        else:
            
            for x in consultar_dados():
                if x[5] == agencia_ and x[6] == conta_:
                    if x[9] >= int(valor_trans):
                        transferir(self.cliente[0],x[0],int(valor_trans))
                        self.agencia_trans.delete(0,END)
                        self.conta_trans.delete(0,END)
                        self.valor_trans.delete(0,END)
                        self.label_trans_ok['text'] ='transferência Realizada com Sucesso '
                        self.label_trans_ok.after(3000,lambda:self.label_trans_ok.config(text=''))

                    else:
                        messagebox.showerror('Erro na transferência','Saldo inválido')
                        
# -------------------------------------------------------------------------------------------------


    def janela_p(self,s):                          
        self.destroy()
        ja_ = janela_interface.Jenala()
        ja_['bg'] = 'black'
        ja_.mainloop()
       
    def sair(self,s):
        self.quit()

if __name__ == "__main__":
    root = Sismeta().mainloop()
  