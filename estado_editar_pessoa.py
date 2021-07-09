from estado import Estado
from pessoa import Pessoa
import PySimpleGUI as sg


class EstadoEditarPessoa(Estado):
    def __init__(self, admin, assinante):
        super().__init__(admin, assinante)
        self.__pessoa = Pessoa(" -", " -", " -", " -", " -")

    @property
    def pessoa(self):
        return self.__pessoa

    @pessoa.setter
    def pessoa(self, pessoa):
        self.__pessoa = pessoa

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica", 25))]
        linha1 = [sg.Text("Nome:")]
        linha2 = [sg.InputText(f"{self.__pessoa.nome}", key="nome")]
        linha3 = [sg.Text("CPF:")]
        linha4 = [sg.InputText(f"{self.__pessoa.cpf}", key="cpf")]   
        linha5 = [sg.Text("Data de nascimento:")]
        linha6 = [sg.InputText(f"{self.__pessoa.nascimento}", key="nascimento")]
        linha7 = [sg.Text("Administrador:")]
        linha8 = [sg.InputText(f"{str(self.__pessoa.admin)}", key="admin")]
        linha9 = [sg.Button("Cancelar"), sg.Button("Salvar")]
        self.container = [linha0, linha1, linha2, linha3, linha4,
                          linha5, linha6, linha7, linha8, linha9]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

        return "editar_pessoa"
