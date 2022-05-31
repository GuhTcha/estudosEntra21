from pfiles import importa_planilha

exemplo = 1


if (exemplo == 1):
    colunas = list('id','Nome','Telefone')

    dd = importa_planilha(colunas)

    colunas.remove['id']

    for i in dd.items():
        print(f' items: {i}')
    
    for i in dd.values():
        print[
            i('Nomes')
            i('Telefones')
        ]
