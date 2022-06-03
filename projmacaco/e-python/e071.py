calculo = input('Qual o tipo de calculo básico?')

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

if calculo == '+':
    print('{} + {} = '.format(n1, n2))
    print(n1 + n2)

elif calculo == '-':
    print('{} - {} = '.format(n1, n2))
    print(n1 - n2)

elif calculo == '*':
    print('{} * {} = '.format(n1, n2))
    print(n1 * n2)

elif calculo == '/':
    print('{} / {} = '.format(n1, n2))
    print(n1 / n2)

else:
    print('Refaça os calculos.')