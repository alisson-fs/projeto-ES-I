class Cartao:
    def __init__(self, nome_cartao, num_cartao, validade, cvv):
        self.__nome_cartao = nome_cartao
        self.__num_cartao = num_cartao
        self.__validade = validade
        self.__cvv = cvv

    @property
    def nome_cartao(self):
        return self.__nome_cartao

    @property
    def num_cartao(self):
        return self.__num_cartao

    @property
    def validade(self):
        return self.__validade

    @property
    def cvv(self):
        return self.__cvv

    @nome_cartao.setter
    def nome_cartao(self, nome_cartao):
        self.__nome_cartao = nome_cartao

    @num_cartao.setter
    def num_cartao(self, num_cartao):
        self.__num_cartao = num_cartao

    @validade.setter
    def validade(self, validade):
        self.__validade = validade

    @cvv.setter
    def cvv(self, cvv):
        self.__cvv = cvv
