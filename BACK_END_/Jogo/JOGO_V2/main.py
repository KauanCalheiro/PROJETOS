from script import Sortear_sequencia, Receber_sequencia, Conferir_, Regras
from menu import Menu, Sair, Erro

def Jogo():
    while True:
        user_input = Menu(['JOGAR', 'REGRAS', 'SAIR'], 'MENU')
        
        if (user_input == 1):
            n = Sortear_sequencia()
            r = Receber_sequencia()
            Conferir_(r, n)

            while (r != n):
                r = Receber_sequencia()
                Conferir_(r, n)

        elif (user_input == 2):
            Regras()

        elif (user_input == 3):
            Sair()

        else:
            Erro()

Jogo()
