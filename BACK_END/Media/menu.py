def Ler_int(msg):
    while True:
        try:
            m = int(input(msg))
        except (ValueError, TypeError):
            print('\n\033[31mERRO: Valor inválido\nDigite um valor válido\033[m\n')
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return m


def Ler_str(msg):
    while True:
        try:
            m = str(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um valor válido\033[m')
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return m


def Ler_float(msg):
    while True:
        try:
            m = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um valor válido\033[m')
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return m


def Linha(tam=42):
    return '-' * tam


def Cabeçalho(txt):
    print(Linha())
    print(txt.center(42))
    print(Linha())


def Menu(lista, txt):
    Cabeçalho(txt)
    item = 1
    for i in lista:
        print(f'[\033[92m{item}\033[m] - \033[36m{i}\033[m')
        item += 1
    print(Linha())

    opcao = Ler_int('Escolha uma opção: ')
    return opcao


def Sair():
    from time import sleep
    Cabeçalho('Saindo do sistema...')
    sleep(1.5)
    Cabeçalho('Você foi desconectado.')
    exit()


def Erro():
    print('\n\033[31mERRO: Valor inválido\033[m')
    print('\033[31mDigite um valor válido\033[m\n')


def Menu_Aritmetica(lista, txt):
    Cabeçalho(txt)
    item = 1
    for i in lista:
        print(f'[\033[92m{item}\033[m] - \033[36m{i}\033[m')
        item += 1
    print(Linha())

    opcao = Ler_int('Escolha uma opção: ')
    if opcao == 1:
        from calculos import Media_Aritmetica
        Media_Aritmetica()
    elif opcao == 2:
        from main import Inicio, itens_menu_inicial
        Inicio(itens_menu_inicial)
    elif opcao == 3:
        from sistema import Ler_Arquivo
        Ler_Arquivo('NOTAS_ALUNOS')
    elif opcao == 4:
        Sair()
    else:
        Erro()


def Menu_Ponderada(lista, txt):
    Cabeçalho(txt)
    item = 1
    for i in lista:
        print(f'[\033[92m{item}\033[m] - \033[36m{i}\033[m')
        item += 1
    print(Linha())

    opcao = Ler_int('Escolha uma opção: ')
    if opcao == 1:
        from calculos import Media_Ponderada
        Media_Ponderada()
    elif opcao == 2:
        from main import Inicio, itens_menu_inicial
        Inicio(itens_menu_inicial)
    elif opcao == 3:
        from sistema import Ler_Arquivo
        Ler_Arquivo('NOTAS_ALUNOS')
    elif opcao == 4:
        Sair()
    else:
        Erro()