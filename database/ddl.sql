DROP TABLE agendamento;

CREATE TABLE agendamento(
    id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
    num_sus INTEGER NOT NULL,
    data_solicitacao TEXT,
    status TEXT DEFAULT 'Pendente',
    hora_agendamento TEXT,
    posicao_atual INTEGER,
    prioridade_calculada INTEGER DEFAULT 0,
    motivo_prioridade TEXT,
    id_fila INTEGER,
    FOREIGN KEY (num_sus) REFERENCES cidadao(num_sus),
    FOREIGN KEY (id_fila) REFERENCES fila(id_fila)
);

DROP TABLE anamnese;

CREATE TABLE anamnese (
    id_anamnese INTEGER PRIMARY KEY AUTOINCREMENT,
    num_sus INTEGER NOT NULL,
    peso REAL NOT NULL,
    altura REAL NOT NULL,
    data_anamnese TEXT NOT NULL,
    pressao_arterial TEXT NOT NULL,
    FOREIGN KEY (num_sus) REFERENCES cidadao(num_sus)
);

DROP TABLE cidadao;

CREATE TABLE cidadao (
    num_sus INTEGER PRIMARY KEY,
    data_nascimento TEXT NOT NULL,
    genero TEXT CHECK (genero = 'F' OR genero = 'M'),
    naturalidade TEXT,
    ocupacao TEXT,
    id_endereco INTEGER NOT NULL,
    id_pessoa INTEGER NOT NULL,
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco),
    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa),
    UNIQUE (id_pessoa)
);

DROP TABLE cidadao_grupo;

CREATE TABLE cidadao_grupo(
    num_sus INTEGER NOT NULL,
    id_grupo INTEGER NOT NULL,
    PRIMARY KEY (num_sus, id_grupo),
    FOREIGN KEY (num_sus) REFERENCES cidadao(num_sus),
    FOREIGN KEY (id_grupo) REFERENCES grupo_vulneravel(id_grupo)
);

DROP TABLE consulta;

CREATE TABLE consulta (
    id_consulta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_agendamento INTEGER NOT NULL,
    crm TEXT NOT NULL,
    id_ubs INTEGER NOT NULL,
    motivo TEXT,
    habito_vida TEXT,
    data TEXT NOT NULL,
    FOREIGN KEY (id_agendamento) REFERENCES agendamento(id_agendamento),
    FOREIGN KEY (crm) REFERENCES medico(crm),
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs)
);

DROP TABLE dependente;

CREATE TABLE dependente(
    id_responsavel INTEGER NOT NULL,
    id_dependente INTEGER NOT NULL,
    parentesco TEXT, 
    PRIMARY KEY(id_responsavel,id_dependente),
    FOREIGN KEY (id_responsavel) REFERENCES pessoa(id_pessoa),
    FOREIGN KEY (id_dependente) REFERENCES pessoa(id_pessoa)
);

DROP TABLE documento;

CREATE TABLE documento (
    id_documento INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_documento TEXT NOT NULL,
    numero_documento TEXT NOT NULL,
    id_pessoa INTEGER NOT NULL,
    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa),
    UNIQUE (tipo_documento, numero_documento)
);

DROP TABLE email;

CREATE TABLE email (
    id_email INTEGER PRIMARY KEY AUTOINCREMENT,
    endereco_email TEXT NOT NULL,
    id_ubs INTEGER,
    id_pessoa INTEGER,
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs),
    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa),
    UNIQUE (endereco_email),
    CHECK (
        (id_ubs IS NOT NULL AND id_pessoa IS NULL) OR
        (id_ubs IS NULL AND id_pessoa IS NOT NULL)
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
    UNIQUE (rua, numero, bairro, cidade, estado, cep)
);

DROP TABLE enfermeiro;

CREATE TABLE enfermeiro (
    cip TEXT PRIMARY KEY,
    id_pessoa INTEGER NOT NULL,
    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa),
    UNIQUE (id_pessoa)
);

DROP TABLE exame;

CREATE TABLE exame (
    id_exame INTEGER PRIMARY KEY AUTOINCREMENT,
    id_consulta INTEGER NOT NULL,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    grau_urgencia NUMERIC,
    status TEXT DEFAULT 'Solicitado',
    FOREIGN KEY (id_consulta) REFERENCES consulta(id_consulta)
);


DROP TABLE fila;

CREATE TABLE fila (
    id_fila INTEGER PRIMARY KEY AUTOINCREMENT,
    data_fila TEXT NOT NULL,
    id_ubs INTEGER NOT NULL,
    tipo_atendimento TEXT NOT NULL,
    quantidade_maxima INTEGER NOT NULL CHECK (quantidade_maxima > 0),
    crm TEXT,
    id_vacina INTEGER,
    
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs),
    FOREIGN KEY (crm) REFERENCES medico(crm),
    FOREIGN KEY (id_vacina) REFERENCES vacina(id_vacina),

    CHECK (
        (crm IS NOT NULL AND id_vacina IS NULL) OR
        (id_vacina IS NOT NULL AND crm IS NULL)
    )

);

