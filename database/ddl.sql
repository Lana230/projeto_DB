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

CREATE TABLE cidadao (
    num_sus INTEGER PRIMARY KEY NOT NULL,
    data_nascimento TEXT NOT NULL,
    genero TEXT CHECK (genero = 'F' OR genero = 'M'),
    naturalidade TEXT,
    id_endereco INTEGER NOT NULL,
    cpf_pessoa TEXT NOT NULL,
    
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco),
    FOREIGN KEY (cpf_pessoa) REFERENCES pessoa(cpf_pessoa),
    UNIQUE (cpf_pessoa)
);

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

CREATE TABLE enfermeiro (
    cip TEXT PRIMARY KEY,
    cpf_pessoa TEXT NOT NULL,

    FOREIGN KEY (cpf_pessoa) REFERENCES pessoa(cpf_pessoa)
    UNIQUE (cpf_pessoa)
);

CREATE TABLE exame (
    id_exame INTEGER PRIMARY KEY AUTOINCREMENT,
    id_consulta INTEGER NOT NULL,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    grau_urgencia NUMERIC,
    status TEXT DEAFULT 'Solicitado',

    FOREIGN KEY (id_consulta) REFERENCES consulta(id_consulta)
);

CREATE TABLE fila (
    id_fila INTEGER PRIMARY KEY AUTOINCREMENT,
    num_sus INTEGER NOT NULL,
    id_ubs INTEGER NOT NULL,
    tipo_atendimento TEXT NOT NULL,
    data_solicitacao TEXT,
    posicao_atual INTEGER NOT NULL,
    status INTEGER DEFAULT 0,
    prioridade_calculada NUMERIC DEFAULT 0,
    motivo_prioridade TEXT,

    FOREIGN KEY (num_sus) REFERENCES cidadao(num_sus),
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs)
);

CREATE TABLE medico (
    crm INTEGER PRIMARY KEY,
    especialidade TEXT NOT NULL,
    cpf_pessoa TEXT NOT NULL,

    FOREIGN KEY (cpf_pessoa) REFERENCES pessoa(cpf_pessoa),
    UNIQUE (cpf_pessoa)
);

CREATE TABLE pessoa (
    cpf_pessoa TEXT PRIMARY KEY CHECK (length(cpf_pessoa) = 11),
    nome TEXT NOT NULL,
    id_ubs INTEGER NOT NULL,

    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs)
);

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

CREATE TABLE ubs (
    id_ubs INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    id_endereco INTEGER NOT NULL,

    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
);

CREATE TABLE vacina (
    id_vacina INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    previne TEXT NOT NULL,
    quantidade_disponivel NUMERIC DEFAULT 0,
    id_ubs INTEGER REFERENCES ubs(id_ubs),

    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs)
);