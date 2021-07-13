from PySimpleGUI.PySimpleGUI import TRANSPARENT_BUTTON
from pessoa import Pessoa
from estado import Estado
import PySimpleGUI as sg


class EstadoGerenciarPessoas(Estado):
    def __init__(self, admin, assinante, registro_pessoas):
        super().__init__(admin, assinante)
        self.__registro_pessoas = registro_pessoas

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha0 = [sg.Text("Buscar clientes:", size=(30,1), font=("Helvetica",15))]
        linha1 = [sg.Text("CPF:", size=(30,1), font=("Helvetica",12))]
        linha2 = [sg.InputText("", key="pessoa")]
        linha3 = [sg.Text("ERRO: Cliente inválido!", size=(30,1), font=("Helvetica",12))]
        linha4 = [sg.Button("Voltar"), sg.Button("Visualizar"), sg.Button("Adicionar cliente"), sg.Button("Remover cliente")]
        if self.erro:
            self.container = [linha0, linha1, linha2, linha3, linha4]
        else:
            self.container = [linha0, linha1, linha2, linha4]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        self.erro = False

    def ler_evento(self, event, values):
        pessoa = self.__registro_pessoas.consultar(values["pessoa"])
        if event == "Voltar":
            self.window.close()
            return "catalogo_admin"
        if event == "Visualizar":
            self.window.close()
            if pessoa != None:
                self.__registro_pessoas.atual = pessoa
                return "visualizar_pessoa"
            else:
                self.erro = True
        if event == "Adicionar cliente":
            self.window.close()
            return "cadastro_admin"
        if event == "Remover cliente":
            self.window.close()
            if pessoa != None:
                self.__registro_pessoas.remover(pessoa.cpf)
                return "lista_pessoas"
            else:
                self.erro = True
        return "lista_pessoas"
