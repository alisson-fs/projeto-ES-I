from estado import Estado
from pessoa import Pessoa
import PySimpleGUI as sg


class EstadoVisualizarPessoa(Estado):
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
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text(f"Nome: {self.__pessoa.nome}", size=(30,1), font=("Helvetica",12))]
        linha2 = [sg.Text(f"CPF: {self.__pessoa.cpf}", size=(30,1), font=("Helvetica",12))]   
        linha3 = [sg.Text(f"Data de nascimento: {self.__pessoa.nascimento}", size=(30,1), font=("Helvetica",12))]
        linha4 = [sg.Text(f"Administrador: {str(self.__pessoa.admin)}", size=(30,1), font=("Helvetica",12))]
        linha5 = [sg.Button("Editar")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

        return "visualizar_pessoa"