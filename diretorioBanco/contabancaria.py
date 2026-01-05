from diretorioCliente.cliente import Cliente
from diretorioCliente.banco_de_dados import inserir_dados

class ContaBancaria:
    def __init__(self, cliente: Cliente,conta:str,agencia:str,login:str,senha:str):
        self.__cliente: Cliente = cliente
        self.__conta = conta
        self.__agencia = agencia
        self.__login = login
        self.__senha = senha
        self.__saldo: float = 0.0


    @property
    def cliente(self) -> 'cliente':
        return  self.__cliente

    @property
    def conta(self)-> str:
        return self.__conta

    @property
    def agencia(self)-> str:
        return self.__agencia


    @property
    def login(self):
        return self.__login
    
    @property
    def senha(self):
        return self.__senha
    

    @property
    def saldo(self):
        return self.__saldo
    
    
    def __str__(self):
            return f'Cliente: {self.cliente.nome.title()}\nConta: {self.conta}\nAgencia:{self.agencia}\nlogin:{self.login}\nSenha:{self.senha}\nSaldo:{self.saldo}'