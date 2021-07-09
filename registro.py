from abc import ABC, abstractmethod


class Registro(ABC):
    def __init__(self):
        self.__DB = []

    @property
    def DB(self):
        return self.__DB

    @abstractmethod
    def adicionar(self, elemento):
        pass

    @abstractmethod
    def remover(self, id):
        pass

    @abstractmethod
    def consultar(self, id):
        pass
