'''
1. Localize na internet uma lista com todos os Municipios do Brasil, 5570 municipios com a Unidade da Federação
2. Consolide esses dados em um arquivo CSV/sheets.csv
3. Crie uma tabela CIDADES (ID/UF/CIDADE)
4. (PANDAS:)Importe todos os municipios para dentro desta tabela. 
5. Imprima todos municipios em uma select * from
6. Imprima um contador do sql count
7. Localize na Internet uma lista de todos os nomes de pessoas registrados em cartorio, 100787. 
8. Consolide esses dados em um arquivo CSV/sheets.csv
9. Crie uma tabela PESSOAS (ID,NOME,IDADE,CIDADE_ID)
10. (PANDAS:)Importe todos os municipios para dentro desta tabela utilizando os seguintes criterios:
    Nome = nome transportados do csv
    Idade = Range de 0 a 100 (Random)
    Cidade_id = Range de 1 a Total de municipios na tabela SQL
11. Imprima todos em uma select *
12. Imprima um contador do sql 

13. Imprima lista de 2000 pessoas, ordenada por estado,cidade,idade,nome (vinda do SQL).
'''
#Bibliotecas requeridas
import sqlite3 as db
import pandas as pd
import random as rd

cnx = db.connect("EXER200-2")
cur = cnx.cursor()

#Construção das tabelas(PESSOAS e MUNICIPIOS)
cur.execute('''
    DROP TABLE IF EXISTS MUNICIPIOS;
''')

cur.execute('''
    CREATE TABLE MUNICIPIOS(
        MUNICIPIO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        MUNICIPIO_NOME TEXT NOT NULL,
        MUNICIPIO_UF TEXT NOT NULL
    );
''')

cur.execute('''
    DROP TABLE IF EXISTS PESSOAS;
''')

cur.execute('''
    CREATE TABLE PESSOAS(
        PESSOA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PESSOA_NOME TEXT NOT NULL,
        PESSOA_IDADE INTEGER NOT NULL,
        PESSOA_CIDADE_ID INTEGER NOT NULL
    );
''')

#Inserção de dados na tabela de MUNICIPIOS
coluna_municipios = list(["ID","UF","Município"])
municipios_in = (r"C:\Users\Gustavo\Downloads\Municípios - Página1.csv")
pm = pd.read_csv(municipios_in, index_col=0, header=0, usecols=coluna_municipios)

numero_cidade = list((pm.shape))[0]

sql_mu=("INSERT INTO MUNICIPIOS('MUNICIPIO_NOME,MUNICIPIO_UF') VALUES(?, ?) ")
for index,row in pm.iterrows():
    val=(row.UF,row.Município)
    cur.execute(sql_mu,val)

cnx.commit()

#Inserção de dados na tabela PESSOAS
coluna_pessoas= list(["ID","first_name"])
pessoas_in = (r"C:\Users\Gustavo\Downloads\nomes.csv~\nomes.csv")
pp = pd.read_csv(pessoas_in, index_col=0, header=0, usecol=coluna_pessoas)

numero_pessoas=list((pp.shape))[0]

sql_pe=("INSERT INTO PESSOAS('PESSOA_NOME,PESSOA_IDADE,PESSOA_CIDADE_ID') VALUES(?, ?, ?) ")
for index,row in pp.iterrows():
    nome = row.first_name
    idade = rd.randrange(1,100)
    cidade_id = rd.randrange(1,numero_cidade)
    valp=(nome,idade,cidade_id)
    cur.execute(sql_pe,valp)

cnx.commit()
cur.close