#--------------------SCRIPT--------------------#
def script (sal_min, qntd_hrs_trab, qntd_hrs_ext_trab, qntd_pess_dpndt ):
    #-----SALARIO_BRUTO-----#
    val_hrs_trab = sal_min * 1/20
    sal_mes = qntd_hrs_trab * val_hrs_trab
    val_hrs_ext = qntd_hrs_ext_trab*(sal_min/20)*(45/100)
    val_dpndt = 45*qntd_pess_dpndt
    salario_bruto = sal_mes + val_dpndt + val_hrs_ext
    print(f'O salário bruto é de: R$ {salario_bruto}')
    print('-'*50)
    #-----SALARIO_LIQUIDO/IMPOSTO DE RENDA-----#
    if salario_bruto < 1000:
        print('Isento de imposto')
    elif salario_bruto >= 1000 and salario_bruto <= 3000:
        print('15% de imposto')
        salario_liquido = salario_bruto - (salario_bruto * (15/100))
    elif salario_bruto > 3000:
        print('25% de imposto')
        salario_liquido = salario_bruto - (salario_bruto * (25/100))
    print(f'Salário líquido é de: R$ {salario_liquido}')
    print('-'*50)
    #-----SALARIO_FINAL/GRATIFICAÇÃO-----#
    if salario_liquido <= 2500:
        salario_final = salario_liquido + 150
        print('Você recebeu uma gratificação de R$ 150,00')
    else:
        salario_final = salario_liquido + 55
        print('Você recebeu uma gratificação de R$ 55,00')
    print('-'*50)
    print(f'Salário final é de: R$ {salario_final}')
    print('='*50)
    
#--------------------ENTRADA_DE_DADOS--------------------#
print('='*50)
salario_minimo = float(input('Valor do Salário Mínimo: R$ '))
print('-'*50)
quantidade_horas_trabalhadas = float(input('Quantidade de horas trabalhadas: '))
print('-'*50)
quantidade_horas_extras_trabalhadas = float(input('Quantidade de horas extras trabalhadas: '))
print('-'*50)
quantidade_pessoas_depententes = float(input('Quantidade de pessoas dependentes: '))
print('='*50)
script(salario_minimo, quantidade_horas_trabalhadas, quantidade_horas_extras_trabalhadas, quantidade_pessoas_depententes)
    