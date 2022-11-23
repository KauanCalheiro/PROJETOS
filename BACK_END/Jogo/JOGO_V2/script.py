from menu import Ler_int, Erro, Cabecalho, Menu, Sair


def Regras():
    Cabecalho('REGRAS')
    print('Regras')


def Sortear_sequencia():
    import random
    n1: int = random.randint(1, 4)
    n2: int = random.randint(1, 4)
    n3: int = random.randint(1, 4)
    n = [n1, n2, n3]
    # print(n)
    return n


def Receber_sequencia():
    print('')
    r1 = R1()

    r2 = R2(r1)

    r3 = R3(r1, r2)

    r = [r1, r2, r3]
    return r


def R1():
    r1 = Ler_int('1º número: ')

    while r1 == 0:
        sair = Menu(['SIM', 'NÃO'], 'DESEJA SAIR?')
        print(' ')

        if (sair == 1):
            print('\nObrigado por jogar ^-^\n')
            Sair()

        if (sair == 2):
            r1 = Ler_int('1º número: ')

    while (r1 > 4):
        Erro()
        r1 = Ler_int('1º número: ')
    return r1


def R2(r1):
    r2 = Ler_int('2º Número: ')

    while r2 == 0:
        sair = Menu(['SIM', 'NÃO'], 'DESEJA SAIR?')
        print(' ')

        if (sair == 1):
            print('\nObrigado por jogar ^-^\n')
            Sair()

        if (sair == 2):
            print(f'1º número: {r1}')
            r2 = Ler_int('2º número: ')

    while (r2 > 4):
        Erro()
        r2 = Ler_int('2º número: ')
    return r2


def R3(r1, r2):
    r3 = Ler_int('3º Número: ')

    while r3 == 0:
        sair = Menu(['SIM', 'NÃO'], 'DESEJA SAIR?')
        print(' ')

        if (sair == 1):
            print('\nObrigado por jogar ^-^\n')
            Sair()

        if (sair == 2):
            print(f'1º número: {r1}')
            print(f'2º número: {r2}')
            r3 = Ler_int('3º número: ')

    while (r3 > 4):
        Erro()
        r3 = Ler_int('3º número: ')
    return r3


def Conferir_(r, n):
    acertos = Numero_acertos(r, n)

    if (r == n):
        Acertou_sequencia(n)

    if (r != n):
        Errou_sequencia(acertos, r)


def Numero_acertos(r, n):
    acertos: int = 0

    if (r[0] == n[0]):
        acertos = acertos + 1

    if (r[1] == n[1]):
        acertos = acertos + 1

    if (r[2] == n[2]):
        acertos = acertos + 1

    return acertos


def Acertou_sequencia(n):
    print(f'\nParabéns a sequencia era: \033[32m[{n[0]}, {n[1]}, {n[2]}]\033[m \n')
    from main import Jogo
    Jogo()


def Errou_sequencia(acertos, r):
    print(f'[{r[0]}, {r[1]}, {r[2]}]       Você acertou {acertos}')
    #acertos = acertos * 0
    # return acertos
