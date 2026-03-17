DELETE FROM vacina;

INSERT INTO vacina(tipo,previne)
VALUES
('BCG', 'Formas graves da tuberculose'),
('Hepatite B', 'Infecção crônica do fígado causada pelo vírus da hepatite B'),
('Pentavalente (DTP/Hib/Hep B)', 'Difteria, tétano, coqueluche, meningite e outras infecções causadas por Haemophilus influenzae tipo b e hepatite B'),
('VIP (Poliomielite inativada)', 'Poliomielite, conhecida como paralisia infantil'),
('VOP (Poliomielite oral)', 'Poliomielite, reforçando a proteção contra paralisia infantil'),
('Rotavírus Humano (VRH)', 'Diarreia grave causada pelo rotavírus'),
('Meningocócica C (Conjugada)', 'Meningite e outras infecções causadas pela bactéria meningococo do tipo C'),
('Pneumocócica 10-valente', 'Pneumonia, meningite, otite e outras infecções causadas pelo pneumococo'),
('Tríplice Viral (SCR)', 'Sarampo, caxumba e rubéola'),
('Febre Amarela', 'Febre amarela'),
('HPV4', 'Cânceres relacionados ao HPV e verrugas genitais'),
('Meningocócica ACWY', 'Meningites e infecções causadas pelos sorogrupos A, C, W e Y do meningococo'),
('dT (Dupla Adulto)', 'Difteria e tétano'),
('Influenza', 'Gripe causada pelo vírus influenza'),
('Covid-19', 'Doença respiratória causada pelo coronavírus SARS-CoV-2'),
('Pneumocócica 23-valente', 'Pneumonia, meningite e outras infecções causadas pelo pneumococo'),
('dTpa', 'Difteria, tétano e coqueluche');

DELETE FROM grupo_vulneravel;

INSERT INTO grupo_vulneravel (nome_grupo, peso_prioridade, descricao) 
VALUES
('Imunossuprimidos', 5, 'Pessoas cujo sistema imunológico está enfraquecido devido a doenças ou tratamentos médicos, como pacientes transplantados, em quimioterapia ou com doenças que reduzem a defesa do organismo.'),
('Crianças', 5, 'Indivíduos desde o nascimento até aproximadamente 12 anos de idade que necessitam de cuidados específicos para o desenvolvimento físico, emocional e social.'),
('Gestantes', 5, 'Mulheres em período de gravidez que necessitam de acompanhamento pré-natal e cuidados específicos para garantir a saúde da mãe e do bebê.'),
('Puérperas', 4, 'Mulheres no período pós-parto que estão em processo de recuperação física e adaptação após o nascimento do bebê.'),
('Idosos', 5, 'Pessoas com idade igual ou superior a 60 anos, geralmente mais vulneráveis a doenças crônicas e que podem necessitar de maior acompanhamento em saúde.'),
('Pessoas com doenças crônicas', 4, 'Indivíduos diagnosticados com doenças de longa duração, como diabetes, hipertensão ou doenças cardíacas, que exigem acompanhamento contínuo.'),
('Pessoas com deficiência', 4, 'Indivíduos com impedimentos físicos, mentais, intelectuais ou sensoriais de longo prazo que podem limitar sua participação plena na sociedade.'),
('Pessoas com transtornos mentais', 3, 'Pessoas que apresentam condições que afetam o funcionamento psicológico ou emocional, como depressão, ansiedade ou outros transtornos mentais.'),
('Pessoas em situação de rua', 4, 'Indivíduos que não possuem moradia fixa ou adequada e vivem em situação de vulnerabilidade social.'),
('População indígena', 5, 'Povos originários do território brasileiro com culturas, tradições e organizações sociais próprias que requerem atenção diferenciada em políticas públicas.'),
('População quilombola', 5, 'Comunidades tradicionais formadas por descendentes de africanos escravizados que preservam identidade cultural, social e territorial própria.'),
('População privada de liberdade', 4, 'Pessoas que se encontram sob custódia do sistema prisional e necessitam de acesso garantido a serviços de saúde e assistência.'),
('Usuários de álcool e drogas', 3, 'Indivíduos que fazem uso problemático ou dependente de substâncias psicoativas e podem necessitar de acompanhamento e tratamento especializado.'),
('Pessoas com HIV/IST', 5, 'Indivíduos diagnosticados com HIV ou outras infecções sexualmente transmissíveis que precisam de acompanhamento médico contínuo.'),
('Adolescentes', 3, 'Pessoas que se encontram na fase de transição entre a infância e a vida adulta, geralmente entre 12 e 18 anos.'),
('Vítimas de violência', 4, 'Indivíduos que sofreram algum tipo de violência física, psicológica ou sexual e necessitam de apoio e acompanhamento especializado.'),
('Recem-Nascidos',5,'Bebês desde o nascimento até aproximadamente 28 dias de vida.');

