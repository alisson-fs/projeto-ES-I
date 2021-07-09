from estado import Estado
import PySimpleGUI as sg


class EstadoLogin(Estado):
    def __init__(self, admin, assinante):
        super().__init__(admin, assinante)

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Nome:", justification="center")]
        linha2 = [sg.InputText("", key="nome")]
        linha3 = [sg.Text("Senha:", justification="center")]
        linha4 = [sg.InputText("", key="senha")]
        linha5 = [sg.Button("Cadastrar"), sg.Button("Entrar")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        return "login"
