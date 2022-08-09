from num2words import num2words

num = int(input('Digite um numero de 0 a 100: '))

if num < 100 or num > 0 :
    num_extenso = num2words(num,lang='pt-br')
    print(f'Numero digitado: {num_extenso}')
else:
    print ('Refaça, por favor')