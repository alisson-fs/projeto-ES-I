from aluguel import Aluguel
from registro import Registro
import datetime


class Alugueis(Registro):
    def __init__(self):
        super().__init__()

    def adicionar(self, aluguel):
        cursor = self.connection.cursor()
        consulta = '''INSERT INTO ALUGUEIS (INICIO,FIM,TITULO,CPF) VALUES (%s,%s,%s,%s)'''
        valores = (aluguel.inicio, aluguel.fim, aluguel.titulo, aluguel.cpf)
        cursor.execute(consulta,valores)
        self.connection.commit()

    def remover(self, titulo, cpf):
        cursor = self.connection.cursor()
        query = '''DELETE FROM ALUGUEIS WHERE TITULO=\'''' + titulo + '''\' AND CPF=\'''' + cpf + '''\''''
        cursor.execute(query)
        self.connection.commit()

    def consultar(self, titulo, cpf):
        cursor = self.connection.cursor()
        consulta = '''SELECT INICIO,FIM,TITULO,CPF FROM ALUGUEIS WHERE TITULO=\'''' + titulo + '''\' AND CPF=\'''' + cpf + '''\''''
        cursor.execute(consulta)
        registro = cursor.fetchone()
        if registro != None:
            aluguel = Aluguel(registro[0], registro[1], registro[2], registro[3])
            return aluguel
        else:
            return None

    def gerar_lista(self, cpf):
        lista = []
        consulta = '''SELECT TITULO,FIM FROM ALUGUEIS WHERE CPF=\'''' + cpf + '''\''''
        cursor = self.connection.cursor()
        cursor.execute(consulta)
        registro = cursor.fetchall()
        for aluguel in registro:
            if datetime.date.today() < datetime.datetime.strptime(aluguel[1], '%Y-%m-%d').date():
                lista.append(aluguel[0])
        return lista

    def atualizar(self, nome, cpf, nascimento, admin, assinante):
        pass

    def verifica_alugado(self, filme, pessoa):
        alugado = False
        lista_alugueis = self.gerar_lista(pessoa.cpf)
        for titulo in lista_alugueis:
            if titulo == filme.titulo:
                alugado = True
        return alugado
