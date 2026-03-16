DROP TABLE anamnese;

CREATE TABLE anamnese (
    id_anamnese INTEGER PRIMARY KEY AUTOINCREMENT,
    num_sus INTEGER NOT NULL,
    id_consulta INTEGER NOT NULL,
    peso REAL NOT NULL,
    altura REAL NOT NULL,
    presao_arterial REAL NOT NULL,
    
    FOREIGN KEY (num_sus) REFERENCES cidadao (num_sus),
    FOREIGN KEY (id_consulta) REFERENCES consulta (id_consulta)
);

DROP TABLE cidadao;

CREATE TABLE cidadao (
    num_sus INTEGER PRIMARY KEY NOT NULL ,
    data_nascimento TEXT NOT NULL,
    genero TEXT CHECK (genero = 'F' OR genero = 'M'),
    naturalidade TEXT,
    id_endereco INTEGER NOT NULL,
    cpf_pessoa TEXT NOT NULL,
    
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco),
    FOREIGN KEY (cpf_pessoa) REFERENCES pessoa(cpf_pessoa),
    UNIQUE (cpf_pessoa)
);
-- criar tababela responsavel para guardar os dados do responsável legal do cidadão, caso seja menor de idade ou incapaz
--ALTER TABLE cidadao
--ADD ESTADO_CIVIL TEXT NOT NULL OK EM PESSOA 

DROP TABLE consulta;

CREATE TABLE consulta (
    id_consulta INTEGER PRIMARY KEY AUTOINCREMENT,
    num_sus INTEGER NOT NULL,
    crm INTEGER NOT NULL,
    id_ubs INTEGER NOT NULL,
    motivo TEXT,
    resultado TEXT,
    data_hora TEXT,

    FOREIGN KEY (num_sus) REFERENCES cidadao(num_sus),
    FOREIGN KEY (crm) REFERENCES medico(crm),
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs)
);

DROP TABLE email;

CREATE TABLE email (
    id_email INTEGER PRIMARY KEY AUTOINCREMENT,
    endereco_email TEXT NOT NULL,
    id_ubs INTEGER,
    cpf_pessoa TEXT,

    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs),
    FOREIGN KEY (cpf_pessoa) REFERENCES pessoa(cpf_pessoa),
    UNIQUE (endereco_email)
    CHECK (
        (id_ubs IS NOT NULL AND cpf_pessoa IS NULL) OR
        (id_ubs IS NULL AND cpf_pessoa IS NOT NULL)
    )
);

DROP TABLE endereco;

CREATE TABLE endereco (
    id_endereco INTEGER PRIMARY KEY AUTOINCREMENT,
    rua TEXT NOT NULL,
    bairro TEXT,
    numero TEXT,
    cidade TEXT,
    estado TEXT,
    cep TEXT NOT NULL,

    UNIQUE (rua, numero, bairro, cidade, cep)
);

DROP TABLE enfermeiro;

CREATE TABLE enfermeiro (
    cip TEXT PRIMARY KEY,
    cpf_pessoa TEXT NOT NULL,

    FOREIGN KEY (cpf_pessoa) REFERENCES pessoa(cpf_pessoa)
    UNIQUE (cpf_pessoa)
);

DROP TABLE exame;

CREATE TABLE exame (
    id_exame INTEGER PRIMARY KEY AUTOINCREMENT,
    id_consulta INTEGER NOT NULL,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    grau_urgencia NUMERIC,
    status TEXT DEAFULT 'Solicitado',

    FOREIGN KEY (id_consulta) REFERENCES consulta(id_consulta)
);


DROP TABLE fila;

CREATE TABLE fila (
    id_fila INTEGER PRIMARY KEY AUTOINCREMENT,
    data_fila TEXT NOT NULL,
    id_ubs INTEGER NOT NULL,
    tipo_atendimento TEXT NOT NULL,
    quantidade_maxima INTEGER NOT NULL,
    crm INTEGER ,
    id_vacina INTEGER ,
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs)
    FOREIGN KEY (crm) REFERENCES medico(crm),
    FOREIGN KEY (id_vacina) REFERENCES vacina(id_vacina),
    CHECK (
        (crm IS NOT NULL AND id_vacina IS NULL) OR
        (id_vacina IS NULL AND crm IS NOT NULL)
    )

);

