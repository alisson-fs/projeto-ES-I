class Sugestao:
    def __init__(self, sugestao):
        self.__sugestao = sugestao

    @property
    def sugestao(self):
        return self.__sugestao

    @sugestao.setter
    def sugestao(self, sugestao):
        self.__sugestao = sugestao
