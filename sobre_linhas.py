

def linhas_especie():
    """
    INSERT INTO ESPECIE (nome) VALUES 
    ('Canis lupus familiaris'),
    ('Felis catus'),
    ('Oryctolagus cuniculus'),
    ('Mesocricetus auratus'),
    ('Melopsittacus undulatus');
    """

def linhas_porte():
    """
    INSERT INTO PORTE (nome, peso_min, peso_max) VALUES 
    ('Miniatura', 0.1, 4.0),
    ('Pequeno', 4.1, 15.0),
    ('Médio', 15.1, 30.0),
    ('Grande', 30.1, 45.0),
    ('Gigante', 45.1, 100.0);
    """

def linhas_raca():
    """
    -- Cães (cod_esp = 1)
    INSERT INTO RACA (cod_esp_fk, cod_pt_fk, nome) VALUES 
    (1, 1, 'Chihuahua'),
    (1, 2, 'Beagle'),
    (1, 4, 'Pastor Alemão'),
    (1, 3, 'Labrador');

    -- Gatos (cod_esp = 2)  
    INSERT INTO RACA (cod_esp_fk, cod_pt_fk, nome) VALUES 
    (2, 1, 'Singapura'),
    (2, 2, 'Persa'),
    (2, 2, 'Maine Coon'),
    (2, 2, 'SRD Gato');

    -- Coelhos (cod_esp = 3)
    INSERT INTO RACA (cod_esp_fk, cod_pt_fk, nome) VALUES 
    (3, 1, 'Anão Holandês'),
    (3, 2, 'Lop Francês'),
    (3, 2, 'Mini Rex');

    -- Hamsters (cod_esp = 4) - usando porte miniatura para todos
    INSERT INTO RACA (cod_esp_fk, cod_pt_fk, nome) VALUES 
    (4, 1, 'Sírio'),
    (4, 1, 'Anão Russo'),
    (4, 1, 'Roborovski');

    -- Aves (cod_esp = 5) - usando porte miniatura
    INSERT INTO RACA (cod_esp_fk, cod_pt_fk, nome) VALUES 
    (5, 1, 'Periquito Australiano'),
    (5, 1, 'Calopsita'),
    (5, 1, 'Agapornis');
    """

def linhas_tutor():
    """
    INSERT INTO TUTOR (cpf, nome, email, telefone) VALUES 
    ('12345678901', 'Antonio', 'antonio@gmail.com', '86999111111'),
    ('23456789012', 'Bento', 'bento@gmail.com', '86999222222'),
    ('34567890123', 'Chico', 'chico@gmail.com', '86999333333'),
    ('45678901234', 'Dirceu', 'dirceu@gmail.com', '86999444444'),
    ('56789012345', 'Elena', 'elena@gmail.com', '86999555555'),
    ('67890123456', 'Fernanda', 'fernanda@gmail.com', '86999666666');
    """

def linhas_pet():
    """
    INSERT INTO PET (cod_raca_fk, cod_tutor_fk, nome, sexo, dt_cadastro) VALUES 
    -- Pets do Antonio (tutor 1)
    (1, 1, 'Antoninho', 'M', '2024-01-15'),  -- Chihuahua
    (5, 1, 'Antoninha', 'F', '2024-02-20'),  -- Singapura

    -- Pets do Bento (tutor 2)  
    (2, 2, 'Bentinho', 'M', '2024-01-10'),  -- Beagle
    (9, 2, 'Bentinha', 'F', '2024-03-05'), -- Anão Holandês

    -- Pets do Chico (tutor 3)
    (3, 3, 'Chiquinho', 'M', '2024-01-25'),  -- Pastor Alemão
    (6, 3, 'Chiquinha', 'F', '2024-02-15'),  -- Persa

    -- Pets do Dirceu (tutor 4)
    (12, 4, 'Dirceuzinho', 'M', '2024-03-10'), -- Sírio
    (15, 4, 'Dirceuzinha', 'F', '2024-03-12'), -- Periquito Australiano

    -- Pets da Elena (tutor 5)
    (4, 5, 'Eleninho', 'M', '2024-01-30'), -- Labrador
    (8, 5, 'Eleninha', 'F', '2024-02-25'), -- SRD Gato

    -- Pets do Fernanda (tutor 6)
    (7, 6, 'Fernandinho', 'M', '2024-02-10'), -- Maine Coon
    (16, 6, 'Fernandinha', 'F', '2024-03-08'); -- Calopsita
    """

def linhas_clinica():
    """
    INSERT INTO CLINICA (cnpj, nome, email, telefone, bairro, rua) VALUES
    ('01.234/5678-90', 'Ouro', 'ouro@gmail.com', 86988111111, 'Desembargador do Ouro', 'Alameda do Ouro'),
    ('12.345/6789-01', 'Prata', 'prata@gmail.com', 86988222222, 'Corregedor da Prata', 'Alameda da Prata'),
    ('23.456/7890-12', 'Bronze', 'bronze@gmail.com', 86988333333, 'Servidor do Bronze', 'Alameda do Bronze');
    """

