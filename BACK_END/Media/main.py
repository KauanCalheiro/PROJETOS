from menu import *
from calculos import *
from sistema import *


itens_menu_inicial = ['MÉDIA ARITMÉTICA','MÉDIA PONDERADA', 'NOTAS DOS ALUNOS', 'SAIR']


def Inicio(itens):
    while True:
        Arquivo_Existe('NOTAS_ALUNOS')
        opc = Menu(itens, 'MENU INICIAL')

        if opc == 1:
            Media_Aritmetica()
        elif opc == 2:
            Media_Ponderada()
        elif opc == 3:
            Ler_Arquivo('NOTAS_ALUNOS')
        elif opc == 4:
            Sair()
        else:
            Erro()

Inicio(itens_menu_inicial)