class Comentario:
    def __init__(self, titulo, comentario):
        self.__titulo = titulo
        self.__comentario = comentario

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def comentario(self):
        return self.__comentario

    @comentario.setter
    def comentario(self, comentario):
        self.__comentario = comentario
