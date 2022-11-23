from menu import Menu, Sair, Erro
from contas import Soma, Subtracao, Multiplicacao, Divisao, Resto


def Main():
    while True:
        user_input = Menu(['SOMA', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO',
                          'DIVISÃO', 'RESTO', 'SAIR'], 'MENU')

        if (user_input == 1):
            Soma()

        elif (user_input == 2):
            Subtracao()

        elif (user_input == 3):
            Multiplicacao()

        elif (user_input == 4):
            Divisao()

        elif (user_input == 5):
            Resto()

        elif (user_input == 6):
            Sair()

        else:
            Erro()


Main()
