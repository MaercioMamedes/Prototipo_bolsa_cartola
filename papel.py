import pandas as pd
from decimal import *
from datetime import *


class Papel:
    def __init__(self, codigo, dados_b3):
        self._codigo = codigo
        self._valor = round(dados_b3[-1],2)
        self._historico = {"data": [], "preço": [], "rentabilidade": []}
        self.historico(dados_b3)
        self.rentabilidade = round(self.rentabilidade_periodo(),2)

    def __str__(self):
        def formatar_historico(historico):
            def formatar_data(data):
                return "{}".format(data.strftime("%d/%m/%Y"))

            def formatar_rentabilidade(rentabilidade):
                return "{:.2f}%".format(rentabilidade)

            def formatar_valor(valor):
                return "R${:.2f}".format(valor)

            historico_formatado = {}
            historico_formatado["data"] = list(map(formatar_data,historico["data"]))
            historico_formatado["preço"] = list(map(formatar_valor, historico["preço"]))
            historico_formatado["rentabilidade"] = list(map(formatar_rentabilidade,historico["rentabilidade"]))
            return historico_formatado

        tabela = pd.DataFrame(formatar_historico(self._historico))
        return f"\nO papel {self._codigo} rendeu {self.rentabilidade}% no período \n\n {tabela.set_index('data')}"

    def __eq__(self, codigo):
        print(codigo)
        return self._codigo == codigo

    @property
    def codigo(self):
        return self._codigo

    @property
    def valor(self):
        return f"{self._valor}"

    def historico(self, dados_b3):
        tamanho_periodo = len(dados_b3)
        for index in range(tamanho_periodo):
            self._historico["data"].append(dados_b3.index[index].to_pydatetime())
            self._historico["preço"].append(round(dados_b3[index],2))
            self._historico["rentabilidade"].append(round(self.rentabilidade_periodo(periodo ="intervalo"),2))


    def rentabilidade_periodo(self, periodo = "full"):
        indice = 0
        if periodo == "intervalo":
            indice = -2

        if len(self._historico["preço"]) >1:
            valor_inicio = Decimal(str(self._historico["preço"][indice]))
            valor_final = Decimal(str(self._historico["preço"][-1]))
            rentabilidade = (valor_final - valor_inicio)/valor_inicio*100
            return  rentabilidade

        else:
            return 0
