from pfiles import importa_planilha

colunas = list('id', 'Nome', 'Telefone')
dd = importa_planilha(colunas)
print(dd)


