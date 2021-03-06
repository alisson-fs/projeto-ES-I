from estado import Estado
from filme import Filme
import PySimpleGUI as sg
from catalogo import Catalogo
from registro_pessoas import RegistroPessoas


class EstadoVisualizarFilme(Estado):
    def __init__(self):
        super().__init__()
        self.__catalogo = Catalogo()
        self.__catalogo.atual = Filme(" -", " -", " -", " -", " -")
        self.__registro_pessoas = RegistroPessoas()

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text(f"Título: {self.__catalogo.atual.titulo}", size=(30,1), font=("Helvetica",12))]
        linha2 = [sg.Text(f"ID: {self.__catalogo.atual.id}", size=(30,1), font=("Helvetica",12))]   
        linha3 = [sg.Text(f"Duração: {self.__catalogo.atual.duracao}", size=(30,1), font=("Helvetica",12))]
        linha4 = [sg.Text(f"Gênero: {self.__catalogo.atual.genero}", size=(30,1), font=("Helvetica",12))]
        linha5 = [sg.Text(f"Classificação: {self.__catalogo.atual.classificacao}", size=(30,1), font=("Helvetica",12))]
        if self.__catalogo.atual.n_avaliacoes == 0:
            nota = 0
        else:
            nota = self.__catalogo.atual.soma_avaliacoes/self.__catalogo.atual.n_avaliacoes
        n_notas = self.__catalogo.atual.n_avaliacoes
        linha6 = [sg.Text(f"Avaliação: Nota {nota:.1f}/10 de {n_notas} avaliações.", size=(40,1), font=("Helvetica",12))]
        if self.__registro_pessoas.atual.admin:
            linha7 = [sg.Button("Voltar"), sg.Button("Assistir"), sg.Button("Comentarios"), sg.Button("Editar")]
        else:
            linha7 = [sg.Button("Voltar"), sg.Button("Assistir"), sg.Button("Comentarios"), sg.Button("Avaliar")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5, linha6, linha7]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
 
    def ler_evento(self, event, values):
        if event == "Voltar":
            self.window.close()
            return "catalogo"
        if event == "Editar":
            self.window.close()
            return "editar_filme"
        if event == "Assistir":
            self.window.close()
            return "visualizar_filme"
        if event == "Avaliar":
            self.window.close()
            return "avaliar"
        if event == "Comentarios":
            self.window.close()
            return "comentarios"
        return "visualizar_filme"
