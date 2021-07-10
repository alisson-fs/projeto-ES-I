from pessoa import Pessoa
from estado import Estado
import PySimpleGUI as sg


class EstadoPessoas(Estado):
    def __init__(self, admin, assinante, pessoas):
        super().__init__(admin, assinante)
        self.__pessoas = pessoas

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha0 = [sg.Text("Buscar clientes:", size=(30,1), font=("Helvetica",15))]
        linha1 = [sg.Text("CPF:", size=(30,1), font=("Helvetica",12))]
        linha2 = [sg.InputText("", key="pessoa")]
        linha3 = [sg.Text("ERRO: Cliente não encontrado!", size=(30,1), font=("Helvetica",12))]
        linha4 = [sg.Button("Voltar"), sg.Button("Visualizar"), sg.Button("Adicionar cliente"), sg.Button("Remover cliente")]
        self.container = [linha0, linha1, linha2, linha4]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

    def ler_evento(self, event, values):
        pessoa = self.__pessoas.consultar(values["pessoa"])
        if pessoa == None:
            pessoa = Pessoa(" -", " -", " -", " -")
        if event == "Voltar":
            self.window.close()
            return "catalogo_admin"
        if event == "Visualizar":
            self.window.close()
            self.__pessoas.atual = pessoa
            return "visualizar_pessoa"
        if event == "Adicionar cliente":
            self.window.close()
            return "cadastro_admin"
        if event == "Remover cliente":
            self.window.close()
            self.__pessoas.remover(pessoa.cpf)
            return "lista_pessoas"
        return "lista_pessoas"
