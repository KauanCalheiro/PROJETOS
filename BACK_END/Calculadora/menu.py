def Ler_int(txt):
    while True:
        try:
            m = int(input(txt))
        except (ValueError, TypeError):
            Erro()
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return m


def Ler_float(txt):
    while True:
        try:
            m = float(input(txt))
        except (ValueError, TypeError):
            Erro()
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return m


def Erro():
    print('ERRO: Valor inválido\nDigite um valor válido\n')


def Linha(tam=42):
    return '-' * tam


def Cabecalho(txt):
    print(Linha())
    print(txt.center(42))
    print(Linha())


def Menu(lista, txt):
    Cabecalho(txt)
    item = 1
    for i in lista:
        print(f'[{item}] - {i}')
        item += 1
    print(Linha())

    user_input = Ler_int('Escolha uma opção: ')
    return user_input


def Sair():
    from time import sleep
    Cabecalho('Desconectando...')
    sleep(1.5)
    Cabecalho('Você foi deconectado.')
    exit()
