contador = 0
soma = 0
for i in range(1,101):
    if i % 3 !=0:
        soma +=i
        contador +=1
print(f'foram encontrados {soma} números impares') 
print(f'tiveram {contador} números impares')