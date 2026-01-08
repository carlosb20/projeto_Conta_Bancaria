from tkinter import *
import customtkinter as ctk
import janelas.interface as janela_interface

class Sismeta(Tk):
    def __init__(self, *args):
        super().__init__()

        # ---------- Configurações da janela ----------------------
        largura = 1000
        altura = 500
        pos_x = self.winfo_screenwidth() // 2 - largura // 2
        pos_y = self.winfo_screenheight() // 2 - altura // 2
        self.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.title("Janela")
        self['bg'] = 'black'
        self.wm_overrideredirect(True)
        self.resizable(False, False)

        print(args[0])

        # ------------------ fecha a janela --------------------------------------

        self.label_x = Label(self,text="X", font=("Arial", 15), bg="black", fg="white")
        self.label_x.bind("<Button-1>",self.janela_p)
        self.label_x.place(x=370, y=5)

        #--------------- frames -------------------------------------------------------
        self.frame_btn_entry = Frame(self, bg="black", width=500, height=500)
        self.frame_btn_entry.configure(highlightbackground="white", highlightcolor="white", highlightthickness=1)
        self.frame_btn_entry.pack(pady=150 , padx=50)



        # ------------------------------btn deposito ------------------------------------------


        self.btn_deposito = ctk.CTkButton(self.frame_btn_entry, text="Deposito",width=190)
        #self.label_deposito.bind("<Button-1>", self.deposito)
        self.btn_deposito.grid(row=0, column=0,pady=30,padx=20)    

        #-----------------------------------btn saque ----------------------------------------------

        self.btn_saque = ctk.CTkButton(self.frame_btn_entry, text="Saque",width=190)
        #self.label_transferencia.bind("<Button-1>", self.transferencia)
        self.btn_saque.grid(row=1, column=0,pady=20,padx=20)

        #---------------------------- extrato -----------------------------------------------

        self.btn_extrato = ctk.CTkButton(self.frame_btn_entry, text="Extrato",width=190)
        #self.label_sair.bind("<Button-1>", self.sair)
        self.btn_extrato.grid(row=2, column=0,pady=20,padx=20)

        #---------------------------- transferencia -----------------------------------------------

        self.btn_transferencia = ctk.CTkButton(self.frame_btn_entry, text="Transferencia",width=190)
        #self.label_sair.bind("<Button-1>", self.sair)
        self.btn_transferencia.grid(row=0, column=1,padx=70)
    
          
        
    def deposito(self):
        pass   
    
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
  