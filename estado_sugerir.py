from sugestao import Sugestao
from estado import Estado
import PySimpleGUI as sg
from sugestoes import Sugestoes


class EstadoSugerir(Estado):
    def __init__(self):
        super().__init__()
        self.__sugestoes = Sugestoes()

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Sugira um filme:", size=(30,1), font=("Helvetica",15))]
        linha2 = [sg.InputText("", key="sugestao")]
        linha3 = [sg.Text("ERRO: Sugestão inválida, você não pode colocar uma sugestão sem preencher ou maior do que 60 caracteres!",
                  size=(90,1), font=("Helvetica",12))]
        linha4 = [sg.Button("Voltar"), sg.Button("Sugerir")]
        if self.erro:
            self.container = [linha0, linha1, linha2, linha3, linha4]
        else:
            self.container = [linha0, linha1, linha2, linha4]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        self.erro = False

    def ler_evento(self, event, values):
        if event == "Voltar":
            self.window.close()
            return "catalogo_assinante"
        if event == "Sugerir":
            self.window.close()
            if values["sugestao"] and len(values["sugestao"]) <= 60:
                sugestao = values["sugestao"]
                self.__sugestoes.adicionar(Sugestao(sugestao))
                return "catalogo_assinante"
            else:
                self.erro = True
                return "sugerir"
        return "sugerir"

