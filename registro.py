from abc import ABC, abstractmethod


class Registro(ABC):
    def __init__(self, connection):
        self.__connection = connection
        self.__atual = None


    @property
    def connection(self):
        return self.__connection

    @property
    def atual(self):
        return self.__atual

    @connection.setter
    def connection(self, connection):
        self.__connection = connection

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
