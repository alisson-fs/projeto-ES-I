from abc import ABC, abstractmethod


class Estado(ABC):
    def __init__(self):
        self.__container = None
        self.__window = None
        self.__erro = False
        
    @property
    def container(self):
        return self.__container

    @property
    def window(self):
        return self.__window

    @property
    def erro(self):
        return self.__erro

    @window.setter
    def window(self, window):
        self.__window = window

    @window.setter
    def window(self, window):
        self.__window = window

    @container.setter
    def container(self, container):
        self.__container = container

    @erro.setter
    def erro(self, erro):
        self.__erro = erro

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def ler_evento(self, event, values):
        pass