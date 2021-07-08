from tkinter.constants import RIGHT
from estado import Estado
import PySimpleGUI as sg


class EstadoCadastro(Estado):
    def __init__(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Nome:"), sg.InputText("", key="nome")]
        linha2 = [sg.Text("CPF:"), sg.InputText("", key="cpf")]
        linha3 = [sg.Text("Nascimento:"),
                  sg.InputCombo(tuple(range(1, 32)), key="dia", size=(5,1)),
                  sg.Text("/"),
                  sg.InputCombo(tuple(range(1, 13)), key="mes", size=(5,1)),
                  sg.Text("/"),
                  sg.InputCombo(tuple(range(2021, 1920, -1)), key="ano", size=(5,1))]
        linha4 = [sg.Text("Senha:"), sg.InputText("", key="senha1")]
        linha5 = [sg.Text("Confirmar senha:"), sg.InputText("", key="senha2")]
        linha6 = [sg.Checkbox("Administrador", key="admin", size=(15,1))]
        linha7 = [sg.Button("Salvar")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5, linha6, linha7]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

    def run(self):
        return "cadastro"
