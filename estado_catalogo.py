from estado import Estado
from filme import Filme
import PySimpleGUI as sg


class EstadoCatalogo(Estado):
    def __init__(self, admin, assinante, catalogo):
        super().__init__(admin, assinante)
        self.__catalogo = catalogo

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Catálogo:", size=(30,1), font=("Helvetica",15))]
        linha2 = [sg.Listbox(values=self.__catalogo.gerar_lista(), size=(30, 6), key="filme")]
        if self.admin:      
            linha3 = [sg.Button("Sair"), sg.Button("Visualizar"), sg.Button("Adicionar filme"), sg.Button("Remover filme"), sg.Button("Gerenciar cadastros")]
        elif self.assinante:
            linha3 = [sg.Button("Sair"), sg.Button("Visualizar")]
        else:
            linha3 = [sg.Button("Sair"), sg.Button("Alugar"), sg.Button("Realizar assinatura")]
        self.container = [linha0, linha1, linha2, linha3]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

    def ler_evento(self, event, values):
        if values["filme"]:
            filme = self.__catalogo.consultar(values["filme"][0])
        if event == "Sair":
            self.window.close()
            return "login"
        if event == "Visualizar":
            self.window.close()
            self.__catalogo.atual = filme
            if self.admin:
                return "visualizar_filme_admin"
            else:
                return "visualizar_filme_cliente"
        if event == "Adicionar filme":
            self.window.close()
            return "adicionar_filme"
        if event == "Remover filme":
            self.window.close()
            self.__catalogo.remover(filme.titulo)
            return "catalogo_admin"
        if event == "Gerenciar cadastros":
            self.window.close()
            return "lista_pessoas"
        if event == "Realizar assinatura":
            self.window.close()
            return "assinar"
        if event == "Alugar":
            self.window.close()
            return "catalogo_cliente"
        if self.admin:
            return "catalogo_admin"
        elif self.assinante:
            return "catalogo_assinante"
        else:
            return "catalogo_cliente"
