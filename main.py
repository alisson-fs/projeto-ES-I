from estado import Estado
from pessoa import Pessoa
from filme import Filme
from catalogo import Catalogo
from pessoas import Pessoas
import PySimpleGUI as sg
from estado_login import EstadoLogin
from estado_cadastro import EstadoCadastro
from estado_catalogo import EstadoCatalogo
from estado_visualizar_filme import EstadoVisualizarFilme
from estado_visualizar_pessoa import EstadoVisualizarPessoa
from estado_editar_pessoa import EstadoEditarPessoa
from estado_editar_filme import EstadoEditarFilme
from estado_assinar import EstadoAssinar


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

pessoas = Pessoas()
pessoas.adicionar(Pessoa("Eduardo Betim", "107.879.469-31", "10/05/2000", True, "123"))
pessoas.adicionar(Pessoa("Alisson Fabra da Silva", "122.146.229-69", "18/09/2000", True, "123"))

estados = {"login": EstadoLogin(False, False),
           "cadastro_admin": EstadoCadastro(True, False),
           "cadastro_cliente": EstadoCadastro(False, False),
           "catalogo_admin": EstadoCatalogo(True, True, catalogo),
           "catalogo_assinante": EstadoCatalogo(False, True, catalogo),
           "catalogo_cliente": EstadoCatalogo(False, False, catalogo),
           "visualizar_filme_admin": EstadoVisualizarFilme(True, True),
           "visualizar_filme_cliente": EstadoVisualizarFilme(False, True),
           "visualizar_pessoa": EstadoVisualizarPessoa(True, True),
           "editar_pessoa": EstadoEditarPessoa(True, True),
           "editar_filme": EstadoEditarFilme(True, True),
           "assinar": EstadoAssinar(False, False)}

estados["editar_filme"].filme = catalogo.consultar("Harry Potter 2")
estados["editar_pessoa"].pessoa = pessoas.consultar("107.879.469-31")

estado = "visualizar_filme_admin"
while True:
    proximo_estado = estados[estado].run()
    estado = proximo_estado
    event, values = estados[estado].window.read()
    if event == sg.WIN_CLOSED:
        break
estados[estado].window.close()