DROP TABLE grupo_vulneravel;

CREATE TABLE grupo_vulneravel(
    id_grupo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_grupo TEXT NOT NULL,
    peso_prioridade INTEGER NOT NULL,
    descricao TEXT,
    UNIQUE(nome_grupo)
);

DROP TABLE hipotese;

CREATE TABLE hipotese(
    id_hipotese INTEGER PRIMARY KEY,
    id_consulta INTEGER NOT NULL,
    doenca TEXT NOT NULL,
    cid TEXT NOT NULL,
    FOREIGN KEY (id_consulta) REFERENCES consulta(id_consulta)
);

DROP TABLE medicamento;

CREATE TABLE medicamento(
    id_medicamento INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_medicamento TEXT NOT NULL UNIQUE   
);

DROP TABLE medicamento_consulta;

CREATE TABLE medicamento_consulta(
    id_medicamento INTEGER NOT NULL,
    id_consulta INTEGER NOT NULL,
    frequencia INTEGER,
    duracao INTEGER,
    dose REAL NOT NULL,
    via TEXT NOT NULL,
    PRIMARY KEY (id_medicamento, id_consulta),
    FOREIGN KEY (id_medicamento) REFERENCES medicamento(id_medicamento),
    FOREIGN KEY (id_consulta) REFERENCES consulta(id_consulta)
);

DROP TABLE medicamento_ubs;

CREATE TABLE medicamento_ubs(
    id_medicamento_ubs INTEGER PRIMARY KEY AUTOINCREMENT,
    id_medicamento INTEGER NOT NULL,
    id_ubs INTEGER NOT NULL,
    num_lote TEXT NOT NULL,
    quantidade_disponivel INTEGER DEFAULT 0,
    validade TEXT NOT NULL,
    FOREIGN KEY (id_medicamento) REFERENCES medicamento(id_medicamento),
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs)
);

DROP TABLE medico;

CREATE TABLE medico (
    crm TEXT PRIMARY KEY,
    especialidade TEXT NOT NULL,
    id_pessoa INTEGER NOT NULL,

    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa),
    UNIQUE (id_pessoa)
);


DROP TABLE pessoa;

CREATE TABLE pessoa(
    id_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,
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
    UNIQUE (num_sus,id_vacina, data_vacina)
);

DROP TABLE telefone;

CREATE TABLE telefone (
    id_tel INTEGER PRIMARY KEY AUTOINCREMENT,
    num_telefone TEXT NOT NULL,
    id_ubs INTEGER,
    id_pessoa INTEGER,
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs),
    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa),
    UNIQUE (num_telefone),
    CHECK (
        (id_ubs IS NOT NULL AND id_pessoa IS NULL) OR
        (id_ubs IS NULL AND id_pessoa IS NOT NULL)
    )
);

DROP TABLE ubs;

CREATE TABLE ubs (
    id_ubs INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    id_endereco INTEGER NOT NULL,

    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
);

DROP TABLE usuario;

CREATE TABLE usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    id_ubs INTEGER,
    nome_usuario TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    tipo TEXT NOT NULL,
    FOREIGN KEY(id_ubs) REFERENCES ubs(id_ubs),
    UNIQUE(nome_usuario, email)
);

DROP TABLE vacina;

CREATE TABLE vacina(
    id_vacina INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    previne TEXT NOT NULL,
    UNIQUE(tipo)
);

DROP TABLE vacina_grupo;

CREATE TABLE vacina_grupo(
    id_vacina INTEGER NOT NULL,
    id_grupo INTEGER NOT NULL,
    PRIMARY KEY (id_vacina, id_grupo),

    FOREIGN KEY (id_vacina) REFERENCES vacina(id_vacina),
    FOREIGN KEY (id_grupo) REFERENCES grupo_vulneravel(id_grupo)
);

DROP TABLE vacina_ubs;

CREATE TABLE vacina_ubs(
    id_vacina_ubs INTEGER PRIMARY KEY AUTOINCREMENT,
    id_vacina INTEGER NOT NULL,
    id_ubs INTEGER NOT NULL,
    num_lote TEXT NOT NULL,
    quantidade_disponivel INTEGER DEFAULT 0,
    validade TEXT NOT NULL,
    
    FOREIGN KEY (id_vacina) REFERENCES vacina(id_vacina),
    FOREIGN KEY (id_ubs) REFERENCES ubs(id_ubs)
);