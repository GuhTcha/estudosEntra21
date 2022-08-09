numero = int(input('Digite o número: '))
divisões = 0

for i in range(1,numero + 1):
    if numero % i ==0:
        divisões += 1
        print(f'i: {i}, numero: {numero%i}')

if divisões == 2:
    print(f'{numero} é primo')
    print(f'{numero} é divisível por um ou {numero}')
else:
    print(f'{numero} primo não ser')
    print(f'{numero} divisível é {divisões} vezes')