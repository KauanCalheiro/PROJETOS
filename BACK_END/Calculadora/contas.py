from menu import Cabecalho, Ler_float


def Soma():
    Cabecalho('Soma'.upper())

    n1 = Ler_float('1º número: ')
    n2 = Ler_float('2º número: ')

    print(f'\n {n1} + {n2} = {n1 + n2}')
    print(f'\n O resultado da soma é {n1 + n2}')


def Subtracao():
    Cabecalho('Subtração'.upper())

    n1 = Ler_float('1º número: ')
    n2 = Ler_float('2º número: ')

    print(f'\n {n1} - {n2} = {n1 - n2}')
    print(f'\n O resultado da subtração é {n1 - n2}')


def Multiplicacao():
    Cabecalho('Multiplicação'.upper())

    n1 = Ler_float('1º número: ')
    n2 = Ler_float('2º número: ')

    print(f'\n {n1} x {n2} = {round(n1 * n2, 2)}')
    print(f'\n O resultado da multiplicação é {round(n1 * n2, 2)}')


def Divisao():
    Cabecalho('Divisão'.upper())

    n1 = Ler_float('1º número: ')
    n2 = Ler_float('2º número: ')

    print(f'\n {n1} ÷ {n2} = {round(n1 / n2, 2)}')
    print(f'\n O resultado da divisão é {round(n1 / n2, 2)}')


def Resto():
    Cabecalho('Resto'.upper())

    n1 = Ler_float('1º número: ')
    n2 = Ler_float('2º número: ')

    print(f'\n {n1} % {n2} = {round(n1 % n2, 2)}')
    print(f'\n O resultado do resto é {round(n1 % n2, 2)}')
