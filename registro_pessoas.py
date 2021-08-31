from pessoa import Pessoa
from registro import Registro
from cartao import Cartao


class RegistroPessoas(Registro):
    def __init__(self, connection):
        super().__init__(connection)
        self.atual = Pessoa(" -", " -", " -", " -")

    def adicionar(self, pessoa):
        cursor = self.connection.cursor()
        consulta = '''INSERT INTO REGISTRO_PESSOAS (NOME,CPF,NASCIMENTO,SENHA,ADMINISTRADOR,ASSINANTE,VENCIMENTO_ASSINATURA,NOME_CARTAO,NUM_CARTAO,VALIDADE,CVV) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        valores = (pessoa.nome, pessoa.cpf, pessoa.nascimento, pessoa.senha, str(pessoa.admin), str(pessoa.assinante), pessoa.vencimento_assinatura, " -", " -", " -", " -")
        cursor.execute(consulta,valores)
        self.connection.commit()

    def remover(self, cpf):
        cursor = self.connection.cursor()
        query = '''DELETE FROM REGISTRO_PESSOAS WHERE CPF=''' + str(cpf)
        cursor.execute(query)
        self.connection.commit()

    def consultar(self, cpf):
        cursor = self.connection.cursor()
        consulta = '''SELECT (NOME,CPF,NASCIMENTO,SENHA,ADMINISTRADOR,ASSINANTE,VENCIMENTO_ASSINATURA,NOME_CARTAO,NUM_CARTAO,VALIDADE,CVV) FROM REGISTRO_PESSOAS WHERE CPF=''' + str(cpf)
        cursor.execute(consulta)
        registro = cursor.fetchone()
        if registro != None:
            cartao = Cartao(registro[7], registro[8], registro[9], registro[10])
            pessoa = Pessoa(registro[0], registro[1], registro[2], registro[3], cartao, registro[6], registro[4], registro[5])
            return pessoa
        else:
            return None

    def gerar_lista(self):
        lista = []
        consulta = '''SELECT (NOME) FROM REGISTRO_PESSOAS'''
        cursor = self.connection.cursor()
        cursor.execute(consulta)
        registro = cursor.fetchone()
        for pessoa in registro:
            lista.append(pessoa[0])
        return lista

    def atualizar(self, nome, cpf, nascimento, admin, assinante, nome_cartao, num_cartao, validade, cvv):
        for pessoa in self.DB:
            if pessoa.cpf == self.atual.cpf:
                pessoa.nome = nome
                pessoa.cpf = cpf
                pessoa.nascimento = nascimento
                pessoa.admin = admin
                pessoa.cartao.nome_cartao = nome_cartao
                pessoa.cartao.num_cartao = num_cartao
                pessoa.cartao.validade = validade
                pessoa.cartao.cvv = cvv
        cursor = self.connection.cursor()
        consulta = '''UPDATE CATALOGO SET NOME=%s,CPF=%s,NASCIMENTO=%s,ADMINISTRADOR=%s,ASSINANTE=%s,NOME_CARTAO=%s,NUM_CARTAO=%s,VALIDADE=%s,CVV=%s WHERE CPF=%s'''
        valores = (nome, cpf, nascimento, str(admin), str(assinante), nome_cartao, num_cartao, validade, cvv, cpf)
        cursor.execute(consulta,valores)
        self.connection.commit()
