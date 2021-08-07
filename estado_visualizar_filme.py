from estado import Estado
from filme import Filme
import PySimpleGUI as sg


class EstadoVisualizarFilme(Estado):
    def __init__(self, admin, assinante, catalogo):
        super().__init__(admin, assinante)
        self.__catalogo = catalogo
        self.__catalogo.atual = Filme(" -", " -", " -", " -", " -")

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text(f"Título: {self.__catalogo.atual.titulo}", size=(30,1), font=("Helvetica",12))]
        linha2 = [sg.Text(f"ID: {self.__catalogo.atual.id}", size=(30,1), font=("Helvetica",12))]   
        linha3 = [sg.Text(f"Duração: {self.__catalogo.atual.duracao}", size=(30,1), font=("Helvetica",12))]
        linha4 = [sg.Text(f"Gênero: {self.__catalogo.atual.genero}", size=(30,1), font=("Helvetica",12))]
        linha5 = [sg.Text(f"Classificação: {self.__catalogo.atual.classificacao}", size=(30,1), font=("Helvetica",12))]
        if self.admin:
            linha6 = [sg.Button("Voltar"), sg.Button("Assistir"), sg.Button("Editar")]
        else:
            linha6 = [sg.Button("Voltar"), sg.Button("Assistir")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5, linha6]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
 
    def ler_evento(self, event, values):
        if event == "Voltar":
            self.window.close()
            if self.admin:
                return "catalogo_admin"
            elif self.assinante:
                return "catalogo_assinante"
            else:
                return "catalogo_cliente"
        if event == "Editar":
            self.window.close()
            return "editar_filme"
        if event == "Assistir":
            self.window.close()
            if self.admin:
                return "visualizar_filme_admin"
            else:
                return "visualizar_filme_cliente"
        if self.admin:
            return "visualizar_filme_admin"
        else:
            return "visualizar_filme_cliente"
