'''
95. Escreva de forma reduzida um programa que recebe do usuário um nome e duas notas,
salvando tais dados como um elemento de uma lista.
Exiba em tela o conteudo desta lista. use: from operator import itemgetter
'''
import operator
a = []

a.append(input('Aluno:'))
a.append(input('Nota do 1ª semestre:'))
a.append(input('Nota do 2ª semestre:'))

a.sort(key=operator.itemgetter(a))
print (a)