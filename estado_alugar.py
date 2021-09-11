from estado import Estado
from cartao import Cartao
from pessoa import Pessoa
from aluguel import Aluguel
from registro_pessoas import RegistroPessoas
from catalogo import Catalogo
from alugueis import Alugueis
import PySimpleGUI as sg
import datetime


class EstadoAlugar(Estado):
    def __init__(self):
        super().__init__()
        self.__registro_pessoas = RegistroPessoas()
        self.__catalogo = Catalogo()
        self.__alugueis = Alugueis()

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
        linha12 = [sg.Button("Cancelar"), sg.Button("Alugar")]
        self.container = [linha0, linha1, linha2, linha4, linha5, linha6, linha7,
                          linha8, linha9, linha10, linha11, linha12]
        if self.erro:
            self.container.insert(3, linha3)
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))
        self.erro = False

    def ler_evento(self, event, values):
        if event == "Alugar":
            pessoa = self.__registro_pessoas.consultar(values["cpf"])
            self.window.close()
            if isinstance(pessoa, Pessoa):
                nome_cartao = values["nome_cartao"]
                num_cartao = values["num_cartao"]
                validade = str(values["mes"])+"/"+str(values["ano"])
                cvv = values["cvv"]
                cartao = Cartao(nome_cartao, num_cartao, validade, cvv)
                pessoa.cartao = cartao
                inicio = datetime.date.today()
                fim = datetime.date.today()+datetime.timedelta(days=7)
                aluguel = Aluguel(inicio, fim, self.__catalogo.atual.titulo, self.__registro_pessoas.atual.cpf)
                self.__alugueis.adicionar(aluguel)
                return "catalogo"
            else:
                self.erro = True
        if event == "Cancelar":
            self.window.close()
            return "catalogo"
        return "alugar"
