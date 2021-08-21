from cartao import Cartao
import datetime


class Pessoa:
    def __init__(self, nome, cpf, nascimento, senha, admin=False, assinante=False):
        self.__nome = nome
        self.__cpf = cpf
        self.__nascimento =nascimento
        self.__senha = senha
        self.__cartao = Cartao(" -", " -", " -", " -")
        self.__admin = admin
        self.__assinante = assinante
        self.__vencimento_assinatura = None
        self.__alugueis = []

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

    @property
    def assinante(self):
        return self.__assinante
    
    @property
    def cartao(self):
        return self.__cartao

    @property
    def vencimento_assinatura(self):
        return self.__vencimento_assinatura

    @property
    def alugueis(self):
        return self.__alugueis

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

    @assinante.setter
    def assinante(self, assinante):
        self.__assinante = assinante

    @cartao.setter
    def cartao(self, cartao):
        self.__cartao = cartao

    @vencimento_assinatura.setter
    def vencimento_assinatura(self, vencimento_assinatura):
        self.__vencimento_assinatura = vencimento_assinatura

    @alugueis.setter
    def alugueis(self, alugueis):
        self.__alugueis = alugueis

    def adicionar_aluguel(self, aluguel):
        self.__alugueis.append(aluguel)

    def retirar_aluguel(self, filme):
        for aluguel in self.__alugueis:
            if aluguel.filme == filme:
                self.__alugueis.remove(aluguel)

    def gerar_lista_alugados(self):
        lista = []
        for aluguel in self.__alugueis:
            lista.append(aluguel.filme.titulo)
        return lista

    def verifica_alugado(self, filme):
        alugado = False
        for aluguel in self.__alugueis:
            if aluguel.filme == filme:
                alugado = True
        return alugado

    def alugar(self, cartao, aluguel):
        self.__cartao = cartao
        self.adicionar_aluguel(aluguel)
        
    def assinar(self, cartao):
        self.__cartao = cartao
        self.__assinante = True
        self.__vencimento_assinatura = datetime.date.today()+datetime.timedelta(days=30)
