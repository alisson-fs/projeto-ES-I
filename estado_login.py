from estado import Estado
from pessoa import Pessoa
from registro_pessoas import RegistroPessoas
import datetime
import PySimpleGUI as sg


class EstadoLogin(Estado):
    def __init__(self):
        super().__init__()
        self.__registro_pessoas = RegistroPessoas()

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("CPF:")]
        linha2 = [sg.InputText("", key="cpf")]
        linha3 = [sg.Text("Senha:")]
        linha4 = [sg.InputText("", key="senha")]
        linha5 = [sg.Text("ERRO: Cadastro inválido!", size=(30,1), font=("Helvetica",10))]
        linha6 = [sg.Button("Cadastrar"), sg.Button("Entrar")]
        self.container = [linha0, linha1, linha2, linha3, linha4, linha6]
        if self.erro:
            self.container.insert(5, linha5)
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        self.erro = False

    def ler_evento(self, event, values):
        if event == "Cadastrar":
            self.window.close()
            return "cadastro"
        if event == "Entrar":
            pessoa = self.__registro_pessoas.consultar(values["cpf"])
            self.window.close()
            if isinstance(pessoa, Pessoa):
                if pessoa.cpf == values["cpf"] and pessoa.senha == values["senha"]:
                    self.__registro_pessoas.atual = pessoa
                    if pessoa.assinante and datetime.date.today() > datetime.datetime.strptime(pessoa.vencimento_assinatura, '%Y-%m-%d').date():
                        pessoa.assinante = False
                    return "catalogo"
                else:
                    self.erro = True
                    return "login"
            else:
                self.erro = True
                return "login"
        return "login"
