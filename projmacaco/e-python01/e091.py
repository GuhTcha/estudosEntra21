'''
Crie um programa que recebe do usuário uma sequencia de números aleatórios separados por vírgula, armazene os números um a um,
em formato de texto, como elementos ordenados de uma lista. Mostre em tela a lista com seus respectivos elementos após serem ordenados. 
'''
no = [x for x in input('Diga os nomes dos convidados, por favor.\n').split(',')]
no.sort()
print(no)
'referencia: https://github.com/Machado-tec/e2122-dados-geral.git'