from estado import Estado
from registro_pessoas import RegistroPessoas
import PySimpleGUI as sg


class EstadoVisualizarPessoa(Estado):
    def __init__(self):
        super().__init__()
        self.__registro_pessoas = RegistroPessoas()

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text(f"Nome: {self.__registro_pessoas.atual.nome}", size=(30,1), font=("Helvetica",12))]
        linha2 = [sg.Text(f"CPF: {self.__registro_pessoas.atual.cpf}", size=(30,1), font=("Helvetica",12))]   
        linha3 = [sg.Text(f"Data de nascimento: {self.__registro_pessoas.atual.nascimento}", size=(30,1), font=("Helvetica",12))]
        linha4 = [sg.Text(f"Administrador: {str(self.__registro_pessoas.atual.admin)}", size=(30,1), font=("Helvetica",12))]
        linha5 = [sg.Text(f"Assinante: {str(self.__registro_pessoas.atual.assinante)}", size=(30,1), font=("Helvetica",12))]
        linha6 = [sg.Button("Voltar"), sg.Button("Editar")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5, linha6]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

    def ler_evento(self, event, values):
        if event == "Editar":
            self.window.close()
            return "editar_pessoa"
        if event == "Voltar":
            self.window.close()
            return "lista_pessoas"
        return "visualizar_pessoa"