DELETE FROM vacina_grupo;

INSERT INTO vacina_grupo (id_vacina, id_grupo) VALUES
(1,17), 
(2,17), 
(3,2),  
(4,2),  
(5,2),  
(6,2),  
(7,2),  
(8,2),  
(9,2),  
(10,2), 
(11,15), 
(12,15), 
(13,5), 
(13,3), 
(14,5), 
(14,4), 
(14,1), 
(15,1), 
(15,5), 
(15,6), 
(16,5), 
(16,6),
(17,3);

DELETE FROM endereco;

INSERT INTO endereco (rua, bairro, numero, cidade, estado, cep) VALUES
('Rua das Flores','Centro','12','Barbalha','CE','63180000'),
('Rua José Marrocos','Centro','15','Juazeiro do Norte','CE','63010120'),
('Rua Santa Luzia','Romeirão','33','Juazeiro do Norte','CE','63050300'),
('Rua Coronel Teixeira','Pimenta','886','Crato','CE','63105000'),
('Rua São Francisco','Triângulo','543','Juazeiro do Norte','CE','63041000'),
('Rua das Acácias','Centro','45','Juazeiro do Norte','CE','63010050'),
('Rua Padre Cícero','Centro','120','Juazeiro do Norte','CE','63050210'),
('Rua São Pedro','Triângulo','78','Juazeiro do Norte','CE','63041020'),
('Rua Bela Vista','Bairro do Rosário','210','Barbalha','CE','63050560'),
('Rua da Paz','Centro','33','Barbalha','CE','63180020'),
('Rua Nova Esperança','Muriti','92','Crato','CE','63106030'),
('Rua José de Alencar','Centro','150','Crato','CE','63100040'),
('Rua Dom Pedro II','Pimenta','64','Crato','CE','63105070'),
('Rua São José','Centro','81','Barbalha','CE','63180040'),
('Rua das Mangueiras','Triângulo','305','Juazeiro do Norte','CE','63041230'),
('Rua Santo Antônio','Centro','45','Barbalha','CE','63180000'),
('Rua Padre Ibiapina','Malvinas','120','Barbalha','CE','63180020'),
('Rua São Jorge','Romeirão','101','Juazeiro do Norte','CE','63050000'),
('Rua das Oliveiras','Romeirão','202','Juazeiro do Norte','CE','63050010'),
('Rua Padre Cícero','Romeirão','303','Juazeiro do Norte','CE','63050020'),
('Rua Santa Luzia','Romeirão','404','Juazeiro do Norte','CE','63050030'),
('Rua do Rosário','Romeirão','505','Juazeiro do Norte','CE','63050040'),
('Rua São Pedro','Centro','88','Juazeiro do Norte','CE','63010000'),
('Rua São Paulo','Centro','190','Juazeiro do Norte','CE','63010020'),
('Rua das Mangueiras','Triângulo','50','Juazeiro do Norte','CE','63041000'),
('Rua das Palmeiras','Triângulo','61','Juazeiro do Norte','CE','63041010'),
('Rua José de Alencar','Triângulo','72','Juazeiro do Norte','CE','63041020'),
('Rua Padre Cícero','Triângulo','83','Juazeiro do Norte','CE','63041030'),
('Rua Coronel Antônio Luiz','Centro','150','Crato','CE','63100000'),
('Rua Tristão Gonçalves','Pimenta','320','Crato','CE','63105000');

DELETE FROM ubs;

INSERT INTO ubs (id_ubs, nome, id_endereco) VALUES
(1234567,'ubs Romeirao',3),
(2749826,'ubs Barbalha',10),
(7654321,'ubs Centro',2),
(8765432,'ubs Triangulo',5),
(7453626,'ubs Crato',13);

