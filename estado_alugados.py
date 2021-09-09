from estado import Estado
import PySimpleGUI as sg


class EstadoAlugados(Estado):
    def __init__(self, admin, assinante, registro_pessoas, catalogo, alugueis):
        super().__init__(admin, assinante)
        self.__registro_pessoas = registro_pessoas
        self.__catalogo = catalogo
        self.__alugueis = alugueis

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Filmes alugados:", size=(30,1), font=("Helvetica",15))]
        linha2 = [sg.Listbox(values=self.__alugueis.gerar_lista(self.__registro_pessoas.atual.cpf), size=(30, 6), key="filme")]
        linha3 = [sg.Text("ERRO: Selecione uma opção.", size=(30,1), font=("Helvetica",12))]     
        linha4 = [sg.Button("Catálogo"), sg.Button("Visualizar")]
        if self.erro:
            self.container = [linha0, linha1, linha2, linha3, linha4]
        else:
            self.container = [linha0, linha1, linha2, linha4]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        self.erro = False

    def ler_evento(self, event, values):
        if event == "Catálogo":
            self.window.close()
            return "catalogo_cliente"
        if event == "Visualizar":
            self.window.close()
            if values["filme"]:
                filme = self.__catalogo.consultar(values["filme"][0])
                self.__catalogo.atual = filme
                return "visualizar_filme_cliente"
            else:
                self.erro = True
        return "alugados"
