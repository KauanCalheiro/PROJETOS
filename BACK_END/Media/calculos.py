from menu import *
from sistema import *


def Media_Aritmetica():
    n = []
    a = []
    r = 0

    Cabeçalho('MÉDIA ARITMÉTICA')
    a.append(Ler_str('Nome do Aluno(a): '))
    num_notas = (Ler_int('\nQuantidade de notas: '))

    for i in range(num_notas):
        n.append(Ler_float(f'Nota {i+1}ª: '))

    nota_final = round(sum(n)/len(n), 2)
    aluno = a[r]
    print(f'\nAluno(a): {aluno}\nNota: {round(nota_final, 2)}')

    Escrever_Aquivo('NOTAS_ALUNOS', aluno, nota_final)

    itens_menu_media_aritmedica = [
        'NOVA NOTA', 'MENU INICIAL', 'NOTAS', 'SAIR']
    Menu_Aritmetica(itens_menu_media_aritmedica, 'MÉDIA ARITMÉTICA')


def Media_Ponderada():
    n = []
    p = []
    a = []
    r = 0

    Cabeçalho('MÉDIA PONDERADA')
    a.append(Ler_str('Nome do Aluno(a): '))
    num_notas = (Ler_int('\nQuantidade de notas: '))
    nota_final = 0

    for i in range(num_notas):
        n.append(Ler_float(f'Nota {i+1}ª: '))
        p.append(Ler_float(f'Peso {i+1}ª: '))
        nota_final += n[i]*p[i]

    nota_final = round(nota_final/sum(p), 2)
    aluno = a[r]
    print(f'\nAluno(a): {aluno}\nNota: {round(nota_final, 2)}')

    Escrever_Aquivo('NOTAS_ALUNOS', aluno, nota_final)

    itens_menu_media_ponderada = ['NOVA NOTA', 'MENU INICIAL', 'NOTAS', 'SAIR']
    Menu_Ponderada(itens_menu_media_ponderada, 'MÉDIA PONDERADA')