DELETE FROM vacina_ubs;

INSERT INTO vacina_ubs (id_vacina,id_ubs,num_lote,quantidade_disponivel,validade)
VALUES

(6,1234567,'ROTA221',35,'2027-04-10'),
(7,1234567,'MEN330',25,'2027-06-15'),
(9,1234567,'SCR540',40,'2027-03-20'),
(13,1234567,'DT112',60,'2028-01-15'),
(1,2749826,'BCG410',30,'2027-05-18'),
(2,2749826,'HEPB515',45,'2027-07-21'),
(11,2749826,'HPV888',55,'2027-08-30'),
(12,2749826,'MENACWY221',30,'2027-09-14'),
(3,7654321,'PENTA550',50,'2027-10-10'),
(6,7654321,'ROTA601',40,'2027-05-09'),
(13,7654321,'DT660',70,'2028-02-02'),
(16,7654321,'PNEU23A11',25,'2027-11-12'),
(2,8765432,'HEPB777',50,'2027-07-07'),
(4,8765432,'VIP443',45,'2027-08-12'),
(8,8765432,'PNEU10221',35,'2027-09-18'),
(17,8765432,'DTPA100',40,'2027-12-05'),
(1,7453626,'BCG990',25,'2027-04-22'),
(5,7453626,'VOP320',60,'2027-06-17'),
(10,7453626,'FA550',30,'2027-11-25'),
(16,7453626,'PNEU23B20',20,'2027-12-10'),
(1,1234567,'BCG001',40,'2027-05-10'),
(2,1234567,'HEPB210',60,'2027-08-20'),
(3,1234567,'PENTA115',50,'2027-09-15'),
(14,1234567,'FLU550',100,'2026-12-01'),
(4,2749826,'VIP332',45,'2027-07-11'),
(7,2749826,'MEN220',35,'2027-04-18'),
(8,2749826,'PNEU441',30,'2027-06-22'),
(15,2749826,'COVID778',120,'2026-11-10'),
(9,7654321,'SCR210',55,'2027-03-30'),
(10,7654321,'FA990',25,'2027-10-10'),
(14,7654321,'FLU771',90,'2026-12-05'),
(11,8765432,'HPV600',70,'2027-08-14'),
(15,8765432,'COVID800',130,'2026-10-20'),
(14,8765432,'FLU990',95,'2026-12-15'),
(2,7453626,'HEPB333',40,'2027-07-07'),
(3,7453626,'PENTA777',35,'2027-09-19'),
(8,7453626,'PNEU888',28,'2027-05-11'),
(14,7453626,'FLU600',80,'2026-11-30');

DELETE FROM pessoa;

INSERT INTO pessoa (nome_pessoa, id_ubs, estado_civil) VALUES
('Vinicius Andrade Silva',1234567,'Divorciado(a)'),
('Camila Renata Gomes Barbosa',1234567,'Casado(a)'),
('Mariana Lima Pereira',1234567,'Solteiro(a)'),
('Patricia Helena Souza Martins',1234567,'Casado(a)'),
('Lucas Andrade Silva',1234567,'Solteiro(a)'),
('Mariana Andrade Silva',1234567,'Solteiro(a)'),
('Rafael Gomes Barbosa',1234567,'Solteiro(a)'),
('Ana Beatriz Gomes Barbosa',1234567,'Solteiro(a)'),
('Camila Rocha Pereira',1234567,'Solteiro(a)'),
('Felipe Souza Martins',1234567,'Solteiro(a)')

('Carlos Eduardo Almeida Rocha',2749826,'Solteiro(a)'),
('Mariana Fernanda Ribeiro Costa',2749826,'Casado(a)'),
('Carla Mendes Monteiro Souza',2749826,'Casado(a)'),
('Juliana Costa Ribeiro Santos',2749826,'Casado(a)'),

('Marcos Batista Nogueira',7654321,'Casado(a)'),
('Patrícia Martins Cardoso',7654321,'Solteiro(a)'),
('Juliana Alves Rocha',7654321,'Solteiro(a)'),
('Carlos Eduardo Lima',7654321,'Casado(a)'),
('Fernanda Costa Ribeiro',7654321,'Solteiro(a)'),

