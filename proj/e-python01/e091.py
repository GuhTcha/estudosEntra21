'''
Escreva um programa da forma mais reduzida possível, que recebe do usuario uma série de nomes,
separando os mesmos e os organizando em ordem alfabetica. Em Seguida exiba em tela os nomes já ordenados.
'''
no = [x for x in input('Diga os nomes dos convidados, por favor.\n').split(',')]
no.sort()
print(no)