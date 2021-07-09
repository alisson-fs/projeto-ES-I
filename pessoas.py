from pessoa import Pessoa
from registro import Registro


class Pessoas(Registro):
    def __init__(self):
        super().__init__()

    def adicionar(self, pessoa):
        if isinstance(pessoa, Pessoa):
            self.DB.append(pessoa)

    def remover(self, cpf):
        for pessoa in self.DB:
            if pessoa.cpf == cpf:
                self.DB.remove(pessoa)

    def consultar(self, cpf):
        for pessoa in self.DB:
            if pessoa.cpf == cpf:
                return pessoa
