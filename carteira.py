import pandas as pd
from papel import *


class Carteira:
    def __init__(self):
        self.capital = 0
        self.ativos = []
        self.historico = {"data": [], "Patrimônio": [], "rentabilidade": []}
        self._rentabilidade_periodo = 0

    def __getitem__(self, item):
        return self.ativos[item]

    def __len__(self):
        return len(self.ativos)

    def adiciona_papel(self, papel):
        self.ativos.append(papel)

    def get_rentabilidade(self):
        valor_inicio = self.historico["Patrimônio"][0]
        valor_final = self.historico["Patrimônio"][-1]
        rentabilidade = (valor_final - valor_inicio)/valor_inicio*100
        return rentabilidade

    @property
    def rentabilidade_periodo(self):
        self._rentabilidade_periodo = self.get_rentabilidade()

        return "{:.2f}%".format(self._rentabilidade_periodo)

    def update_capital(self):
        tamanho_lista = len(self.ativos)
        self.capital = sum([self.ativos[n].posicao for n in range(tamanho_lista)])

    def update_carteira(self, valor, data):
        capital_anterior = self.capital
        self.update_capital()
        data_formatada = data.strftime('%d/%m/%Y')
        rentabilidade = (self.capital - capital_anterior) / capital_anterior * 100

        if data_formatada not in self.historico["data"]:
            self.historico["data"].append(data_formatada)
            self.historico["Patrimônio"].append(self.capital)
            self.historico["rentabilidade"].append(rentabilidade)

        else:
            indice = self.historico["data"].index(data_formatada)
            self.historico["Patrimônio"][indice] += valor
            self.historico["rentabilidade"][indice] = rentabilidade

    def get_historico_formatado(self):
        def formatar_capital(valor):
            return "R${:.2f}".format(valor)

        def formatar_rentabilidade(rentabilidade):
            return "{:.2f}%".format(rentabilidade)

        historico = {
            "data": self.historico["data"],
            "Patrimônio": list(map(formatar_capital, self.historico["Patrimônio"])),
            "Rentabilidade": list(map(formatar_rentabilidade, self.historico["rentabilidade"]))
        }
        return historico
