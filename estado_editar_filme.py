from estado import Estado
from filme import Filme
import PySimpleGUI as sg


class EstadoEditarFilme(Estado):
    def __init__(self, admin, assinante):
        super().__init__(admin, assinante)
        self.__filme = Filme(" -", " -", " -", " -", " -")

    @property
    def filme(self):
        return self.__filme

    @filme.setter
    def filme(self, filme):
        self.__filme = filme

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica", 25))]
        linha1 = [sg.Text("Título:")]
        linha2 = [sg.InputText(f"{self.__filme.titulo}", key="titulo")]
        linha3 = [sg.Text("ID:")]
        linha4 = [sg.InputText(f"{self.__filme.id}", key="ID")]  
        linha5 = [sg.Text("Duração:")]
        linha6 = [sg.InputText(f"{self.__filme.duracao}", key="duracao")]
        linha7 = [sg.Text("Gênero:")]
        linha8 = [sg.InputText(f"{str(self.__filme.genero)}", key="genero")]
        linha9 = [sg.Text("Classificação:")]
        linha10 = [sg.InputText(f"{str(self.__filme.classificacao)}", key="classificacao")]
        linha11 = [sg.Button("Cancelar"), sg.Button("Salvar")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5,
                          linha6, linha7, linha8, linha9, linha10, linha11]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

        return "editar_filme"