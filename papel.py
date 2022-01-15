
class Papel:
    def __init__(self, codigo, valor, data_inicio):
        self.codigo = codigo
        self.valor = valor
        self.qtd = 1
        self.data = data_inicio
        self.posicao = self.update_papel()
        self.historico = {"data": [], "preço": [], "rentabilidade": []}
        self._rentabilidade_periodo = 0

    @property
    def rentabilidade_periodo(self):
        valor_inicio = self.historico["preço"][0]
        valor_final = self.historico["preço"][-1]
        rentabilidade = (valor_final - valor_inicio)/valor_inicio*100
        self._rentabilidade_periodo = rentabilidade
        return "{:.2f}%".format(self._rentabilidade_periodo)

    def set_rentabilidade(self, data, valor):
        preco = valor
        valor_rentabilidade = (valor - self.valor) / self.valor * 100
        data_formatada = data.strftime('%d/%m/%Y')
        self.historico["data"].append(data_formatada)
        self.historico["preço"].append(preco)
        self.historico["rentabilidade"].append(valor_rentabilidade)

    def compra_papel(self, qtd):
        self.qtd += qtd
        self.posicao = self.update_papel()

    def update_papel(self):
        return self.valor * self.qtd

    def update_valor(self, valor, data):
        self.set_rentabilidade(data, valor)
        self.valor = valor
        self.posicao = self.update_papel()

    def get_historico_formatado(self):
        def formatar_capital(valor):
            return "R${:.2f}".format(valor)

        def formatar_rentabilidade(rentabilidade):
            return "{:.2f}%".format(rentabilidade)
        historico = {
            "data":self.historico["data"],
            "Patrimônio":list(map(formatar_capital, self.historico["preço"])),
            "Rentabilidade":list(map(formatar_rentabilidade, self.historico["rentabilidade"]))
        }
        return historico
