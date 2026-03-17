DELETE FROM vacina;
ALTER TABLE vacina;

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
ALTER TABLE grupo_vulneravel;

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
ALTER TABLE vacina_grupo;

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
ALTER TABLE endereco;

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
ALTER TABLE ubs;

INSERT INTO ubs (id_ubs, nome, id_endereco) VALUES
(1234567,'ubs Romeirao',3),
(2749826,'ubs Barbalha',10),
(7654321,'ubs Centro',2),
(8765432,'ubs Triangulo',5),
(7453626,'ubs Crato',13);

DELETE FROM vacina_ubs;
ALTER TABLE vacina_ubs;

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
ALTER TABLE pessoa;

INSERT INTO pessoa (nome_pessoa, id_ubs, estado_civil) VALUES
('Vinicius Andrade Silva',1234567,'Divorciado(a)'),
('Camila Renata Gomes Barbosa',1234567,'Casado(a)'),
('Mariana Lima Pereira',1234567,'Solteiro(a)'),
('Patricia Helena Souza Martins',1234567,'Casado(a)'),

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
('Juliana Vitória Azevedo Mendes',7453626,'Solteiro(a)');
