from PySimpleGUI.PySimpleGUI import No
from filme import Filme
from registro import Registro


class Catalogo(Registro):
    def __init__(self, connection):
        super().__init__(connection)
        self.atual = Filme(" -", " -", " -", " -", " -")

    def adicionar(self, filme):
        cursor = self.connection.cursor()
        consulta = '''INSERT INTO CATALOGO (TITULO,FILME_ID,DURACAO,GENERO,CLASSIFICACAO,N_AVALIACOES,SOMA_AVALIACOES) VALUES (%s,%s,%s,%s,%s,%s,%s)'''
        valores = (filme.titulo, filme.id, filme.duracao, filme.genero, filme.classificacao, str(0), str(0))
        cursor.execute(consulta,valores)
        self.connection.commit()

    def remover(self, titulo):
        cursor = self.connection.cursor()
        query = '''DELETE FROM CATALOGO WHERE TITULO=\'''' + str(titulo) + '''\''''
        cursor.execute(query)
        self.connection.commit()

    def consultar(self, titulo):
        cursor = self.connection.cursor()
        consulta = '''SELECT TITULO,FILME_ID,DURACAO,GENERO,CLASSIFICACAO,N_AVALIACOES,SOMA_AVALIACOES FROM CATALOGO WHERE TITULO=\'''' + titulo + '''\''''
        cursor.execute(consulta)
        registro = cursor.fetchone()
        if registro != None:
            filme = Filme(registro[0], registro[1], registro[2], registro[3], registro[4], float(registro[5]), float(registro[6]))
            return filme
        else:
            return None

    def gerar_lista(self):
        lista = []
        consulta = '''SELECT TITULO FROM CATALOGO'''
        cursor = self.connection.cursor()
        cursor.execute(consulta)
        registro = cursor.fetchall()
        for filme in registro:
            lista.append(filme[0])
        return lista

    def atualizar(self, titulo, id, duracao, genero, classificacao, n_avaliacoes, soma_avaliacoes):
        cursor = self.connection.cursor()
        consulta = '''UPDATE CATALOGO SET TITULO=%s,FILME_ID=%s,DURACAO=%s,GENERO=%s,CLASSIFICACAO=%s,N_AVALIACOES=%s,SOMA_AVALIACOES=%s WHERE TITULO=%s'''
        valores = (titulo, id, duracao, genero, classificacao, n_avaliacoes, soma_avaliacoes, titulo)
        cursor.execute(consulta,valores)
        self.connection.commit()

    def avaliar(self, nota):
        self.atual.soma_avaliacoes += nota
        self.atual.n_avaliacoes += 1
        self.atualizar(self.atual.titulo, self.atual.id, self.atual.duracao, self.atual.genero, self.atual.classificacao, self.atual.n_avaliacoes, self.atual.soma_avaliacoes)
