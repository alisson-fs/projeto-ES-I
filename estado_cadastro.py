from estado import Estado
import PySimpleGUI as sg


class EstadoCadastro(Estado):
    def __init__(self, admin, assinante):
        super().__init__(admin, assinante)

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Nome:")]
        linha2 = [sg.InputText("", key="nome")]
        linha3 = [sg.Text("CPF:")]
        linha4 = [sg.InputText("", key="cpf")]
        linha5 = [sg.Text("Nascimento:")]
        linha6 = [sg.InputCombo(tuple(range(1, 32)), key="dia", size=(5,1)),
                  sg.Text("/"),
                  sg.InputCombo(tuple(range(1, 13)), key="mes", size=(5,1)),
                  sg.Text("/"),
                  sg.InputCombo(tuple(range(2021, 1920, -1)), key="ano", size=(5,1))]
        linha7 = [sg.Text("Senha:")]
        linha8 = [sg.InputText("", key="senha1")]
        linha9 = [sg.Text("Confirmar senha:")]
        linha10 = [sg.InputText("", key="senha2")]
        linha11 = [sg.Checkbox("Administrador", key="admin", size=(15,1))]
        linha12 = [sg.Button("Salvar")]
        if self.admin:
            self.container = [linha0, linha1, linha2, linha3, linha4, linha5, linha6,
                              linha7, linha8, linha9, linha10, linha11, linha12]
        else:
            self.container = [linha0, linha1, linha2, linha3, linha4, linha5, linha6,
                              linha7, linha8, linha9, linha10, linha12]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        
        if self.admin:
            return "cadastro_admin"
        else:
            return "cadastro_cliente"
