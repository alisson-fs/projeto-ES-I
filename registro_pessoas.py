from pessoa import Pessoa
from registro import Registro


class RegistroPessoas(Registro):
    def __init__(self):
        super().__init__()
        self.atual = Pessoa(" -", " -", " -", " -")

    def adicionar(self, pessoa):
        cursor = self.connection.cursor()
        consulta = '''INSERT INTO REGISTRO_PESSOAS (NOME,CPF,NASCIMENTO,SENHA,VENCIMENTO_ASSINATURA,ADMINISTRADOR,ASSINANTE) VALUES (%s,%s,%s,%s,%s,%s,%s)'''
        valores = (pessoa.nome, pessoa.cpf, pessoa.nascimento, pessoa.senha, pessoa.vencimento_assinatura, str(pessoa.admin), str(pessoa.assinante))
        cursor.execute(consulta,valores)
        self.connection.commit()

    def remover(self, cpf):
        cursor = self.connection.cursor()
        query = '''DELETE FROM REGISTRO_PESSOAS WHERE CPF=\'''' + str(cpf) + '''\''''
        cursor.execute(query)
        self.connection.commit()

    def consultar(self, cpf):
        cursor = self.connection.cursor()
        consulta = '''SELECT NOME,CPF,NASCIMENTO,SENHA,VENCIMENTO_ASSINATURA,ADMINISTRADOR,ASSINANTE FROM REGISTRO_PESSOAS WHERE CPF=\'''' + str(cpf) + '''\''''
        cursor.execute(consulta)
        registro = cursor.fetchone()
        if registro != None:
            if registro[5] == "True":
                admin = True
            else:
                admin = False
            if registro[6] == "True":
                assinante = True
            else:
                assinante = False
            pessoa = Pessoa(registro[0], registro[1], registro[2], registro[3], registro[4], admin, assinante)
            return pessoa
        else:
            return None

    def gerar_lista(self):
        lista = []
        consulta = '''SELECT CPF FROM REGISTRO_PESSOAS'''
        cursor = self.connection.cursor()
        cursor.execute(consulta)
        registro = cursor.fetchall()
        for pessoa in registro:
            lista.append(pessoa[0])
        return lista

    def atualizar(self, nome, cpf, nascimento, vencimento_assinatura, admin, assinante):
        lista_pessoas_cpf = self.gerar_lista()
        for pessoa_cpf in lista_pessoas_cpf:
            if pessoa_cpf == self.atual.cpf:
                cursor = self.connection.cursor()
                consulta = '''UPDATE REGISTRO_PESSOAS SET NOME=%s,NASCIMENTO=%s,VENCIMENTO_ASSINATURA=%s,ADMINISTRADOR=%s,ASSINANTE=%s WHERE CPF=%s'''
                valores = (nome, nascimento, vencimento_assinatura, str(admin), str(assinante), str(cpf))
                cursor.execute(consulta,valores)
                self.connection.commit()
