from estado import Estado
from pessoa import Pessoa
import PySimpleGUI as sg


class EstadoEditarPessoa(Estado):
    def __init__(self, admin, assinante, registro_pessoas):
        super().__init__(admin, assinante)
        self.__registro_pessoas = registro_pessoas
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
        linha7 = [sg.Text("Nome no cartão:")]
        linha8 = [sg.InputText(f"{self.__registro_pessoas.atual.cartao.nome_cartao}", key="nome_cartao")]
        linha9 = [sg.Text("Número do cartão:")]
        linha10 = [sg.InputText(f"{self.__registro_pessoas.atual.cartao.num_cartao}", key="num_cartao")]
        linha11 = [sg.Text("Validade do cartão:")]
        linha12 = [sg.InputCombo(tuple(str(range(1, 13))), key="mes_cartao", size=(5,1)),
                   sg.Text("/"),
                   sg.InputCombo(tuple(str(range(2021, 1920, -1))), key="ano_cartao", size=(5,1))]
        linha13 = [sg.Text("CVV cartão:")]
        linha14 = [sg.InputText(f"{self.__registro_pessoas.atual.cartao.cvv}", key="cvv")]
        linha15 = [sg.Checkbox("Administrador", key="admin", size=(15,1))]
        linha16 = [sg.Button("Cancelar"), sg.Button("Salvar")]
        self.container = [linha0, linha1, linha2, linha3, linha4,
                          linha5, linha6, linha15, linha16]
        if self.__registro_pessoas.atual.assinante:
            linhas = [linha7, linha8, linha9, linha10, linha11, linha12, linha13, linha14]
            for i in range(7, 15):
                self.container.insert(i, linhas[i])
        self.window = sg.Window("UFLIX", self.container, font=("Helvetica", 14))

    def ler_evento(self, event, values):
        if event == "Salvar":
            self.window.close()
            nome = values["nome"]
            cpf = values["cpf"]
            nascimento = str(values["dia"])+"/"+str(values["mes"])+"/"+str(values["ano"])
            admin = values["admin"]
            if self.__registro_pessoas.atual.assinante:
                nome_cartao = values["nome_cartao"]
                num_cartao = values["num_cartao"]
                validade = values["mes_cartao"]+"/"+values["ano_cartao"]
                cvv = values["cvv"]
            else:
                nome_cartao = None
                num_cartao = None
                validade = None
                cvv = None
            self.__registro_pessoas.atualizar(nome, cpf, nascimento, admin, nome_cartao, num_cartao, validade, cvv)
            return "visualizar_pessoa"
        if event == "Cancelar":
            self.window.close()
            return "visualizar_pessoa"
        return "editar_pessoa"
