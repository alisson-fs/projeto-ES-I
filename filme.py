class Filme:
    def __init__(self, titulo, id, duracao, genero, classificacao, n_avalliacoes=0, soma_avaliacoes=0):
        self.__titulo = titulo
        self.__id = id
        self.__duracao = duracao
        self.__genero = genero
        self.__classificacao = classificacao
        self.__n_avaliacoes = n_avalliacoes
        self.__soma_avaliacoes = soma_avaliacoes

    @property
    def titulo(self):
        return self.__titulo

    @property
    def id(self):
        return self.__id

    @property
    def duracao(self):
        return self.__duracao

    @property
    def genero(self):
        return self.__genero

    @property
    def classificacao(self):
        return self.__classificacao

    @property
    def n_avaliacoes(self):
        return self.__n_avaliacoes
    
    @property
    def soma_avaliacoes(self):
        return self.__soma_avaliacoes

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @id.setter
    def id(self, id):
        self.__id = id

    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @classificacao.setter
    def classificacao(self, classificacao):
        self.__classificacao = classificacao

    @n_avaliacoes.setter
    def n_avaliacoes(self, n_avaliacoes):
        self.__n_avaliacoes = n_avaliacoes

    @soma_avaliacoes.setter
    def soma_avaliacoes(self, soma_avaliacoes):
        self.__soma_avaliacoes = soma_avaliacoes
