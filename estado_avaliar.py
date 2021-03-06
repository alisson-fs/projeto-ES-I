from estado import Estado
from catalogo import Catalogo
import PySimpleGUI as sg


class EstadoAvaliar(Estado):
    def __init__(self):
        super().__init__()
        self.__catalogo = Catalogo()

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica", 25))]
        linha1 = [sg.Text("Avaiação:")]
        notas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        linha2 = [sg.Listbox(values=notas, size=(30, 6), key="nota")]
        linha3 = [sg.Text("ERRO: Selecione uma opção.", size=(30,1), font=("Helvetica",12))]
        linha4 = [sg.Button("Cancelar"), sg.Button("Avaliar")]
        if self.erro:
            self.container = [linha0, linha1, linha2, linha3, linha4]
        else:
            self.container = [linha0, linha1, linha2, linha4]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        self.erro = False

    def ler_evento(self, event, values):
        if event == "Avaliar":
            self.window.close()
            if values["nota"]:
                nota = values["nota"][0]
                self.__catalogo.avaliar(nota)
                return "visualizar_filme"
            else:
                self.erro = True
        if event == "Cancelar":
            self.window.close()
            return "visualizar_filme"
        return "avaliar"
