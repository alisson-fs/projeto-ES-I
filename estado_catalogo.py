from estado import Estado
from registro_pessoas import RegistroPessoas
from catalogo import Catalogo
from alugueis import Alugueis
import PySimpleGUI as sg


class EstadoCatalogo(Estado):
    def __init__(self):
        super().__init__()
        self.__registro_pessoas = RegistroPessoas()
        self.__catalogo = Catalogo()
        self.__alugueis = Alugueis()
        self.__mensagem_erro = ""

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Catálogo:", size=(30,1), font=("Helvetica",15))]
        linha2 = [sg.Listbox(values=self.__catalogo.gerar_lista(), size=(30, 6), key="filme")]
        linha3 = [sg.Text(self.__mensagem_erro, size=(30,1), font=("Helvetica",12))]
        if self.__registro_pessoas.atual.admin:      
            linha4 = [sg.Button("Sair"),
                      sg.Button("Visualizar"),
                      sg.Button("Adicionar filme"),
                      sg.Button("Remover filme"),
                      sg.Button("Gerenciar cadastros"),
                      sg.Button("Sugestões")]
        elif self.__registro_pessoas.atual.assinante:
            linha4 = [sg.Button("Sair"), sg.Button("Visualizar"), sg.Button("Sugerir Filme")]
        else:
            linha4 = [sg.Button("Sair"), sg.Button("Alugar"), sg.Button("Realizar assinatura"), sg.Button("Alugados")]
        if self.erro:
            self.container = [linha0, linha1, linha2, linha3, linha4]
        else:
            self.container = [linha0, linha1, linha2, linha4]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        self.erro = False

    def ler_evento(self, event, values):
        if event == "Sair":
            self.window.close()
            return "login"
        if event == "Visualizar":
            self.window.close()
            if values["filme"]:
                filme = self.__catalogo.consultar(values["filme"][0])
                self.__catalogo.atual = filme
                return "visualizar_filme"
            else:
                self.erro = True
                self.__mensagem_erro = "ERRO: Selecione uma opção."
        if event == "Adicionar filme":
            self.window.close()
            return "adicionar_filme"
        if event == "Remover filme":
            self.window.close()
            if values["filme"]:
                filme = self.__catalogo.consultar(values["filme"][0])
                self.__catalogo.remover(filme.titulo)
                return "catalogo"
            else:
                self.erro = True
                self.__mensagem_erro = "ERRO: Selecione uma opção."
        if event == "Gerenciar cadastros":
            self.window.close()
            return "lista_pessoas"
        if event == "Realizar assinatura":
            self.window.close()
            return "assinar"
        if event == "Alugar":
            self.window.close()
            if values["filme"]:
                filme = self.__catalogo.consultar(values["filme"][0])
                self.__catalogo.atual = filme
                if self.__alugueis.verifica_alugado(filme, self.__registro_pessoas.atual):
                    self.erro = True
                    self.__mensagem_erro = "ERRO: Filme já alugado."
                else:
                    return "alugar"
            else:
                self.erro = True
                self.__mensagem_erro = "ERRO: Selecione uma opção."
        if event == "Alugados":
            self.window.close()
            return "alugados"
        if event == "Sugestões":
            self.window.close()
            return "sugestoes"
        if event == "Sugerir Filme":
            self.window.close()
            return "sugerir"
        return "catalogo"
