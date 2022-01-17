from repositorioPapeis import *
from usuario import *
from collections import *


class menu:
    def __init__(self):
        self._repositorio = Repositorio()
        self._lista_usuarios = []

    def criar_usuario(self):
        nome = input("Digite o nome do usuario: ")
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu email:  ")
        self._lista_usuarios.append(Usuario(nome, telefone, email))

    def mostrar_usuarios(self):
        if len(self._lista_usuarios) !=0:
            print("USUÁRIOS CADASTRADOS")
            for index, usuario in enumerate(self._lista_usuarios):
                print(f"{index+1} - {usuario.nome}")


    def main(self):
        print("Jogo da bolsa")
        print("ESCOLHA UMA DAS OPÇÕES")
        menu = defaultdict({})
        escolha = int(input("1 - MOSTRAR USUÁRIOS 2 - CRIAR USUÁRIO 3 - MOSTRAR CLASSIFICAÇÃO:  "))



if __name__ == "__main__":
    main()