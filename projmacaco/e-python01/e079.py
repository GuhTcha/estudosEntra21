from num2words import num2words



numero = int( input('Digite um número: ') )


numextenso = num2words(numero, lang='pt-br')

print(f'Número: {numextenso}')