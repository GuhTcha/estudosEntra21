# Conexão Python com SQLite

## Criar o banco de dados(database)
import sqlite3

### Conectar ao sqlite
    conexão = sqlite.connect('modulo06.sqlite3')

## Conectar a Database
'Invoca métodos que executam instruções SQLite'
    cur = cnx.cursor()

## Criar tabela
cur.execute("""
    CREATE TABLE...();
""")

## Inserir dados
cur.execute("""
    INSERT INTO... ():
""")
## Selecionar dados inseridos
'''
Utilizado para mostrar os resultados
cur.fetchone() --> só o primeiro resultado
cur.fetchmany(2) --> os primeiros 2
cur.fetchall() --> todos resultados
'''

## Uso dos resultados de uma query
cur.execute('SELECT * FROM PESSOAS;')
todos = cur.fetchall()
'Quatro atributos, quatro variáveis(w,x,y,z)'
for w,x,y,z in todos:
    print(f'{w},{x},{y},{z}')

## Update e delete




sep=';', encoding='ISO-8859-1')
