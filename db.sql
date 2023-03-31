create database desafio_lol;

CREATE TABLE champion(
	id VARCHAR(30) PRIMARY KEY,
	`key` VARCHAR(10),
    name VARCHAR(50),
	title VARCHAR(80),
	blurb text,
    version VARCHAR(20)
); 

CREATE TABLE spells (
	idspells int PRIMARy key auto_increment,
    id VARCHAR(30), 
	name VARCHAR(50),
	description TEXT,
	champion_id VARCHAR(30),
    spells_index INT(1),
    spells_key CHAR(1)
);

ALTER TABLE spells ADD CONSTRAINT fk_spells_champions FOREIGN KEY (champion_id) REFERENCES champions(id);



