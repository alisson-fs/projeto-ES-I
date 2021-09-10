from estado import Estado
import PySimpleGUI as sg


class EstadoComentarios(Estado):
    def __init__(self, admin, assinante, registro_pessoas, comentarios):
        super().__init__(admin, assinante)
        self.__registro_pessoas = registro_pessoas
        self.__comentarios = comentarios

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Comentarios:", size=(30,1), font=("Helvetica",15))]
        linha3 = [sg.Button("Voltar"), sg.Button("Comentar")]
        self.container = [linha0, linha1]
        for comentario in self.__comentarios.gerar_lista():
            linha = [sg.Text("- "+comentario+"\n", size=(30,1), font=("Helvetica",12))]
            self.container.append(linha)
        self.container.append(linha3)
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

    def ler_evento(self, event, values):
        if event == "Voltar":
            self.window.close()
            if self.__registro_pessoas.atual.admin:
                return "visualizar_filme_admin"
            else:
                return "visualizar_filme_assinante"
        if event == "Comentar":
            self.window.close()
            return "comentar"
        return "comentarios"