CREATE TABLE agendamento(
    id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
    num_sus INTEGER NOT NULL,
    data_solicitacao TEXT,
    status TEXT DEFAULT 'PENDENTE',
    hora_agendamento TEXT, 
    posicao atual INTEGER,
    prioridade_calculada INTEGER DEFAULT 0,
    motivo_prioridade TEXT,

    FOREIGN KEY (num_sus) REFERENCES cidadao(num_sus)  
);

CREATE TABLE fila_agendamento(
    id_fila INTEGER NOT NULL,
    id_agendamento INTEGER NOT NULL,
    PRIMARY KEY (id_fila, id_agendamento),
     FOREIGN KEY (id_fila) REFERENCES fila(id_fila),
     FOREIGN KEY (id_agendamento) REFERENCES agendamento(id_agendamento)
);

DROP TABLE medico;

CREATE TABLE medico (
    crm INTEGER PRIMARY KEY,
    especialidade TEXT NOT NULL,
    cpf_pessoa TEXT NOT NULL,

    FOREIGN KEY (cpf_pessoa) REFERENCES pessoa(cpf_pessoa),
    UNIQUE (cpf_pessoa)
);


DROP TABLE pessoa;

CREATE TABLE pessoa(
    cpf_pessoa INTEGER PRIMARY KEY NOT NULL CHECK(length(cpf_pessoa) = 11),
    nome_pessoa TEXT NOT NULL,
    id_ubs INTEGER NOT NULL,
    estado_civil TEXT NOT NULL,
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs)
);

DROP TABLE reg_vacina;

CREATE TABLE reg_vacina (
    id_reg_vacina INTEGER PRIMARY KEY AUTOINCREMENT,
    num_sus INTEGER NOT NULL,
    id_vacina INTEGER NOT NULL,
    cip TEXT NOT NULL,
    id_ubs INTEGER NOT NULL,
    data_vacina TEXT,

    FOREIGN KEY (num_sus) REFERENCES cidadao(num_sus),
    FOREIGN KEY (id_vacina) REFERENCES vacina(id_vacina),
    FOREIGN KEY (cip) REFERENCES enfermeiro(cip),
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs),
    UNIQUE (num_sus, data_vacina)
);

DROP TABLE telefone;

CREATE TABLE telefone (
    id_tel INTEGER PRIMARY KEY AUTOINCREMENT,
    num_telefone TEXT NOT NULL,
    id_ubs INTEGER,
    cpf_pessoa TEXT,

    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs),
    FOREIGN KEY (cpf_pessoa) REFERENCES pessoa(cpf_pessoa),
    UNIQUE (num_telefone) 
    CHECK (
        (id_ubs IS NOT NULL AND cpf_pessoa IS NULL) OR
        (id_ubs IS NULL AND cpf_pessoa IS NOT NULL)
    )
);

DROP TABLE ubs;

CREATE TABLE ubs (
    id_ubs INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    id_endereco INTEGER NOT NULL,

    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
);

DROP TABLE vacina;

CREATE TABLE vacina (
    id_vacina INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    previne TEXT NOT NULL,
    quantidade_disponivel NUMERIC DEFAULT 0,
    id_ubs INTEGER REFERENCES ubs(id_ubs),
    lote TEXT NOT NULL,

    UNIQUE(tipo, id_ubs),
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs)
);


CREATE TABLE grupo_vulneravel(
    id_grupo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_grupo TEXT NOT NULL, 
	peso_prioridade
);

CREATE TABLE cidadao_grupo(
    num_sus INTEGER NOT NULL,
    id_grupo INTEGER NOT NULL,
    PRIMARY KEY (num_sus, id_grupo),

    FOREIGN KEY (num_sus) REFERENCES cidadao(num_sus),
    FOREIGN KEY (id_grupo) REFERENCES grupo_vulneravel(id_grupo)
);