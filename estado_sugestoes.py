from estado import Estado
import PySimpleGUI as sg
from sugestoes import Sugestoes

class EstadoSugestoes(Estado):
    def __init__(self):
        super().__init__()
        self.__sugestoes = Sugestoes()

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Sugestões:", size=(30,1), font=("Helvetica",15))]
        linha2 = [sg.Listbox(values=self.__sugestoes.gerar_lista(), size=(30, 6), key="sugestao")]
        linha3 = [sg.Text("ERRO: Selecione uma sugestão!", size=(30,1), font=("Helvetica",12))]
        linha4 = [sg.Button("Voltar"), sg.Button("Remover")]
        if self.erro:
            self.container = [linha0, linha1, linha2, linha3, linha4]
        else:
            self.container = [linha0, linha1, linha2, linha4]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        self.erro = False

    def ler_evento(self, event, values):
        if event == "Voltar":
            self.window.close()
            return "catalogo_admin"
        if event == "Remover":
            self.window.close()
            if values["sugestao"]:
                self.__sugestoes.remover(values["sugestao"][0])
            else:
                self.erro = True
            return "sugestoes"
        return "sugestoes"
