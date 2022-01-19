import os
from usuario import *


class Menu:
    repositorio = Repositorio()

    def __init__(self):
        self._lista_usuarios = []

    def criar_usuario(self):
        nome = input("Digite o nome do usuario: ")
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu email:  ")
        self._lista_usuarios.append(Usuario(nome, telefone, email))
        self.flag()
        self.main()

    def mostrar_usuarios(self):
        if len(self._lista_usuarios) != 0:
            print("USUÁRIOS CADASTRADOS")
            for index, usuario in enumerate(self._lista_usuarios):
                print(f"{index + 1} - {usuario.nome}")
        else:
            print("NENHUM USUÁRIO CADASTRADO")

        escolha = int(input("Selecione o usuário: "))
        self.flag()
        self.main()

    @staticmethod
    def flag():
        confirm = input("Pressione qualquer tecla para continuar: ")
        os.system("clear")

    def main(self):
        print("Jogo da bolsa")
        print("ESCOLHA UMA DAS OPÇÕES")
        escolha = int(input("1 - MOSTRAR USUÁRIOS 2 - CRIAR USUÁRIO 3 - MOSTRAR CLASSIFICAÇÃO:  "))
        if escolha == 1:
            self.mostrar_usuarios()
        elif escolha == 2:
            self.criar_usuario()
        else:
            print("opção inválida")


if __name__ == "__main__":
    menu = Menu()
    menu.main()
