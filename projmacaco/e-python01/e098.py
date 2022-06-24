def data(nota):
    if nota < 0 and nota > 1.0:
        print('digite um numero válido')
    elif nota < 0.59:
        print('Reprovado')
    elif nota > 0.6:
        print('aprovado')
try:
    nota=float(input('Qual foi sua nota? '))

except:
    print ('valor invalido')
print(data(nota))