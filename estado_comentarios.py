from estado import Estado
import PySimpleGUI as sg
from catalogo import Catalogo
from comentarios import Comentarios


class EstadoComentarios(Estado):
    def __init__(self):
        super().__init__()
        self.__catalogo = Catalogo()
        self.__comentarios = Comentarios()

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Comentarios:", size=(30,1), font=("Helvetica",15))]
        linha3 = [sg.Button("Voltar"), sg.Button("Comentar")]
        self.container = [linha0, linha1]
        for comentario in self.__comentarios.gerar_lista(self.__catalogo.atual.titulo):
            linha = [sg.Text("- "+comentario+"\n", size=(30,1), font=("Helvetica",12))]
            self.container.append(linha)
        self.container.append(linha3)
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

    def ler_evento(self, event, values):
        if event == "Voltar":
            self.window.close()
            return "visualizar_filme"
        if event == "Comentar":
            self.window.close()
            return "comentar"
        return "comentarios"
