from abc import ABC, abstractmethod


class Registro(ABC):
    def __init__(self):
        self.__DB = []
        self.__atual = None

    @property
    def DB(self):
        return self.__DB

    @property
    def atual(self):
        return self.__atual

    @atual.setter
    def atual(self, atual):
        self.__atual = atual

    @abstractmethod
    def adicionar(self, elemento):
        pass

    @abstractmethod
    def remover(self, id):
        pass

    @abstractmethod
    def consultar(self, id):
        pass

    @abstractmethod
    def atualizar(self):
        pass

    @abstractmethod
    def gerar_lista(self):
        pass
