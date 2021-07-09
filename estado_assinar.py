from estado import Estado
import PySimpleGUI as sg


class EstadoAssinar(Estado):
    def __init__(self, admin, assinante):
        super().__init__(admin, assinante)

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Nome no cartão:")]
        linha2 = [sg.InputText("", key="nome_cartao")]
        linha3 = [sg.Text("Número do cartão:")]
        linha4 = [sg.InputText("", key="num_cartao")]
        linha5 = [sg.Text("Validade:")]
        linha6 = [sg.InputCombo(tuple(range(1, 13)), key="mes", size=(5,1)),
                  sg.Text("/"),
                  sg.InputCombo(tuple(range(50, 10, -1)), key="ano", size=(5,1))]
        linha7 = [sg.Text("CVV:")]
        linha8 = [sg.InputText("", key="cvv")]
        linha9 = [sg.Button("Assinar")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

        return "assinar"
