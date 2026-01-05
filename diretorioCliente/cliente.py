class Cliente:
    def __init__(self,nome:str,cpf:str,email:str,telefone:str):
        self.__nome = nome.title()
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def email(self):
        return self.__email

    @property
    def telefone(self):
        return self.__telefone

    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nEmail: {self.email}\nTelefone: {self.telefone}'
