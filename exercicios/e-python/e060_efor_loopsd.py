'''
r = [[1, 2, 3], ['a', 'b', 'c'], ['~', '?', '!']]

for x inr:
    #print(x)
    for y in x:
        pass 
    "pass" termina a função
        print(y, end='')

print()
'''
'''
r = ([10,20,30], [15,1,2], [50.3,5])
volume_total = 0

for a, b, c in r:
    print(a,b,c)
    print(a,b,c, 'volume é:', (a*b*c))
    volume_total += (a*b*c)
'''
## Aqui vamos multiplicar os items [0],[1],[2] de cada item da lista
p0=1
p1=1
p2=1
lista = [[10, 20, 30], [15,1,2], [50,3,5], [45,12,7], [100,200,300]]
for x in lista:
    print(x)
    p0 *= x[0]
    p1 *= x[1]
    p2 *= x[2]

print(p0,p1,p2)