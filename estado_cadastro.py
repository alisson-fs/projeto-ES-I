from estado import Estado
from pessoa import Pessoa
from registro_pessoas import RegistroPessoas
import PySimpleGUI as sg


class EstadoCadastro(Estado):
    def __init__(self):
        super().__init__()
        self.__registro_pessoas = RegistroPessoas()

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("Nome:")]
        linha2 = [sg.InputText("", key="nome")]
        linha3 = [sg.Text("CPF:")]
        linha4 = [sg.InputText("", key="cpf")]
        linha5 = [sg.Text("Nascimento:")]
        linha6 = [sg.InputCombo(tuple(range(1, 32)), key="dia", size=(5,1)),
                  sg.Text("/"),
                  sg.InputCombo(tuple(range(1, 13)), key="mes", size=(5,1)),
                  sg.Text("/"),
                  sg.InputCombo(tuple(range(2021, 1920, -1)), key="ano", size=(5,1))]
        linha7 = [sg.Text("Senha:")]
        linha8 = [sg.InputText("", key="senha1")]
        linha9 = [sg.Text("Confirmar senha:")]
        linha10 = [sg.InputText("", key="senha2")]
        linha11 = [sg.Text("ERRO: Senhas não compatíveis!", font=("Helvetica",10))]
        linha12 = [sg.Checkbox("Administrador", key="admin", size=(15,1))]
        linha13 = [sg.Button("Cancelar"), sg.Button("Salvar")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha5,
                          linha6, linha7, linha8, linha9, linha10, linha13]
        if self.erro:
                self.container.insert(11, linha11)
        if self.__registro_pessoas.atual.admin:
            if self.erro:
                self.container.insert(12, linha12)
            else:
                self.container.insert(11, linha12)

        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        self.erro = False

    def ler_evento(self, event, values):
        if event == "Salvar":
            senha1 = values["senha1"]
            senha2 = values["senha2"]
            self.window.close()
            if senha1 == senha2:
                nome = values["nome"]
                cpf = values["cpf"]
                nascimento = str(values["dia"])+"/"+str(values["mes"])+"/"+str(values["ano"])
                if self.__registro_pessoas.atual.admin:
                    admin = values["admin"]
                else:
                    admin = False
                senha = senha1
                vencimento_assinatura = "1900-01-01"
                pessoa = Pessoa(nome, cpf, nascimento, senha, vencimento_assinatura, admin)
                self.__registro_pessoas.adicionar(pessoa)
                if self.__registro_pessoas.atual.admin:
                    return "lista_pessoas"
                else:
                    return "login"
            else:
                self.erro = True
                return "cadastro"
        if event == "Cancelar":
            self.window.close()
            if self.__registro_pessoas.atual.admin:
                return "lista_pessoas"
            else:
                return "login"
        return "cadastro"