('Camila Gomes Silva',8765432,'Solteiro(a)'),
('Rodrigo Rocha Almeida',8765432,'Divorciado(a)'),
('Débora Cristina Gomes',8765432,'Solteiro(a)'),
('Sérgio Henrique Fernandes Souza',8765432,'Casado(a)'),
('Tatiane Alves Barbosa',8765432,'Solteiro(a)'),

('Gabriel Luiz Pereira',7453626,'Casado(a)'),
('Larissa Santos Gomes',7453626,'Solteiro(a)'),
('André Felipe Batista Oliveira',7453626,'Divorciado(a)'),
('Patrícia Fernanda Barros Lima',7453626,'Solteiro(a)'),
('Ricardo Augusto Farias Teixeira',7453626,'Casado(a)'),
('Juliana Vitória Azevedo Mendes',7453626,'Solteiro(a)'),

('Ana Beatriz Silva Santos',1234567,'Casado(a)'),
('Mariana Souza Oliveira',1234567,'Solteiro(a)'),
('Joao Pedro Batista Nogueira',1234567,'Solteiro(a)'),
('Rafael Henrique Barbosa Lima',1234567,'Divorciado(a)'),

('Juliana Costa Pereira',2749826,'Casado(a)'),
('Camila Rodrigues Almeida',2749826,'Solteiro(a)'),
('Rafael Tavares Nogueira',2749826,'Casado(a)'),
('Carla Mendes Ferreira',2749826,'Uniao Estavel'),

('Larissa Martins Carvalho',7654321,'Casado(a)'),
('Fernanda Gomes Barbosa',7654321,'Divorciado(a)'),
('Bruna Alves Rodrigues',7654321,'Solteiro(a)'),
('Tatiane Souza Martins',7654321,'Casado(a)'),

('Gabriela Ribeiro Fernandes',8765432,'Solteiro(a)'),
('Patrícia Alves Monteiro',8765432,'Casado(a)'),
('Debora Lima Carvalho',8765432,'Divorciado(a)'),
('Aline Rocha Pereira',8765432,'Uniao Estavel'),

('Renata Rocha Cardoso',7453626,'Casado(a)'),
('Vanessa Teixeira Lopes',7453626,'Solteiro(a)'),
('Rodrigo Alves Ferreira',7453626,'Casado(a)'),
('Patrícia Gomes Barbosa',7453626,'Divorciado(a)'),

('Carlos Eduardo Mendes Silva', 1234567, 'Casado(a)'),
('Fernanda Cristina Alves Rocha', 1234567, 'Solteiro(a)'),
('Paulo Henrique Batista Souza', 2749826, 'Divorciado(a)'),
('Juliana Martins de Oliveira', 2749826, 'Casado(a)'),

('Ricardo Gomes Pereira', 7654321, 'Solteiro(a)'),
('Aline Barbosa dos Santos', 7654321, 'Uniao Estavel'),
('Marcos Vinicius Teixeira Lima', 8765432, 'Casado(a)'),
('Patricia Fernandes Costa', 8765432, 'Solteiro(a)');

DELETE FROM cidadao;

INSERT INTO cidadao
(num_sus,data_nascimento,genero,naturalidade,ocupacao,id_endereco,id_pessoa)
VALUES
-- UBS 1234567 (Romeirão)
(9000001,'1985-02-12','M','Juazeiro do Norte','Pedreiro',18,1),
(9000002,'1990-04-21','F','Juazeiro do Norte','Professora',19,2),
(9000003,'2001-07-10','F','Juazeiro do Norte','Recepcionista',20,3),
(9000004,'1988-09-30','F','Juazeiro do Norte','Costureira',21,4),
(9500001,'2026-03-01','M','Juazeiro do Norte','Recém-nascido',18,25),
(9500002,'2026-02-27','M','Juazeiro do Norte','Recém-nascido',19,27),
(9500003,'2018-04-12','F','Juazeiro do Norte','Estudante',18,26),
(9500004,'2017-09-03','F','Juazeiro do Norte','Estudante',19,28),
(9500005,'2016-06-21','F','Juazeiro do Norte','Estudante',20,29),
(9500006,'2015-11-14','M','Juazeiro do Norte','Estudante',21,30),

