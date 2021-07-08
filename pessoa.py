

class Pessoa:
    def __init__(self, nome, cpf, nascimento, admin, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__nascimento =nascimento
        self.__admin = admin
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nascimento(self):
        return self.__nascimento

    @property
    def admin(self):
        return self.__admin

    @property
    def senha(self):
        return self.__senha

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @admin.setter
    def admin(self, admin):
        self.__admin = admin

    @senha.setter
    def senha(self, senha):
        self.__senha = senha