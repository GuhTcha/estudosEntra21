#e086.py
"""
86. A partir de uma lista composta apenas de dados numéricos, gere outra lista usando list comprehension usando como base a lista anterior,
compondo a nova com valores dos elementos originais elevados ao cubo: kkk é mais facil que imagina.
(lista1 = [1,2,3,4,5,6] ; lista2 = [i** 3 for i in lista1]), Explicarei em sala. 
"""

lista1=[1,2,3,4,5,6,7,8,9,10]
lista_q = [num ** 2 for num in lista1]

print (lista1)
print (lista_q)

'referência: https://www.youtube.com/watch?v=a3zqV2yTLD0'