-- UBS 2749826 (Centro Barbalha)
(9000005,'1983-05-12','M','Barbalha','Comerciante',1,5),
(9000006,'1989-03-19','F','Barbalha','Enfermeira',14,6),
(9000007,'1992-08-22','F','Barbalha','Secretária',16,7),
(9000008,'1991-10-02','F','Barbalha','Vendedora',31,8),
(9700004,'2017-02-14','F','Barbalha','Estudante',16,34),
(9700001,'2015-03-12','M','Barbalha','Estudante',1,31),
(9700002,'2016-07-25','F','Barbalha','Estudante',1,32),
(9700003,'2014-11-03','M','Barbalha','Estudante',14,33),
(9700004,'2017-02-14','F','Barbalha','Estudante',16,34),
(9700005,'2018-06-18','M','Barbalha','Estudante',31,35),

-- recém-nascida (não mora com outra criança no mesmo endereço)
(9700006,'2026-02-25','F','Barbalha','Recém-nascido',16,36),

-- UBS 7654321 (Centro Juazeiro)
(9000009,'1979-11-18','M','Juazeiro do Norte','Motorista',6,9),
(9000010,'1987-06-20','F','Juazeiro do Norte','Cabeleireira',7,10),
(9000011,'1993-02-11','F','Juazeiro do Norte','Auxiliar Administrativo',23,11),
(9000012,'1986-12-01','M','Juazeiro do Norte','Vendedor',24,12),
(9000013,'1995-09-09','F','Juazeiro do Norte','Atendente',6,13),

-- UBS 8765432 (Triângulo)
(9000014,'1990-01-30','F','Juazeiro do Norte','Operadora de Caixa',8,14),
(9000015,'1984-04-15','M','Juazeiro do Norte','Motorista',15,15),
(9000016,'1996-03-12','F','Juazeiro do Norte','Recepcionista',25,16),
(9000017,'1982-08-28','M','Juazeiro do Norte','Pedreiro',26,17),
(9000018,'1994-06-18','F','Juazeiro do Norte','Comerciante',27,18),

-- UBS 7453626 (Pimenta Crato)
(9000019,'1981-07-22','M','Crato','Agricultor',4,19),
(9000020,'1997-05-14','F','Crato','Atendente',30,20),
(9000021,'1983-09-17','M','Crato','Motorista',4,21),
(9000022,'1991-12-10','F','Crato','Costureira',30,22),
(9000023,'1986-05-02','M','Crato','Pedreiro',4,23),
(9000024,'1994-07-25','F','Crato','Vendedora',30,24);

DELETE FROM documento;

INSERT INTO documento (tipo_documento, numero_documento, id_pessoa) VALUES
('CPF','487.354.827-46',1),
('CPF','593.148.276-55',2),
('CPF','712.639.845-03',3),
('CPF','864.120.593-91',4),

('CPF','295.743.168-44',5),
('CPF','348.915.702-66',6),
('CPF','629.504.813-77',7),
('CPF','703.281.694-20',8),

('CPF','514.837.206-18',9),
('CPF','678.349.520-31',10),
('CPF','145.983.762-04',11),
('CPF','208.764.951-63',12),
('CPF','359.820.174-55',13),

('CPF','471.693.820-72',14),
('CPF','520.483.716-09',15),
('CPF','634.981.257-11',16),
('CPF','718.450.392-86',17),
('CPF','809.317.546-94',18),

('CPF','903.845.271-33',19),
('CPF','124.690.538-47',20),
('CPF','236.481.759-82',21),
('CPF','347.920.681-15',22),
('CPF','458.172.906-64',23),
('CPF','569.381.742-28',24),

('CPF', '912.458.736-21', 37),
('CPF', '384.729.615-08', 38),
('CPF', '650.193.847-55', 39),
('CPF', '741.852.963-00', 40),

('CPF', '159.357.486-92', 41),
('CPF', '268.741.593-77', 42),
('CPF', '903.615.274-18', 43),
('CPF', '476.829.130-64', 44),

('CPF', '821.564.739-05', 45),
('CPF', '390.847.162-88', 46),
('CPF', '574.938.261-33', 47),
('CPF', '683.210.975-49', 48),

