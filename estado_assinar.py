from estado import Estado
from cartao import Cartao
from pessoa import Pessoa
import PySimpleGUI as sg
import datetime


class EstadoAssinar(Estado):
    def __init__(self, admin, assinante, registro_pessoas):
        super().__init__(admin, assinante)
        self.__registro_pessoas = registro_pessoas

    def run(self):
        linha0 = [sg.Text("UFLIX", size=(30,1), font=("Helvetica",25))]
        linha1 = [sg.Text("CPF:")]
        linha2 = [sg.InputText("", key="cpf")]
        linha3 = [sg.Text("ERRO: CPF inválido!", size=(30,1), font=("Helvetica",10))]
        linha4 = [sg.Text("Nome no cartão:")]
        linha5 = [sg.InputText("", key="nome_cartao")]
        linha6 = [sg.Text("Número do cartão:")]
        linha7 = [sg.InputText("", key="num_cartao")]
        linha8 = [sg.Text("Validade:")]
        linha9 = [sg.InputCombo(tuple(range(1, 13)), key="mes", size=(5,1)),
                  sg.Text("/"),
                  sg.InputCombo(tuple(range(50, 10, -1)), key="ano", size=(5,1))]
        linha10 = [sg.Text("CVV:")]
        linha11 = [sg.InputText("", key="cvv")]
        linha12 = [sg.Button("Cancelar"), sg.Button("Assinar")]
        self.container = [linha0, linha1, linha2, linha4, linha5, linha6, linha7,
                          linha8, linha9, linha10, linha11, linha12]
        if self.erro:
            self.container.insert(3, linha3)
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

    def ler_evento(self, event, values):
        if event == "Assinar":
            pessoa = self.__registro_pessoas.consultar(values["cpf"])
            self.window.close()
            if isinstance(pessoa, Pessoa):
                nome_cartao = values["nome_cartao"]
                num_cartao = values["num_cartao"]
                validade = values["mes"]+"/"+values["ano"]
                cvv = values["cvv"]
                cartao = Cartao(nome_cartao, num_cartao, validade, cvv)
                pessoa.cartao = cartao
                pessoa.assinante = True
                pessoa.vencimento_assinatura = datetime.date.today()+datetime.timedelta(days=30)
                return "catalogo_assinante"
            else:
                self.erro = True
                return "assinar"
        if event == "Cancelar":
            self.window.close()
            return "catalogo_cliente"
        return "assinar"
