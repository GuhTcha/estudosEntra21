print("Esse é um programa que diz qual palavra é maior, também mostra a quantidade de letras")
a=str(input('por tanto,me diga uma frase: '))
b=str(input('outra frase para a comparação: '))

if len(a) > len(b):
    print(a,len(a))
if len(b) > len(a):
    print (b,len(b))
if len(a) == len(b):
    print(a,len(a),b,len(b))