('CPF', '147.258.369-11', 49),
('CPF', '258.369.147-22', 50),
('CPF', '369.147.258-33', 51),
('CPF', '456.123.789-44', 52),

('CPF', '789.456.123-55', 53),
('CPF', '951.753.852-66', 54),
('CPF', '852.456.951-77', 55),
('CPF', '753.159.456-88', 56),

('CPF', '913.482.765-10', 57),
('CPF', '284.917.635-22', 58),
('CPF', '765.321.984-33', 59),
('CPF', '198.273.645-44', 60),

('CPF', '321.654.987-55', 61),
('CPF', '456.789.123-66', 62),
('CPF', '654.987.321-77', 63),
('CPF', '789.123.456-88', 64),

('CERTIDAO_NASCIMENTO','CN-2025-000025',25),
('CERTIDAO_NASCIMENTO','CN-2025-000026',26),
('CERTIDAO_NASCIMENTO','CN-2025-000027',27),
('CERTIDAO_NASCIMENTO','CN-2025-000028',28),
('CERTIDAO_NASCIMENTO','CN-2025-000029',29),
('CERTIDAO_NASCIMENTO','CN-2025-000030',30),
('CERTIDAO_NASCIMENTO','CN-2025-000031',31),
('CERTIDAO_NASCIMENTO','CN-2025-000032',32),
('CERTIDAO_NASCIMENTO','CN-2025-000033',33),
('CERTIDAO_NASCIMENTO','CN-2025-000034',34),
('CERTIDAO_NASCIMENTO','CN-2025-000035',35),
('CERTIDAO_NASCIMENTO','CN-2025-000036',36);

DELETE FROM dependente;

INSERT INTO dependente (id_responsavel, id_dependente, parentesco)
VALUES
(11,31,'Pai'),
(11,32,'Pai'),

(12,33,'Mãe'),

(13,34,'Mãe'),

(14,35,'Mãe'),
(14,36,'Mãe'),

(1,25,'Pai'),
(1,26,'Pai'),

(2,27,'Mãe'),
(2,28,'Mãe'),

(3,29,'Responsável'),

(4,30,'Mãe');

DELETE FROM cidadao_grupo;

INSERT INTO cidadao_grupo(num_sus,id_grupo)
VALUES
(9700006,17),
(9500001,17),
(9500002,17),
(9700004,2),
(9700001,2),
(9700002,2),
(9700003,2),
(9700005,2),
(9500003,2),
(9500004,2),
(9500005,2),
(9500006,2);

DELETE FROM email;

INSERT INTO email (endereco_email, id_pessoa) VALUES
('vinicius.andrade@email.com', 1),
('camila.gomes@email.com', 2),
('mariana.pereira@email.com', 3),
('patricia.martins@email.com', 4),
('carlos.rocha@email.com', 5),
('mariana.costa@email.com', 6),
('carla.souza@email.com', 7),
('juliana.santos@email.com', 8),
('marcos.nogueira@email.com', 9),
('patricia.cardoso@email.com', 10),
('juliana.rocha@email.com', 11),
('carlos.lima@email.com', 12),
('fernanda.ribeiro@email.com', 13),
('camila.silva@email.com', 14),
('rodrigo.almeida@email.com', 15),
('debora.gomes@email.com', 16),
('sergio.souza@email.com', 17),
('tatiane.barbosa@email.com', 18),
('gabriel.pereira@email.com', 19),
('larissa.gomes@email.com', 20),
('andre.oliveira@email.com', 21),
('patricia.lima@email.com', 22),
('ricardo.teixeira@email.com', 23);

INSERT INTO email (endereco_email, id_ubs) VALUES
('romeirao@ubs.com', 1234567),
('barbalha@ubs.com', 2749826),
('centro@ubs.com', 7654321),
('triangulo@ubs.com', 8765432),
('crato@ubs.com', 7453626);

DELETE FROM email;

