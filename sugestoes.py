from sugestao import Sugestao
from registro import Registro


class Sugestoes(Registro):
    def __init__(self):
        super().__init__()

    def adicionar(self, sugestao):
        cursor = self.connection.cursor()
        consulta = '''INSERT INTO SUGESTOES (SUGESTAO) VALUES (%s)'''
        valores = (sugestao.sugestao,)
        cursor.execute(consulta,valores)
        self.connection.commit()

    def remover(self, sugestao):
        cursor = self.connection.cursor()
        query = '''DELETE FROM SUGESTOES WHERE SUGESTAO=\'''' + sugestao + '''\''''
        cursor.execute(query)
        self.connection.commit()

    def consultar(self):
        pass

    def gerar_lista(self):
        lista = []
        consulta = '''SELECT SUGESTAO FROM SUGESTOES'''
        cursor = self.connection.cursor()
        cursor.execute(consulta)
        registro = cursor.fetchall()
        for sugestao in registro:
            lista.append(sugestao[0])
        return lista

    def atualizar(self):
        pass
