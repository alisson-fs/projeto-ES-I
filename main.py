import psycopg2
from catalogo import Catalogo
from registro_pessoas import RegistroPessoas
from alugueis import Alugueis
from sugestoes import Sugestoes
import PySimpleGUI as sg
from estado_login import EstadoLogin
from estado_cadastro import EstadoCadastro
from estado_catalogo import EstadoCatalogo
from estado_visualizar_filme import EstadoVisualizarFilme
from estado_visualizar_pessoa import EstadoVisualizarPessoa
from estado_editar_pessoa import EstadoEditarPessoa
from estado_editar_filme import EstadoEditarFilme
from estado_assinar import EstadoAssinar
from estado_adicionar_filme import EstadoAdicionarFilme
from estado_gerenciar_pessoas import EstadoGerenciarPessoas
from estado_alugar import EstadoAlugar
from estado_alugados import EstadoAlugados
from estado_avaliar import EstadoAvaliar
from estado_sugerir import EstadoSugerir
from estado_sugestoes import EstadoSugestoes


sg.theme("DarkTeal10")

connection = psycopg2.connect(user="postgres",
							  password="postgres",
							  host="localhost",
							  port="5432",
							  database="uflix")

catalogo = Catalogo(connection)
registro_pessoas = RegistroPessoas(connection)
alugueis = Alugueis(connection)
sugestoes = Sugestoes(connection)

estados = {"login": EstadoLogin(False, False, registro_pessoas),
           "cadastro_admin": EstadoCadastro(True, False, registro_pessoas),
           "cadastro_cliente": EstadoCadastro(False, False, registro_pessoas),
           "catalogo_admin": EstadoCatalogo(True, True, registro_pessoas, catalogo, alugueis),
           "catalogo_assinante": EstadoCatalogo(False, True, registro_pessoas, catalogo, alugueis),
           "catalogo_cliente": EstadoCatalogo(False, False, registro_pessoas, catalogo, alugueis),
           "visualizar_filme_admin": EstadoVisualizarFilme(True, True, catalogo),
           "visualizar_filme_assinante": EstadoVisualizarFilme(False, True, catalogo),
           "visualizar_filme_cliente": EstadoVisualizarFilme(False, False, catalogo),
           "visualizar_pessoa": EstadoVisualizarPessoa(True, True, registro_pessoas),
           "editar_pessoa": EstadoEditarPessoa(True, True, registro_pessoas),
           "editar_filme": EstadoEditarFilme(True, True, catalogo),
           "assinar": EstadoAssinar(False, False, registro_pessoas),
           "adicionar_filme": EstadoAdicionarFilme(True, True, catalogo),
           "lista_pessoas": EstadoGerenciarPessoas(True, True, registro_pessoas),
           "alugar": EstadoAlugar(False, False, registro_pessoas, catalogo, alugueis),
           "alugados": EstadoAlugados(False, False, registro_pessoas, catalogo, alugueis),
           "avaliar": EstadoAvaliar(False, False, catalogo),
           "sugerir": EstadoSugerir(False, True, sugestoes),
           "sugestoes": EstadoSugestoes(True, False, sugestoes)}

estado = "login"
while True:
    estados[estado].run()
    event, values = estados[estado].window.read()
    proximo_estado = estados[estado].ler_evento(event, values)
    estado = proximo_estado
    if event == sg.WIN_CLOSED:
        break
