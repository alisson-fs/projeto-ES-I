from comentario import Comentario
from registro import Registro


class Comentarios(Registro):
    def __init__(self):
        super().__init__()

    def adicionar(self, comentario):
        cursor = self.connection.cursor()
        consulta = '''INSERT INTO COMENTARIOS (TITULO, COMENTARIO) VALUES (%s,%s)'''
        valores = (comentario.titulo, comentario.comentario)
        cursor.execute(consulta,valores)
        self.connection.commit()

    def remover(self, titulo):
        cursor = self.connection.cursor()
        query = '''DELETE FROM COMENTARIOS WHERE TITULO=\'''' + titulo + '''\''''
        cursor.execute(query)
        self.connection.commit()

    def consultar(self):
        pass

    def gerar_lista(self, titulo):
        lista = []
        consulta = '''SELECT COMENTARIO FROM COMENTARIOS WHERE TITULO=\'''' + titulo + '''\''''
        cursor = self.connection.cursor()
        cursor.execute(consulta)
        registro = cursor.fetchall()
        for sugestao in registro:
            lista.append(sugestao[0])
        return lista

    def atualizar(self):
        pass
