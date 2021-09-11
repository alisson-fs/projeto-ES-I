import psycopg2
from singleton import Singleton

class Registro(metaclass=Singleton):
    def __init__(self):
        self.__connection = psycopg2.connect(user="postgres",
							                 password="postgres",
							                 host="localhost",
							                 port="5432",
							                 database="uflix")
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

    def adicionar(self, elemento):
        pass

    def remover(self, id):
        pass

    def consultar(self, id):
        pass

    def atualizar(self):
        pass

    def gerar_lista(self):
        pass
