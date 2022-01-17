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
                self.lista_papeis.append(Papel(codigo, dados_b3['Close'][codigo]))
        else:
            self.lista_papeis.append(Papel(codigos[0], dados_b3['Close']))

    def varifica_papel(self, codigo):
        for papel in self.lista_papeis:
            if papel.codigo == codigo:
                return True
        else:
            return False
