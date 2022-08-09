import sqlite3

cnx = sqlite3.connect("Modulo06.sql")
cur = cnx.cursor()


cur.execute("""
    DROP TABLE IF EXISTS CIDADES;
""")

cur.execute ("""
    CREATE TABLE CIDADES(
        CIDADE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CIDADE_NOME TEXT NOT NULL
    );
""")

cur.execute('''
    DROP TABLE IF EXISTS PESSOAS;
''')

cur.execute('''
    CREATE TABLE PESSOAS (
        PESSOA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PESSOA_NOME TEXT NOT NULL,
        PESSOA_IDADE INTEGER,
        PESSOA_CIDADE_ID INTEGER NOT NULL
    );
''')


cur.execute("""
    INSERT INTO PESSOAS (PESSOA_NOME, PESSOA_IDADE, PESSOA_CIDADE_ID) VALUES
    ('Gustavo',18,6),
    ('Jaqueline',28,2),
    ('Roberta',32,7),
    ('Bianca',14,3),
    ('Fátima',42,5),
    ('Benjamin',63,4);
""")


cur.execute("""
    INSERT INTO CIDADES (CIDADE_NOME) VALUES
    ('Guabiruba'),
    ('Joinville'),
    ('Jaraguá'),
    ('Brusque'),
    ('Florianópolis'),
    ('Gaspar'),
    ('Timbó');
""")

cnx.commit()

cur.execute('''SELECT*
 FROM CIDADES;''')
resultado1=cur.fetchone()
print(resultado1)

cur.execute('''SELECT*
 FROM CIDADES;''')
resultado2=cur.fetchmany(2)
print(resultado2)

cur.execute('''SELECT PESSOA_NOME,PESSOA_CIDADE_ID 
FROM CIDADES, PESSOAS
WHERE PESSOA_CIDADE_ID = CIDADE_ID;''')
resultado3=cur.fetchall()
print(resultado3)