alunos = {
    'adriano' : 'reprovado',
    'Silvio' : 'aprovado',
    'Jocimar' : 'aprovado'
}

for n, s in alunos.copy().items():
    print(n)

for n, s in alunos.copy().items():
    print(n,s)
    if s == 'aprovado':
        print("parabéns!!!", n)

#for nome in alunos.items():
   # print(nome)

print(alunos.items())