def linhas_especialidade():
    """
    INSERT INTO ESPECIALIDADE (nome, descricao) VALUES
    ('Dermatologista', 'Especialista em doenças de pele, pelos, unhas e orelhas dos animais.'),
    ('Cardiologista', 'Especialista em doenças do coração e sistema cardiovascular animal.'),
    ('Oftalmologista', 'Especialista em doenças dos olhos e sistema visual dos animais.'),
    ('Ortopedista', 'Especialista em ossos, articulações, ligamentos e sistema musculoesquelético.'),
    ('Oncologista', 'Especialista no diagnóstico e tratamento de cânceres em animais.'),
    ('Neurologista', 'Especialista em doenças do sistema nervoso (cérebro, medula espinhal, nervos).'),
    ('Endocrinologista', 'Especialista em distúrbios hormonais e do sistema endócrino.'),
    ('Nefrologista', 'Especialista em doenças dos rins e sistema urinário.'),
    ('Gastroenterologista', 'Especialista em doenças do sistema digestivo (estômago, intestinos, fígado).'),
    ('Anestesista', 'Especialista em anestesia e manejo da dor durante procedimentos cirúrgicos.');
    """

def linhas_vet_serv():
    """
    INSERT INTO VET_SERV(nome, descricao, preco) VALUES
    ('Curso e Treinamento', 'Aulas práticas de primeiros socorros, manejo animal ou capacitação para auxiliares veterinários.', 350),
    ('Castração', 'Procedimentos cirúrgicos de esterilização realizados em eventos ou organizações.', 140),
    ('Necropsia', 'Exames post-mortem e elaboração de relatórios técnicos para seguros, processos ou investigações.', 375),
    ('Reprodução Assistida', 'Coleta e análise de sêmen, inseminação artificial, acompanhamento reprodutivo especializado.', 425),
    ('Microshipagem', 'Implantação de microchips para identificação e registro em bancos de dados nacionais/internacionais.', 115);
    """

def linhas_cli_serv():
    """
    INSERT INTO VET_SERV(nome, descricao, preco) VALUES
    ('Banho e Tosa', 'Higienização e corte de pelos realizados por tosadores ou auxiliares especializados', 80),
    ('Transporte', 'Serviço de busca e entrega executado por motoristas especializados ou auxiliares.', 65),
    ('Corte de Unhas', 'Procedimento estético realizado por auxiliares ou tosadores.', 30),
    ('Hospedagem', 'Hospedagem temporária com cuidados básicos realizados por auxiliares ou cuidadores.', 55),
    ('Bandagem e Curativos', 'Troca de bandagens e cuidados pós-operatórios básicos por auxiliares treinados.', 40);
    """

def linhas_veterinario():
    """
    INSERT INTO VETERINARIO (crmv, cod_espec_fk, cod_cli_fk, cpf, nome, email, telefone) VALUES 
	('CRMV-PI 0001', 1, 1, '20101010017', 'Cebolinha', 'cebolinha@gmail.com', '86988335998'),
	('CRMV-PI 0002', 3, 2, '10100117777', 'Cascão', 'cascao@gmail.com', '86988312319'),
	('CRMV-PI 0003', 5, 3, '30010101001', 'Chico Bento', 'chico@gmail.com', '86988368395'),
	('CRMV-PI 0004', 7, 1, '40101017777', 'Mônica', 'monica@gmail.com', '86988796831'),
	('CRMV-PI 0005', 9, 2, '10101017777', 'Magali', 'magali@gmail.com', '86988715198'),
	('CRMV-PI 0006', 1, 3, '40011007777', 'Scooby', 'scooby@gmail.com', '86988239956'),
	('CRMV-PI 0007', 3, 1, '10100100177', 'Salsicha', 'salsicha@gmail.com', '86988219283'),
	('CRMV-PI 0008', 5, 2, '20010777777', 'Fred', 'fred@gmail.com', '86988443300'),
	('CRMV-PI 0009', 7, 3, '10100017777', 'Daphne', 'daphne@gmail.com', '86988310663'),
	('CRMV-PI 0010', 9, 1, '20100177777', 'Velma', 'velma@gmail.com', '86988439710');
    """

# Pessoal da Turma da Mônica ficam com os serviços (1, 2, 5)
# Pessoal do Scooby-Doo ficam com os serviços (3, 4)
def linhas_vet_funcao():
    """
    INSERT INTO VET_FUNCAO (cod_vet_serv_fk, crmv_fk) VALUES 
    (1, 'CRMV-PI 0001'), (2, 'CRMV-PI 0001'), (5, 'CRMV-PI 0001'),
    (1, 'CRMV-PI 0002'), (2, 'CRMV-PI 0002'), (5, 'CRMV-PI 0002'),
    (1, 'CRMV-PI 0003'), (2, 'CRMV-PI 0003'), (5, 'CRMV-PI 0003'),
    (1, 'CRMV-PI 0004'), (2, 'CRMV-PI 0004'), (5, 'CRMV-PI 0004'),
    (1, 'CRMV-PI 0005'), (2, 'CRMV-PI 0005'), (5, 'CRMV-PI 0005'),

    (3, 'CRMV-PI 0006'), (4, 'CRMV-PI 0006'),
    (3, 'CRMV-PI 0007'), (4, 'CRMV-PI 0007'),
    (3, 'CRMV-PI 0008'), (4, 'CRMV-PI 0008'),
    (3, 'CRMV-PI 0009'), (4, 'CRMV-PI 0009'),
    (3, 'CRMV-PI 0010'), (4, 'CRMV-PI 0010');
    """

