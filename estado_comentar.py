from comentario import Comentario
from estado import Estado
import PySimpleGUI as sg


class EstadoComentar(Estado):
    def __init__(self, admin, assinante, catalogo, comentarios):
        super().__init__(admin, assinante)
        self.__catalogo = catalogo
        self.__comentarios = comentarios

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Adicione seu comentario:", size=(30,1), font=("Helvetica",15))]
        linha2 = [sg.InputText("", key="comentario")]
        linha3 = [sg.Text("ERRO: Sugestão inválida, você não pode colocar um comentario sem preencher ou maior do que 200 caracteres!",
                  size=(90,1), font=("Helvetica",12))]
        linha4 = [sg.Button("Voltar"), sg.Button("Salvar")]
        if self.erro:
            self.container = [linha0, linha1, linha2, linha3, linha4]
        else:
            self.container = [linha0, linha1, linha2, linha4]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        self.erro = False

    def ler_evento(self, event, values):
        if event == "Voltar":
            self.window.close()
            return "comentarios"
        if event == "Salvar":
            self.window.close()
            if values["comentario"] and len(values["comentario"]) <= 200:
                titulo = self.__catalogo.atual.titulo
                comentario = values["comentario"]
                self.__comentarios.adicionar(Comentario(titulo, comentario))
                return "comentarios"
            else:
                self.erro = True
                return "comentar"
        return "sugerir"

