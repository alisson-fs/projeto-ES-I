from estado_cadastro import EstadoCadastro
import PySimpleGUI as sg
from estado_login import EstadoLogin


sg.theme("DarkTeal10")
estados = {"login": EstadoLogin(),
           "cadastro": EstadoCadastro()}

estado = "cadastro"
while True:
    proximo_estado = estados[estado].run()
    estado = proximo_estado
    event, values = estados[estado].window.read()
    if event == sg.WIN_CLOSED:
        break
estados[estado].window.close()