# A clínica Ouro presta todos os 5 serviços (1, 2, 3, 4, 5)
# A clínica Prata presta 4 dos 5 serviços (1, 2, 3, 5)
# A clínica Bronze presta 3 dos 5 serviços (1, 2, 5)
def linhas_cli_funcao():
    """
    INSERT INTO CLI_FUNCAO (cod_cli_serv_fk, cod_cli_fk) VALUES 
    (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
    (1, 2), (2, 2), (3, 2), (5, 2),
    (1, 3), (3, 3), (5, 3);
    """

# Salsicha é o único sem nenhum de seus serviços prestados
def linhas_vet_atend():
    """
    INSERT INTO VET_ATEND 
    (cod_vet_funcao_fk, cod_pet_fk, valor, diagnostico, dt_atend, avaliacao, status) VALUES
    
    --o Cebolinha já registrou todos os seus serviços
    (1, 1, 350, 'vazio', DEFAULT, 7, 'agendado'),
    (2, 2, 140, 'vazio', DEFAULT, 6, 'finalizado'),
    (3, 3, 115, 'vazio', DEFAULT, 8, 'cancelado'),
    
    --o Cascão registrou 2/3 de seus serviços
    (4, 4, 350, 'vazio', DEFAULT, 7, 'finalizado'),
    (5, 5, 140, 'vazio', DEFAULT, 10, 'finalizado'),

    --o Chico Bento registrou 2/3 de seus serviços
    (7, 7, 350, 'vazio', DEFAULT, 9, 'cancelado'),
    (9, 9, 115, 'vazio', DEFAULT, 8, 'agendado'),
    
    --o Mônica já registrou todos os seus serviços
    (10, 10, 350, 'vazio', DEFAULT, 10, 'agendado'),
    (11, 6, 140, 'vazio', DEFAULT, 10, 'finalizado'),

    --o Magali já registrou 1/3 de seus serviços 
    (14, 8, 140, 'vazio', DEFAULT, 8, 'finalizado'),

    --o Scooby já registrou todos seus serviços
    (16, 1, 375, 'vazio', DEFAULT, 6, 'finalizado'),
    (17, 2, 425, 'vazio', DEFAULT, 7, 'finalizado'),

    --o Salsicha registrou nenhum de seus serviços

    --o Fred já registrou todos seus serviços 
    (20, 3, 375, 'vazio', DEFAULT, 6, 'finalizado'),
    (21, 4, 425, 'vazio', DEFAULT, 10, 'agendado'),

    --o Daphne registrou 1/2 de seus serviços
    (23, 5, 425, 'vazio', DEFAULT, 8, 'finalizado'),

    --o Velma já registrou todos seus serviços (e repetiu 1 deles)
    (24, 6, 375, 'vazio', DEFAULT, 8, 'finalizado'),
    (25, 7, 425, 'vazio', DEFAULT, 7, 'finalizado'),
    (24, 8, 375, 'vazio', DEFAULT, 9, 'finalizado');
    """

def linhas_cli_atend():
    """
    INSERT INTO CLI_ATEND 
    (cod_cli_funcao_fk, cod_pet_fk, valor, dt_atend, avaliacao, status) VALUES
    
    --o Clínica Ouro registrou 3/5 dos seus serviços (2, 3, 4) de (1, 2, 3, 4, 5)
    (2, 2, 65, DEFAULT, 10, 'finalizado'),
    (3, 3, 30, DEFAULT, 8, 'finalizado'),
    (4, 4, 55, DEFAULT, 7, 'finalizado'),

    --o Clínica Prata registrou 3/4 dos seus serviços (1, 2, 5) de (1, 2, 3, 5)
    (6, 6, 80, DEFAULT, 10, 'finalizado'),
    (7, 7, 65, DEFAULT, 10, 'finalizado'),
    (7, 7, 65, DEFAULT, 7, 'agendado'),
    (9, 9, 40, DEFAULT, 7, 'finalizado'),
    (9, 9, 40, DEFAULT, 8, 'cancelado'),
    (9, 9, 40, DEFAULT, 8, 'finalizado'),

    --o Clínica Bronze registrou 3/3 dos seus serviços (1, 3, 5)
    (11, 11, 30, DEFAULT, 9, 'agendado'),
    (12, 12, 40, DEFAULT, 10, 'agendado'),
    (12, 12, 40, DEFAULT, 10, 'finalizado'),
    (11, 11, 30, DEFAULT, 9, 'finalizado'),
    (10, 10, 80, DEFAULT, 9, 'cancelado'),
    (11, 11, 30, DEFAULT, 7, 'finalizado'),
    (10, 10, 80, DEFAULT, 10, 'finalizado'),
    (10, 10, 80, DEFAULT, 6, 'finalizado');
    """
