BEGIN TRANSACTION;

DROP TABLE IF EXISTS CIDADES;

CREATE TABLE CIDADES(
    ID INT PRIMARY KEY AUTOINCREMENT
    NOME TEXT NOT NULL
    ESTADO TEXT NOT NULL
    POPULAÇÃO INT NULL
);


INSERT INTO CIDADES(NOME,ESTADO,POPULAÇÃO)
    VALUES
    ('São Paulo','São Paulo',12.325.232), 
    ('Rio de Janeiro','Rio de Janeiro',6.747.815), 
    ('Brasília','Distrito Federal'3.055.149), 
    ('Salvador','Bahia',2.886.698),
    ('Fortaleza','Ceará',2.686.612),
    ('Belo Horizonte','Minas Gerais',2.521.564),
    ('Manaus','Amazonas',2.219.580), 
    ('Curitiba','Paraná',1.948.626),
    ('Recife','Pernambuco',1.653.461),
    ('Goiânia','Goiás',1.536.097),
    ('Belém','Pará',1.499.641),
    ('Porto Alegre','Rio Grande do Sul',1.488.252),
    ('São Luís','Maranhão',1.108.975),
    ('Maceió', 'Alagoas', 1.025.360);

COMMIT;