INSERT INTO telefone (num_telefone, id_pessoa) VALUES
('(88) 99000-0001', 1),
('(88) 99000-0002', 2),
('(88) 99000-0003', 3),
('(88) 99000-0004', 4),
('(88) 99000-0005', 5),
('(88) 99000-0006', 6),
('(88) 99000-0007', 7),
('(88) 99000-0008', 8),
('(88) 99000-0009', 9),
('(88) 99000-0010', 10),
('(88) 99000-0011', 11),
('(88) 99000-0012', 12),
('(88) 99000-0013', 13),
('(88) 99000-0014', 14),
('(88) 99000-0015', 15),
('(88) 99000-0016', 16),
('(88) 99000-0017', 17),
('(88) 99000-0018', 18),
('(88) 99000-0019', 19),
('(88) 99000-0020', 20),
('(88) 99000-0021', 21),
('(88) 99000-0022', 22),
('(88) 99000-0023', 23);

DELETE FROM telefone;

INSERT INTO telefone (num_telefone, id_ubs) VALUES
('(88) 3511-0001', 1234567),
('(88) 3532-0002', 2749826),
('(88) 3521-0003', 7654321),
('(88) 3571-0004', 8765432),
('(88) 3512-0005', 7453626);

DELETE FROM medico;

INSERT INTO medico (crm, especialidade, id_pessoa) VALUES
(1001, 'Ginecologista', 37),
(1002, 'Pediatria', 38),
(1003, 'Psiquiatria', 39),
(1004, 'Clinico Geral', 40),

(1005, 'Ginecologista', 41),
(1006, 'Clinico Geral', 42),
(1007, 'Pediatria', 43),
(1008, 'Clinico Geral', 44),

(1009, 'Ginecologista', 45),
(1010, 'Clinico Geral', 46),
(1011, 'Clinico Geral', 47),
(1012, 'Clinico Geral', 48),

(1013, 'Clinico Geral', 49),
(1014, 'Ginecologista', 50),
(1015, 'Clinico Geral', 51),
(1016, 'Clinico Geral', 52),

(1017, 'Ginecologista', 53),
(1018, 'Pediatria', 54),
(1019, 'Clinico Geral', 55),
(1020, 'Clinico Geral', 56);

DELETE FROM enfermeiro;

INSERT INTO enfermeiro (cip, id_pessoa) VALUES
('ENF1001', 57),
('ENF1002', 58),
('ENF1003', 59),
('ENF1004', 60),

('ENF1005', 61),
('ENF1006', 62),
('ENF1007', 63),
('ENF1008', 64);

DELETE FROM consulta;

INSERT INTO consulta (num_sus, crm, id_ubs, motivo, habito_vida, data) 
VALUES
-- UBS Romeirão
(9000001, 1004, 1234567, 'Dor nas costas', 'Sedentário', '2026-03-10'),
(9000002, 1001, 1234567, 'Consulta de rotina', 'Ativa', '2026-03-11'),
(9000003, 1004, 1234567, 'Dor de cabeça', 'Sono irregular', '2026-03-12'),
(9000004, 1001, 1234567, 'Exame preventivo', 'Ativa', '2026-03-13'),

-- crianças / recém-nascidos
(9500001, 1002, 1234567, 'Primeira consulta', 'Recém-nascido', '2026-03-02'),
(9500003, 1002, 1234567, 'Acompanhamento escolar', 'Ativa', '2026-03-05'),

-- UBS Barbalha
(9000005, 1010, 2749826, 'Pressão alta', 'Sedentário', '2026-03-10'),
(9000006, 1005, 2749826, 'Consulta ginecológica', 'Ativa', '2026-03-11'),
(9000007, 1006, 2749826, 'Ansiedade', 'Estressada', '2026-03-12'),
(9000008, 1006, 2749826, 'Dor abdominal', 'Alimentação irregular', '2026-03-13'),

-- crianças
(9700001, 1007, 2749826, 'Febre', 'Ativo', '2026-03-09'),
(9700002, 1007, 2749826, 'Vacinação', 'Saudável', '2026-03-08'),

-- UBS Centro Juazeiro
(9000009, 1011, 7654321, 'Dor no peito', 'Tabagista', '2026-03-10'),
(9000010, 1009, 7654321, 'Consulta de rotina', 'Ativa', '2026-03-11'),
(9000011, 1012, 7654321, 'Estresse', 'Sedentária', '2026-03-12'),
(9000012, 1012, 7654321, 'Gripe', 'Ativo', '2026-03-13'),

