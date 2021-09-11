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
from estado_comentarios import EstadoComentarios
from estado_comentar import EstadoComentar


sg.theme("DarkTeal10")

estados = {"login": EstadoLogin(),
           "cadastro_admin": EstadoCadastro(),
           "cadastro_cliente": EstadoCadastro(),
           "catalogo_admin": EstadoCatalogo(),
           "catalogo_assinante": EstadoCatalogo(),
           "catalogo_cliente": EstadoCatalogo(),
           "visualizar_filme_admin": EstadoVisualizarFilme(),
           "visualizar_filme_assinante": EstadoVisualizarFilme(),
           "visualizar_filme_cliente": EstadoVisualizarFilme(),
           "visualizar_pessoa": EstadoVisualizarPessoa(),
           "editar_pessoa": EstadoEditarPessoa(),
           "editar_filme": EstadoEditarFilme(),
           "assinar": EstadoAssinar(),
           "adicionar_filme": EstadoAdicionarFilme(),
           "lista_pessoas": EstadoGerenciarPessoas(),
           "alugar": EstadoAlugar(),
           "alugados": EstadoAlugados(),
           "avaliar": EstadoAvaliar(),
           "sugerir": EstadoSugerir(),
           "sugestoes": EstadoSugestoes(),
           "comentarios": EstadoComentarios(),
           "comentar": EstadoComentar()}

estado = "login"
while True:
    estados[estado].run()
    event, values = estados[estado].window.read()
    proximo_estado = estados[estado].ler_evento(event, values)
    estado = proximo_estado
    if event == sg.WIN_CLOSED:
        break
