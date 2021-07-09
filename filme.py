class Filme:
    def __init__(self, titulo, id, duracao, genero, classificacao):
        self.__titulo = titulo
        self.__id = id
        self.__duracao = duracao
        self.__genero = genero
        self.__classificacao = classificacao

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
