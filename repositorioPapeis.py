import yfinance as yf
from papel import *


class Repositorio:
    def __init__(self):
        self.lista_papeis = []

    def download_b3(self, periodo, codigos):
        dados_b3 = yf.download(codigos, period=periodo, auto_adjust=True)
        print(len(codigos))
        if len(codigos) >= 2:
            for codigo in codigos:
                papel = Papel(codigo, dados_b3['Close'][codigo])
                self.lista_papeis.append(papel)
        else:
            self.lista_papeis.append(Papel(codigos[0], dados_b3['Close']))

    def varifica_papel(self, codigo):
        for index in range(len(self.lista_papeis)):
            codigo_papel = self.lista_papeis[index].codigo
            if codigo_papel == codigo:
                return True, index
        else:
            return False, None
