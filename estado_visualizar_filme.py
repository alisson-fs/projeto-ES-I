from estado import Estado
from filme import Filme
import PySimpleGUI as sg


class EstadoVisualizarFilme(Estado):
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
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text(f"Título: {self.__filme.titulo}", size=(30,1), font=("Helvetica",12))]
        linha2 = [sg.Text(f"ID: {self.__filme.id}", size=(30,1), font=("Helvetica",12))]   
        linha3 = [sg.Text(f"Duração: {self.__filme.duracao}", size=(30,1), font=("Helvetica",12))]
        linha4 = [sg.Text(f"Gênero: {self.__filme.genero}", size=(30,1), font=("Helvetica",12))]
        linha5 = [sg.Text(f"Classificação: {self.__filme.classificacao}", size=(30,1), font=("Helvetica",12))]
        if self.admin:
            linha6 = [sg.Button("Assistir"), sg.Button("Editar")]
        else:
            linha6 = [sg.Button("Assistir")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5, linha6]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

        if self.admin:
            return "visualizar_filme_admin"
        else:
            return "visualizar_filme_cliente"
