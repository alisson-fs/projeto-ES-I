from pessoa import Pessoa


class Registro:
    def __init__(self):
        self.__DB = []

    @property
    def DB(self):
        return self.__DB

    def adicionar_pepssoa(self, pessoa):
        if isinstance(pessoa, Pessoa):
            self.__DB.append(pessoa)

    def remover_pessoa(self, cpf):
        for pessoa in self.__DB:
            if pessoa.cpf == cpf:
                self.__DB.remove(pessoa)

    def consultar_pessoa(self, cpf):
        for pessoa in self.__DB:
            if pessoa.cpf == cpf:
                return pessoa
