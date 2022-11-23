def Ler_int(txt):
    while True:
        try:
            m = int(input(txt))
        except (ValueError, TypeError):
            Erro()
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return m


def Erro():
    print('\n\033[31mERRO: Valor inválido\nDigite um valor válido\033[m\n')


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
        print(f'[\033[92m{item}\033[m] - \033[36m{i}\033[m')
        item += 1
    print(Linha())

    user_input = Ler_int('Escolha uma opção: ')
    return user_input


def Sair():
    from time import sleep
    Cabecalho('Fechando o Jogo...')
    sleep(1.5)
    Cabecalho('Você foi desconectado.')
    exit()
