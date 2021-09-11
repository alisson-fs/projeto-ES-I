from estado import Estado
from pessoa import Pessoa
import PySimpleGUI as sg
from registro_pessoas import RegistroPessoas


class EstadoEditarPessoa(Estado):
    def __init__(self):
        super().__init__()
        self.__registro_pessoas = RegistroPessoas()
        self.__registro_pessoas.atual = Pessoa(" -", " -", " -", " -")

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica", 25))]
        linha1 = [sg.Text("Nome:")]
        linha2 = [sg.InputText(f"{self.__registro_pessoas.atual.nome}", key="nome")]
        linha3 = [sg.Text("CPF:")]
        linha4 = [sg.InputText(f"{self.__registro_pessoas.atual.cpf}", key="cpf")]   
        linha5 = [sg.Text("Data de nascimento:")]
        linha6 = [sg.InputCombo(tuple(range(1, 32)), key="dia", size=(5,1)),
                  sg.Text("/"),
                  sg.InputCombo(tuple(range(1, 13)), key="mes", size=(5,1)),
                  sg.Text("/"),
                  sg.InputCombo(tuple(range(2021, 1920, -1)), key="ano", size=(5,1))]
        
        linha15 = [sg.Checkbox("Administrador", key="admin", size=(15,1))]
        linha16 = [sg.Button("Cancelar"), sg.Button("Salvar")]
        self.container = [linha0, linha1, linha2, linha3, linha4,
                          linha5, linha6, linha15, linha16]
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

    def ler_evento(self, event, values):
        if event == "Salvar":
            self.window.close()
            self.__registro_pessoas.atual.nome = values["nome"]
            self.__registro_pessoas.atual.cpf = values["cpf"]
            self.__registro_pessoas.atual.nascimento = str(values["dia"])+"/"+str(values["mes"])+"/"+str(values["ano"])
            self.__registro_pessoas.atual.admin = values["admin"]
            self.__registro_pessoas.atualizar(self.__registro_pessoas.atual.nome,
                                              self.__registro_pessoas.atual.cpf,
                                              self.__registro_pessoas.atual.nascimento,
                                              self.__registro_pessoas.atual.admin,
                                              self.__registro_pessoas.atual.assinante)
            return "visualizar_pessoa"
        if event == "Cancelar":
            self.window.close()
            return "visualizar_pessoa"
        return "editar_pessoa"
