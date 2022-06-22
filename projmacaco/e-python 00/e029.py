import time
inicio = int(input("digite valor para o inicio: "))
fim = int(input('digite o valor do fim: '))

for i in range(inicio,fim+1):
    print(i)
    time.sleep(0.1)