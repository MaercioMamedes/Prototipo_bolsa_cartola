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

    def adiciona_papel(self, codigo):
        if self._carteira.verifica_papel(codigo):
            pass




