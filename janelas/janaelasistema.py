from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import janelas.interface as janela_interface
from diretorioCliente.banco_de_dados import *
from tkinter import messagebox
from diretorioCliente.mascaramento import formata_dinheiro
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

        #print(args[0])
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

        #print(args)

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
        #self.label_transferencia.bind("<Button-1>", self.transferencia)
        self.btn_saque.grid(row=1, column=0,pady=20,padx=20)

        #---------------------------- extrato -----------------------------------------------

        self.btn_extrato = ctk.CTkButton(self.frame_btn_entry, text="Extrato",width=190)
        self.btn_extrato.configure(command=self.extrato_bancario)
        self.btn_extrato.grid(row=2, column=0,pady=20,padx=20)

        #---------------------------- transferencia -----------------------------------------------

        self.btn_transferencia = ctk.CTkButton(self.frame_btn_entry, text="Transferência",width=190)
        #self.label_sair.bind("<Button-1>", self.sair)
        self.btn_transferencia.grid(row=0, column=1,padx=70)
    
          
        self.btn_saldo = ctk.CTkButton(self.frame_btn_entry, text="Saldo",width=190)
        #self.label_sair.bind("<Button-1>", self.sair)
        self.btn_saldo.grid(row=1, column=1,padx=70)

        
        self.btn_pagamento_conta = ctk.CTkButton(self.frame_btn_entry, text="Pagamento de contas",width=190)
        #self.label_sair.bind("<Button-1>", self.sair)
        self.btn_pagamento_conta.grid(row=2, column=1,padx=70)

    def jane(self,s):
        # self.frame_deposito.destroy()
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

        self.text_titula = Label(self.frame_deposito,font=('calibri',15),bg='black',fg='white')
        self.text_titula.place(x=235,y=250)

    def ativa_btn(self,s):
        agencia = self.agencia_set.get()
        conta = self.conta_set.get()
        ativo = True
        for a in consultar_dados():
            if a[5] == agencia and a[6] == conta :
                ativo = False
                self.btn_enviar_deposito.configure(state='normal')
                self.text_titula['text'] = f'Titular {a[1]}'
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
        
        # 8181 , 3030 , 5151
       
        lista_dados = list()
        for x in set_extrato(self.cliente[0]):
            lista_dados.append((x[1],x[3],x[4],formata_dinheiro(x[5]),formata_dinheiro(x[6])))
      
        for x in range(0,len(lista_dados)):
            self.tag = "negativo" if x % 2 else "positivo"
            self.tree_extrato.insert("","end",values=(lista_dados[x]),tags=self.tag)
            
    
    def saque(self):
        pass
    def transferencia(self):
        pass
    
    def janela_p(self,s):
        self.destroy()
        ja_ = janela_interface.Jenala()
        ja_['bg'] = 'black'
        ja_.mainloop()
       
    def sair(self,s):
        self.quit()

if __name__ == "__main__":
    root = Sismeta().mainloop()
  