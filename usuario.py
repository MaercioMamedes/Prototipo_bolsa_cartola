
class Usuario:
    def __init__(self, nome, email, telefone):
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._carteira = []
        self._criou_carteira = False

    @property
    def nome(self):
        return self._nome

    def verifica_carteira(self):
        self._criou_carteira = False if len(self._carteira) == 0 else True


