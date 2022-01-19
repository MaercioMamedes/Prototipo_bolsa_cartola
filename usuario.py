from carteira import *
from repositorioPapeis import *


class Usuario:
    def __init__(self, nome, email, telefone):
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._carteira = None
        self._criou_carteira = False

    @property
    def nome(self):
        return self._nome

    def cria_carteira(self):
        if self._criou_carteira:
            return "Você já criou uma carteira"
        else:
            self._carteira = Carteira()
            self.verifica_carteira()

    def deleta_carteira(self):
        self._carteira = None
        self.verifica_carteira()

    def verifica_carteira(self):
        self._criou_carteira = True if not self._carteira else False

    def compra_papel(self, repositorio, codigo):
        verificador = repositorio.varifica_papel(codigo)[0]
        index_papel = repositorio.varifica_papel(codigo)[1]
        if verificador:
            papel = repositorio.lista_papeis[index_papel]
            if papel not in self._carteira:
                self._carteira.adiciona_papel(papel)
            else:
                print("Você já possui esse ativo na carteira")
        else:
            repositorio.download_b3("1mo", [codigo])  # tratar erro de entrada
            papel = repositorio.lista_papeis[-1]
            self._carteira.adiciona_papel(papel)

