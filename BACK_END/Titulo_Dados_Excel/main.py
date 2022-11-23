import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

book = openpyxl.Workbook()
encoding = 'utf-8'
arquivo_excel = 'Excel.xlsx'

excel = pd.read_excel(arquivo_excel, sheet_name="Planilha2")

nomes = str(excel.columns[0])
nomes = excel[nomes]
titulo = list(excel.columns)
numerodelinhas = max(list(excel.index))+1

for i in range(numerodelinhas):
    book = openpyxl.Workbook()
    nome = str(nomes[i])
    texto = list(excel.loc[i , :])
    sheet_page = book['Sheet']
    sheet_page.append(titulo)
    sheet_page.append(texto)
    book.save(f'Arquivos\\{nome}.xlsx')
    i += 1
    
print ('\n\n\033[32mArquivos gerados com sucesso!!\033[m\n\n')
