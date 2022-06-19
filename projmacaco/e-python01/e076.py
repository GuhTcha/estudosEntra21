'''
76. Crie um programa que gera um dicionario a partir de um valor digitado pelo usuário,
de modo que serão exibidos todos os valores antecessores a este número multiplicados por eles mesmos.
Supondo que o usuário tenha digitado 4, a saida deve ser { 1:1, 2:4, 3:9, 4:16}:
'''

num = int(input('num? '))
dd = dict()
for i in range(1,num+1):
    dd[i] = i*i
print(dd)

'referência: https://github.com/Machado-tec/e2122-dados-geral/tree/main/projeto/exercicios_065-099'