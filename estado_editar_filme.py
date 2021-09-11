from estado import Estado
from filme import Filme
from catalogo import Catalogo
import PySimpleGUI as sg


class EstadoEditarFilme(Estado):
    def __init__(self):
        super().__init__()
        self.__catalogo = Catalogo()
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
            self.__catalogo.atual.titulo = values["titulo"]
            self.__catalogo.atual.id = values["id"]
            self.__catalogo.atual.duracao = values["duracao"]
            self.__catalogo.atual.genero = values["genero"]
            self.__catalogo.atual.classificacao = values["classificacao"]
            self.__catalogo.atual.n_avaliacoes = self.__catalogo.atual.n_avaliacoes
            self.__catalogo.atual.soma_avaliacoes = self.__catalogo.atual.soma_avaliacoes
            self.__catalogo.atualizar(self.__catalogo.atual.titulo,
                                      self.__catalogo.atual.id,
                                      self.__catalogo.atual.duracao,
                                      self.__catalogo.atual.genero,
                                      self.__catalogo.atual.classificacao,
                                      self.__catalogo.atual.n_avaliacoes,
                                      self.__catalogo.atual.soma_avaliacoes)
            return "visualizar_filme_admin"

        if event == "Cancelar":
            self.window.close()
            return "visualizar_filme_admin"
        return "editar_filme"