-- UBS Triângulo
(9000014, 1014, 8765432, 'Consulta ginecológica', 'Ativa', '2026-03-10'),
(9000015, 1015, 8765432, 'Dor muscular', 'Trabalho pesado', '2026-03-11'),
(9000016, 1016, 8765432, 'Dor de garganta', 'Ativa', '2026-03-12'),
(9000017, 1016, 8765432, 'Cansaço', 'Sedentário', '2026-03-13'),

-- UBS Crato
(9000019, 1019, 7453626, 'Dor na coluna', 'Trabalho rural', '2026-03-10'),
(9000020, 1017, 7453626, 'Consulta ginecológica', 'Ativa', '2026-03-11'),
(9000021, 1019, 7453626, 'Pressão alta', 'Sedentário', '2026-03-12'),
(9000022, 1017, 7453626, 'Exame preventivo', 'Ativa', '2026-03-13');

DELETE FROM anamnese;

INSERT INTO anamnese (num_sus, peso, altura, data_anaminese, presao_arterial) VALUES

-- UBS Romeirão
(9000001, 78.5, 1.72, '2026-03-10', 13.5),
(9000002, 62.3, 1.60, '2026-03-11', 12.0),
(9000003, 55.0, 1.58, '2026-03-12', 11.5),
(9000004, 68.2, 1.65, '2026-03-13', 12.8),

-- crianças / recém-nascidos
(9500001, 3.2, 0.50, '2026-03-02', 8.0),
(9500003, 22.0, 1.10, '2026-03-05', 10.0),

-- UBS Barbalha
(9000005, 85.0, 1.75, '2026-03-10', 14.5),
(9000006, 64.0, 1.62, '2026-03-11', 12.3),
(9000007, 59.0, 1.60, '2026-03-12', 11.8),
(9000008, 70.0, 1.68, '2026-03-13', 12.9),

-- crianças
(9700001, 21.0, 1.08, '2026-03-09', 10.1),
(9700002, 19.5, 1.02, '2026-03-08', 10.0),

-- UBS Centro Juazeiro
(9000009, 90.0, 1.78, '2026-03-10', 15.0),
(9000010, 58.0, 1.59, '2026-03-11', 11.7),
(9000011, 60.0, 1.63, '2026-03-12', 12.1),
(9000012, 82.0, 1.74, '2026-03-13', 13.8),

-- UBS Triângulo
(9000014, 65.0, 1.64, '2026-03-10', 12.4),
(9000015, 88.0, 1.80, '2026-03-11', 14.2),
(9000016, 55.0, 1.60, '2026-03-12', 11.6),
(9000017, 79.0, 1.70, '2026-03-13', 13.5),

-- UBS Crato
(9000019, 84.0, 1.76, '2026-03-10', 14.0),
(9000020, 61.0, 1.62, '2026-03-11', 12.2),
(9000021, 87.0, 1.79, '2026-03-12', 14.3),
(9000022, 63.0, 1.64, '2026-03-13', 12.5);

INSERT INTO fila (data_fila, id_ubs, tipo_atendimento, quantidade_maxima, id_vacina) VALUES
('2026-03-24', 1234567, 'vacina', 50, 14),
('2026-03-25', 1234567, 'vacina', 40, 1),
('2026-03-24', 2749826, 'vacina', 60, 15),
('2026-03-25', 2749826, 'vacina', 30, 12),
('2026-03-24', 7654321, 'vacina', 70, 13),
('2026-03-25', 7654321, 'vacina', 25, 16),
('2026-03-24', 8765432, 'vacina', 95, 14),
('2026-03-25', 8765432, 'vacina', 40, 17),
('2026-03-24', 7453626, 'vacina', 60, 5),
('2026-03-25', 7453626, 'vacina', 30, 10);

INSERT INTO fila (data_fila, id_ubs, tipo_atendimento, quantidade_maxima, crm) VALUES
('2026-03-23', 1234567, 'consulta', 20, 1004),
('2026-03-23', 2749826, 'consulta', 18, 1002),
('2026-03-23', 7654321, 'consulta', 25, 1010),
('2026-03-23', 8765432, 'consulta', 18, 1019),
('2026-03-23', 7453626, 'consulta', 20, 1015);