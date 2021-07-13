import datetime

from estado import Estado
from pessoa import Pessoa
from filme import Filme
from catalogo import Catalogo
from registro_pessoas import RegistroPessoas
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


sg.theme("DarkTeal10")

catalogo = Catalogo()
catalogo.adicionar(Filme("Senhor dos aneis", "1", "180min", "Aventura", "14"))
catalogo.adicionar(Filme("Harry Potter 1", "2", "144min", "Aventura", "12"))
catalogo.adicionar(Filme("Harry Potter 2", "3", "144min", "Aventura", "12"))
catalogo.adicionar(Filme("Harry Potter 3", "4", "144min", "Aventura", "12"))
catalogo.adicionar(Filme("Harry Potter 4", "5", "144min", "Aventura", "12"))
catalogo.adicionar(Filme("Harry Potter 5", "6", "144min", "Aventura", "12"))
catalogo.adicionar(Filme("Harry Potter 6", "7", "144min", "Aventura", "12"))
catalogo.adicionar(Filme("Harry Potter 7", "8", "144min", "Aventura", "12"))
catalogo.adicionar(Filme("Harry Potter 8", "9", "144min", "Aventura", "12"))

registro_pessoas = RegistroPessoas()
registro_pessoas.adicionar(Pessoa("Admin", "000", "10/07/2021", "000", True, True))
registro_pessoas.adicionar(Pessoa("Eduardo Betim", "10787946931", "10/05/2000", "123", False, True))
registro_pessoas.consultar("10787946931").vencimento_assinatura = datetime.date.today()+datetime.timedelta(days=30)
registro_pessoas.adicionar(Pessoa("Alisson Fabra da Silva", "12214622969", "18/09/2000", "321", False, False))

estados = {"login": EstadoLogin(False, False, registro_pessoas),
           "cadastro_admin": EstadoCadastro(True, False, registro_pessoas),
           "cadastro_cliente": EstadoCadastro(False, False, registro_pessoas),
           "catalogo_admin": EstadoCatalogo(True, True, catalogo),
           "catalogo_assinante": EstadoCatalogo(False, True, catalogo),
           "catalogo_cliente": EstadoCatalogo(False, False, catalogo),
           "visualizar_filme_admin": EstadoVisualizarFilme(True, True, catalogo),
           "visualizar_filme_cliente": EstadoVisualizarFilme(False, True, catalogo),
           "visualizar_pessoa": EstadoVisualizarPessoa(True, True, registro_pessoas),
           "editar_pessoa": EstadoEditarPessoa(True, True, registro_pessoas),
           "editar_filme": EstadoEditarFilme(True, True, catalogo),
           "assinar": EstadoAssinar(False, False, registro_pessoas),
           "adicionar_filme": EstadoAdicionarFilme(True, True, catalogo),
           "lista_pessoas": EstadoGerenciarPessoas(True, True, registro_pessoas)}

estados["editar_filme"].filme = catalogo.consultar("Harry Potter 2")
estados["editar_pessoa"].pessoa = registro_pessoas.consultar("107879469-31")

estado = "login"
while True:
    estados[estado].run()
    event, values = estados[estado].window.read()
    proximo_estado = estados[estado].ler_evento(event, values)
    estado = proximo_estado
    if event == sg.WIN_CLOSED:
        break
estados[estado].window.close()
