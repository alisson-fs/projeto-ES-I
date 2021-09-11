--> REMOCAO DAS TABELAS

DROP TABLE CATALOGO;
DROP TABLE REGISTRO_PESSOAS;
DROP TABLE ALUGUEIS;
DROP TABLE SUGESTOES;
DROP TABLE COMENTARIOS;

--> CRIACAO DAS TABELAS

CREATE TABLE CATALOGO
(TITULO VARCHAR(100),
 FILME_ID VARCHAR(20),
 DURACAO VARCHAR(20),
 GENERO VARCHAR(20),
 CLASSIFICACAO VARCHAR(20),
 N_AVALIACOES VARCHAR(20),
 SOMA_AVALIACOES VARCHAR(20),
 PRIMARY KEY (TITULO)
);

CREATE TABLE REGISTRO_PESSOAS
(NOME VARCHAR(100),
 CPF VARCHAR(20),
 NASCIMENTO VARCHAR(20),
 SENHA VARCHAR(20),
 VENCIMENTO_ASSINATURA VARCHAR(20),
 ADMINISTRADOR VARCHAR(20),
 ASSINANTE VARCHAR(20),
 PRIMARY KEY (CPF)
);

CREATE TABLE ALUGUEIS
(INICIO VARCHAR(20),
 FIM VARCHAR(20),
 TITULO VARCHAR(100),
 CPF VARCHAR(20),
 FOREIGN KEY (TITULO) REFERENCES CATALOGO(TITULO),
 FOREIGN KEY (CPF) REFERENCES REGISTRO_PESSOAS(CPF)
);

CREATE TABLE SUGESTOES
(SUGESTAO VARCHAR(100),
 PRIMARY KEY (SUGESTAO)
);

CREATE TABLE COMENTARIOS
(TITULO VARCHAR(100),
 COMENTARIO VARCHAR(100),
 FOREIGN KEY (TITULO) REFERENCES CATALOGO(TITULO)
);

--> Inserts genéricos

INSERT INTO CATALOGO (TITULO,FILME_ID,DURACAO,GENERO,CLASSIFICACAO,N_AVALIACOES,SOMA_AVALIACOES) VALUES ('Senhor dos aneis','1','180min','Aventura','14','0','0');
INSERT INTO CATALOGO (TITULO,FILME_ID,DURACAO,GENERO,CLASSIFICACAO,N_AVALIACOES,SOMA_AVALIACOES) VALUES ('Harry Potter 1','2','144min','Aventura','12','0','0');
INSERT INTO CATALOGO (TITULO,FILME_ID,DURACAO,GENERO,CLASSIFICACAO,N_AVALIACOES,SOMA_AVALIACOES) VALUES ('Harry Potter 2','3','144min','Aventura','12','0','0');
INSERT INTO CATALOGO (TITULO,FILME_ID,DURACAO,GENERO,CLASSIFICACAO,N_AVALIACOES,SOMA_AVALIACOES) VALUES ('Harry Potter 3','4','144min','Aventura','12','0','0');
INSERT INTO CATALOGO (TITULO,FILME_ID,DURACAO,GENERO,CLASSIFICACAO,N_AVALIACOES,SOMA_AVALIACOES) VALUES ('Harry Potter 4','5','144min','Aventura','12','0','0');
INSERT INTO CATALOGO (TITULO,FILME_ID,DURACAO,GENERO,CLASSIFICACAO,N_AVALIACOES,SOMA_AVALIACOES) VALUES ('Harry Potter 5','6','144min','Aventura','12','0','0');
INSERT INTO CATALOGO (TITULO,FILME_ID,DURACAO,GENERO,CLASSIFICACAO,N_AVALIACOES,SOMA_AVALIACOES) VALUES ('Harry Potter 6','7','144min','Aventura','12','0','0');
INSERT INTO CATALOGO (TITULO,FILME_ID,DURACAO,GENERO,CLASSIFICACAO,N_AVALIACOES,SOMA_AVALIACOES) VALUES ('Harry Potter 7','8','144min','Aventura','12','0','0');
INSERT INTO CATALOGO (TITULO,FILME_ID,DURACAO,GENERO,CLASSIFICACAO,N_AVALIACOES,SOMA_AVALIACOES) VALUES ('Harry Potter 8','9','144min','Aventura','12','0','0');


INSERT INTO REGISTRO_PESSOAS (NOME,CPF,NASCIMENTO,SENHA,VENCIMENTO_ASSINATURA,ADMINISTRADOR,ASSINANTE) VALUES ('Admin','000','10/07/2021','000','9999-01-01','True','True');
INSERT INTO REGISTRO_PESSOAS (NOME,CPF,NASCIMENTO,SENHA,VENCIMENTO_ASSINATURA,ADMINISTRADOR,ASSINANTE) VALUES ('Eduardo Betim','10787946931','10/05/2000','123','2020-11-30','False','True');
INSERT INTO REGISTRO_PESSOAS (NOME,CPF,NASCIMENTO,SENHA,VENCIMENTO_ASSINATURA,ADMINISTRADOR,ASSINANTE) VALUES ('Alisson Fabra da Silva','12214622969','18/09/2000','321','1900-01-01','False','False');


INSERT INTO SUGESTOES (SUGESTAO) VALUES ('Velozes e furiosos 1');
INSERT INTO SUGESTOES (SUGESTAO) VALUES ('Velozes e furiosos 2');