from estado import Estado
from filme import Filme
import PySimpleGUI as sg


class EstadoEditarFilme(Estado):
    def __init__(self, admin, assinante, catalogo):
        super().__init__(admin, assinante)
        self.__catalogo = catalogo
        self.__catalogo.atual = Filme(" -", " -", " -", " -", " -")

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica", 25))]
        linha1 = [sg.Text("Título:")]
        linha2 = [sg.InputText(f"{self.__catalogo.atual.titulo}", key="titulo")]
        linha3 = [sg.Text("ID:")]
        linha4 = [sg.InputText(f"{self.__catalogo.atual.id}", key="id")]  
        linha5 = [sg.Text("Duração:")]
        linha6 = [sg.InputText(f"{self.__catalogo.atual.duracao}", key="duracao")]
        linha7 = [sg.Text("Gênero:")]
        linha8 = [sg.InputText(f"{str(self.__catalogo.atual.genero)}", key="genero")]
        linha9 = [sg.Text("Classificação:")]
        linha10 = [sg.InputText(f"{str(self.__catalogo.atual.classificacao)}", key="classificacao")]
        linha11 = [sg.Button("Cancelar"), sg.Button("Salvar")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5,
                          linha6, linha7, linha8, linha9, linha10, linha11]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

    def ler_evento(self, event, values):
        if event == "Salvar":
            self.window.close()
            titulo = values["titulo"]
            id = values["id"]
            duracao = values["duracao"]
            genero = values["genero"]
            classificacao = values["classificacao"]
            self.__catalogo.atualizar(titulo, id, duracao, genero, classificacao)
            return "visualizar_filme_admin"

        if event == "Cancelar":
            self.window.close()
            return "visualizar_filme_admin"
        return "editar_filme"
