from menu import *
from time import sleep


def Arquivo_Existe(titulo):
    try:
        a = open(titulo, 'rt')
        a.close
    except (FileNotFoundError, FileExistsError):
        print('\n\033[31mERRO: Arquivo não existe.\033[m\n')
        return Criar_Arquivo(titulo)
    else:
        return True


def Criar_Arquivo(titulo):
    m = Criar_Arquivo_()
    while (m<=0 and m>2):
        print('\n\033[31mERRO: Valor inválido\033[m')
        print('\033[31mDigite um valor válido\033[m\n')
        Criar_Arquivo(titulo)
        break
    else:
        if m == 1:
            try:
                a = open(titulo, 'wt+')
                a.close()
            except:
                print(f'\n\033[31mERRO: Não foi possível criar o arquivo {titulo}\033[m\n')
            else:
                print('\n\033[32mArquivo gerado com suscesso!\033[m')
                from main import itens_menu_inicial, Inicio
                Arquivo_Existe(titulo)
                Inicio(itens_menu_inicial)
        elif m == 2:
            n = Sair_Sistema()
            if n == 1:
                Cabeçalho('Saindo do sistema...')
                sleep(1.5)
                Cabeçalho('Você foi desconectado.')
                exit()
            elif n == 2:
                from main import itens_menu_inicial, Inicio
                Inicio(itens_menu_inicial)
            else:
                print('\n\033[31mERRO2: Valor inválido\033[m')
                print('\033[31mDigite um valor válido\033[m\n')
                Sair_Sistema()

def Criar_Arquivo_():
    m = Ler_int('[1] - Sim\n[2] - Não\nDeseja criar o arquivo? ')
    if m == 1:
        return m 
    if m == 2:
        print('')
        return m

def Sair_Sistema():
    m = Ler_int('[1] - Sim\n[2] - Não\nDeseja sair? ')
    return m


def Ler_Arquivo(titulo):
    try:
        Arquivo_Existe(titulo)
        a = open(titulo, 'rt')
    except (FileNotFoundError, FileExistsError):
        Criar_Arquivo(titulo)
    else:
        Cabeçalho('NOTAS DOS ALUNOS')
        for i in a:
            dado = i.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} Nota:{dado[1]:>1}')
        a.close()


def Escrever_Aquivo(titulo, nome, nota):
    try:
        a = open(titulo, 'at')
        a.write(f'{nome};{nota}\n')
        print(f'\033[32mNova nota cadastrada com sucesso!\033[m')
    except:
        print(f'\033[31mERRO: Não foi possível cadastrar nota do aluno(a) {nome}\033[m')
    finally:
        a.close()