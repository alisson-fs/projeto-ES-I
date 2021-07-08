from abc import ABC, abstractmethod


class Estado(ABC):
    def __init__(self):
        self.__container = None
        self.__window = None

    @property
    def container(self):
        return self.__container

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window

    @container.setter
    def container(self, container):
        self.__container = container

    @abstractmethod
    def run(self):
        pass