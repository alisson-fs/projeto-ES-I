from estado import Estado
from catalogo import Catalogo
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
            linha3 = [sg.Button("Visualizar"), sg.Button("Adicionar Filme"), sg.Button("Remover Filme")]
        elif self.assinante:
            linha3 = [sg.Button("Visualizar")]
        else:
            linha3 = [sg.Button("Alugar"), sg.Button("Realizar Assinatura")]
        self.container = [linha0, linha1, linha2, linha3]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

        if self.admin:      
            return "catalogo_admin"
        elif self.assinante:
            return "catalogo_assinante"
        else:
            return "catalogo_cliente"
