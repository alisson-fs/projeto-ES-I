from pessoa import Pessoa
from registro import Registro


class RegistroPessoas(Registro):
    def __init__(self):
        super().__init__()
        self.atual = Pessoa(" -", " -", " -", " -")

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
        return None

    def gerar_lista(self):
        lista = []
        for pessoa in self.DB:
            lista.append(pessoa.nome)
        return lista
    
    def atualizar(self, nome, cpf, nascimento, admin, nome_cartao, num_cartao, validade, cvv):
        for pessoa in self.DB:
            if pessoa.cpf == self.atual.cpf:
                pessoa.nome = nome
                pessoa.cpf = cpf
                pessoa.nascimento = nascimento
                pessoa.admin = admin
                pessoa.cartao.nome_cartao = nome_cartao
                pessoa.cartao.num_cartao = num_cartao
                pessoa.cartao.validade = validade
                pessoa.cartao.cvv = cvv
