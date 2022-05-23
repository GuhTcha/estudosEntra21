#e0147.py
aluno = ("Gustavo")
p1 = 100.0
p2 = 100.0
p3 = 0.0
soma1 = p1+p2+p3
media1 = round(soma1/3,1)
 

print(aluno)
if media1 < 60.0:
    print(f'Sua nota no 1ª trimestre foi: {media1}\n você não alacançou a nota necessária para passar, se esforce mais!')
else:
    print(f'Essa foi sua nota no 1ª trimestre: {media1}\n Parabéns você alcançou a média do trimestre!!')

p4 = 100.0
p5 = 100.0
p6 = 50.0
soma2 = p4+p5+p6
media2 = round(soma2/3,1)

if media2 < 60.0:
    print(f'\nSua nota no 2ª trimestre foi: {media2}\n você não alacançou a nota necessária para passar\n')
else:
    print(f'\nEssa foi sua nota no 2ª trimestre: {media2}\n Parabéns você alcançou a média do trimestre!!\n')

p7 = 100.0
p8 = 100.0
p9 = 100.0
soma3 = p7+p8+p9
media3 = round(soma3/3,1)

if media3 < 60.0:
    print(f'Sua nota no 3ª trimestre foi: {media3}\n você não alacançou a nota necessária para passar\n')
else:
    print(f'Essa foi sua nota no 3ª trimestre: {media3}\n Parabéns você alcançou a média do trimestre!!\n')

soano= (soma1+soma2+soma3)
meano=round(soano/9,1)

if meano > 60:
    print(f'Sua nota média do ano foi: {meano}\n Parabéns, você passou de ano!!')
else:
    print(f'Sua nota média do ano foi: {meano}\n Você rodou de ano, te espero ano que vem')
