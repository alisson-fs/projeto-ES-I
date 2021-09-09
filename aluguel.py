class Aluguel:
    def __init__(self, inicio, fim, titulo, cpf):
        self.__inicio = inicio
        self.__fim = fim
        self.__titulo = titulo
        self.__cpf = cpf

    @property
    def inicio(self):
        return self.__inicio
    
    @property
    def fim(self):
        return self.__fim
    
    @property
    def titulo(self):
        return self.__titulo

    @property
    def cpf(self):
        return self.__cpf

    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio

    @fim.setter
    def fim(self, fim):
        self.__fim = fim

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
