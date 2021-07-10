from estado import Estado
from filme import Filme
from catalogo import Catalogo
import PySimpleGUI as sg


class EstadoAdicionarFilme(Estado):
    def __init__(self, admin, assinante, catalogo):
        super().__init__(admin, assinante)
        self.__catalogo = catalogo
        self.__catalogo.atual = Filme(" -", " -", " -", " -", " -")

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Título:")]
        linha2 = [sg.InputText("", key="titulo")]
        linha3 = [sg.Text("ID:")]
        linha4 = [sg.InputText("", key="id")]
        linha5 = [sg.Text("Duração:")]
        linha6 = [sg.InputText("", key="duracao")]
        linha7 = [sg.Text("Gênero:")]
        linha8 = [sg.InputText("", key="genero")]
        linha9 = [sg.Text("Classificação:")]
        linha10 = [sg.InputText("", key="classificacao")]
        linha11 = [sg.Text("ERRO: Campos não preenchidos!", font=("Helvetica",10))]
        linha12 = [sg.Button("Cancelar"), sg.Button("Salvar")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5,
                          linha6, linha7, linha8, linha9, linha10, linha12]
        if self.erro:
                self.container.insert(11, linha11)
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        self.erro = False

    def ler_evento(self, event, values):
        if event == "Salvar":
            self.window.close()
            if (values["titulo"] == "" or values["id"] == "" or values["duracao"] == ""
                or values["genero"] == "" or values["classificacao"] == ""):
                self.erro = True
            else:
                titulo = values["titulo"]
                id = values["id"]
                duracao = values["duracao"]
                genero = values["genero"]
                classificacao = values["classificacao"]
                filme = Filme(titulo, id, duracao, genero, classificacao)
                self.__catalogo.adicionar(filme)
                return "catalogo_admin"
        if event == "Cancelar":
            self.window.close()
            return "catalogo_admin"
        return "catalogo_admin"
