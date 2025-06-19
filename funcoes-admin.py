

def limpar_tabelas():
    """
    BEGIN;
    SET CONSTRAINTS ALL DEFERRED;
    TRUNCATE TABLE ESPECIE, PORTE, RACA, TUTOR, PET, CLINICA, ESPECIALIDADE, VET_SERV, CLI_SERV, VETERINARIO, VET_FUNCAO, CLI_FUNCAO RESTART IDENTITY CASCADE;
    COMMIT;
    """

def derrubar_tabelas():
    """
    ROLLBACK;
    BEGIN;
    SET CONSTRAINTS ALL DEFERRED;
    DROP TABLE ESPECIE CASCADE;
    DROP TABLE PORTE CASCADE;
    DROP TABLE RACA CASCADE;
    DROP TABLE TUTOR CASCADE;
    DROP TABLE PET CASCADE;
    DROP TABLE CLINICA CASCADE;
    DROP TABLE ESPECIALIDADE CASCADE;
    DROP TABLE VET_SERV CASCADE;
    DROP TABLE CLI_SERV CASCADE;
    DROP TABLE VETERINARIO CASCADE;
    DROP TABLE VET_FUNCAO CASCADE;
    DROP TABLE CLI_FUNCAO CASCADE;
    DROP TABLE VET_ATEND CASCADE;
    DROP TABLE CLI_ATEND CASCADE;
    COMMIT;
    """

def criar_tabelas():
    """
    CREATE OR REPLACE FUNCTION criar_tabelas() RETURNS VOID AS $$
    BEGIN
    CREATE TABLE ESPECIE (
            cod_esp SERIAL PRIMARY KEY,
            nome VARCHAR(50) 
        );

        CREATE TABLE PORTE(
            cod_pt SERIAL PRIMARY KEY,
            nome VARCHAR(50),
            peso_min FLOAT,
            peso_max FLOAT
        );

        CREATE TABLE RACA(
            cod_raca SERIAL PRIMARY KEY,
            cod_esp_fk INT,
            cod_pt_fk INT,
            nome VARCHAR(50),
            
            FOREIGN KEY (cod_esp_fk) REFERENCES ESPECIE(cod_esp) ON DELETE SET NULL,
            FOREIGN KEY (cod_pt_fk) REFERENCES PORTE(cod_pt) ON DELETE SET NULL
        );

        CREATE TABLE TUTOR(
            cod_tutor SERIAL PRIMARY KEY,
            cpf VARCHAR(11),
            nome VARCHAR(70),
            email VARCHAR(50),
            telefone VARCHAR(11)
        );

        CREATE TABLE PET(
            cod_pet SERIAL PRIMARY KEY,
            cod_raca_fk INT,
            cod_tutor_fk INT,
            nome VARCHAR(70),
            sexo CHAR(1),
            dt_cadastro DATE,

            FOREIGN KEY (cod_raca_fk) REFERENCES RACA(cod_raca) ON DELETE SET NULL,
            FOREIGN KEY (cod_tutor_fk) REFERENCES TUTOR(cod_tutor) ON DELETE SET NULL
        );

        CREATE TABLE CLINICA(
            cod_cli SERIAL PRIMARY KEY,
            cnpj VARCHAR(14),
            nome VARCHAR(70),
            email VARCHAR(50),
            telefone VARCHAR(11),
            bairro VARCHAR(30),
            rua VARCHAR(50)
        );

        CREATE TABLE ESPECIALIDADE(
            cod_espec SERIAL PRIMARY KEY,
            nome VARCHAR(70),
            descricao VARCHAR(100)
        );

        CREATE TABLE VET_SERV(
            cod_vet_serv SERIAL PRIMARY KEY,
            nome VARCHAR(70),
            descricao VARCHAR(100),
            preco FLOAT
        );

        CREATE TABLE CLI_SERV(
            cod_cli_serv SERIAL PRIMARY KEY,
            nome VARCHAR(70),
            descricao VARCHAR(100),
            preco FLOAT
        );

        CREATE TABLE VETERINARIO(
            crmv VARCHAR(13) NOT NULL PRIMARY KEY,
            cod_espec_fk INT,
            cod_cli_fk INT,
            cpf VARCHAR(11),
            nome VARCHAR(70),
            email VARCHAR(50),
            telefone VARCHAR(11),

            FOREIGN KEY (cod_espec_fk) REFERENCES ESPECIALIDADE(cod_espec) ON DELETE SET NULL,
            FOREIGN KEY (cod_cli_fk) REFERENCES CLINICA(cod_cli) ON DELETE SET NULL
        );

        CREATE TABLE VET_FUNCAO(
            cod_vet_funcao SERIAL PRIMARY KEY,
            cod_vet_serv_fk INT,  
            crmv_fk VARCHAR(13),  

            FOREIGN KEY (cod_vet_serv_fk) REFERENCES VET_SERV(cod_vet_serv) ON DELETE SET NULL,
            FOREIGN KEY (crmv_fk) REFERENCES VETERINARIO(crmv) ON DELETE SET NULL
        );

        CREATE TABLE CLI_FUNCAO(
            cod_cli_funcao SERIAL PRIMARY KEY,
            cod_cli_serv_fk INT, 
            cod_cli_fk INT,

            FOREIGN KEY (cod_cli_serv_fk) REFERENCES CLI_SERV(cod_cli_serv) ON DELETE SET NULL,
            FOREIGN KEY (cod_cli_fk) REFERENCES CLINICA(cod_cli) ON DELETE SET NULL
        );

        CREATE TABLE VET_ATEND(
            cod_vet_atend SERIAL PRIMARY KEY,
            cod_vet_funcao_fk INT,
            cod_pet_fk INT,
            valor FLOAT,
            diagnostico VARCHAR(100),
            dt_atend TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            avaliacao INT,
            status VARCHAR(20), 

            FOREIGN KEY (cod_vet_funcao_fk) REFERENCES VET_FUNCAO(cod_vet_funcao) ON DELETE SET NULL,
            FOREIGN KEY (cod_pet_fk) REFERENCES PET(cod_pet) ON DELETE SET NULL
        );

        CREATE TABLE CLI_ATEND(
            cod_cli_atend SERIAL PRIMARY KEY,
            cod_cli_funcao_fk INT, 
            cod_pet_fk INT, 
            valor FLOAT,
            dt_atend TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            avaliacao INT,
            status VARCHAR(20),

            FOREIGN KEY (cod_cli_funcao_fk) REFERENCES CLI_FUNCAO(cod_cli_funcao) ON DELETE SET NULL,
            FOREIGN KEY (cod_pet_fk) REFERENCES PET(cod_pet) ON DELETE SET NULL
        );
        RAISE INFO 'Tabelas criadas';
    END;
    $$ LANGUAGE plpgsql;
    """

# Usada em: popular_todas_tabelas() [LINHAS DE CADA TABELA]
def popular_tabela():
    """
    CREATE OR REPLACE FUNCTION popular_tabela(nome_tabela TEXT) RETURNS VOID AS $$
    BEGIN
    CASE LOWER(nome_tabela)
    
    WHEN 'especie' THEN
        INSERT INTO ESPECIE (nome) VALUES 
        ('Canis lupus familiaris'),
        ('Felis catus'),
        ('Oryctolagus cuniculus'),
        ('Mesocricetus auratus'),
        ('Melopsittacus undulatus');
    
    WHEN 'porte' THEN
        INSERT INTO PORTE (nome, peso_min, peso_max) VALUES 
        ('Miniatura', 0.1, 4.0),
        ('Pequeno', 4.1, 15.0),
        ('Médio', 15.1, 30.0),
        ('Grande', 30.1, 45.0),
        ('Gigante', 45.1, 100.0);
    
    WHEN 'raca' THEN
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
    
    WHEN 'tutor' THEN
        INSERT INTO TUTOR (cpf, nome, email, telefone) VALUES 
        ('12345678901', 'Antonio', 'antonio@gmail.com', '86999111111'),
        ('23456789012', 'Bento', 'bento@gmail.com', '86999222222'),
        ('34567890123', 'Chico', 'chico@gmail.com', '86999333333'),
        ('45678901234', 'Dirceu', 'dirceu@gmail.com', '86999444444'),
        ('56789012345', 'Elena', 'elena@gmail.com', '86999555555'),
        ('67890123456', 'Fernanda', 'fernanda@gmail.com', '86999666666');
    
    WHEN 'pet' THEN
        INSERT INTO PET (cod_raca_fk, cod_tutor_fk, nome, sexo, dt_cadastro) VALUES 
        -- Pets do Antonio (tutor 1)
        (1, 1, 'Antoninho', 'M', gerar_data()),  -- Chihuahua
        (5, 1, 'Antoninha', 'F', gerar_data()),  -- Singapura

        -- Pets do Bento (tutor 2)  
        (2, 2, 'Bentinho', 'M', gerar_data()),  -- Beagle
        (9, 2, 'Bentinha', 'F', gerar_data()), -- Anão Holandês

        -- Pets do Chico (tutor 3)
        (3, 3, 'Chiquinho', 'M', gerar_data()),  -- Pastor Alemão
        (6, 3, 'Chiquinha', 'F', gerar_data()),  -- Persa

        -- Pets do Dirceu (tutor 4)
        (12, 4, 'Dirceuzinho', 'M', gerar_data()), -- Sírio
        (15, 4, 'Dirceuzinha', 'F', gerar_data()), -- Periquito Australiano

        -- Pets da Elena (tutor 5)
        (4, 5, 'Eleninho', 'M', gerar_data()), -- Labrador
        (8, 5, 'Eleninha', 'F', gerar_data()), -- SRD Gato

        -- Pets do Fernanda (tutor 6)
        (7, 6, 'Fernandinho', 'M', gerar_data()), -- Maine Coon
        (16, 6, 'Fernandinha', 'F', gerar_data()); -- Calopsita
    
    WHEN 'clinica' THEN
        INSERT INTO CLINICA (cnpj, nome, email, telefone, bairro, rua) VALUES
        ('01.234/5678-90', 'Ouro', 'ouro@gmail.com', 86988111111, 'Desembargador do Ouro', 'Alameda do Ouro'),
        ('12.345/6789-01', 'Prata', 'prata@gmail.com', 86988222222, 'Corregedor da Prata', 'Alameda da Prata'),
        ('23.456/7890-12', 'Bronze', 'bronze@gmail.com', 86988333333, 'Servidor do Bronze', 'Alameda do Bronze');
    
    WHEN 'especialidade' THEN
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
        ('Anestesista Veterinário', 'Especialista em anestesia e manejo da dor durante procedimentos cirúrgicos.');
    
    WHEN 'vet_serv' THEN
        INSERT INTO VET_SERV(nome, descricao, preco) VALUES
        ('Curso e Treinamento', 'Aulas práticas de primeiros socorros, manejo animal ou capacitação para auxiliares veterinários.', 350),
        ('Castração', 'Procedimentos cirúrgicos de esterilização realizados em eventos ou organizações.', 140),
        ('Necropsia', 'Exames post-mortem e elaboração de relatórios técnicos para seguros, processos ou investigações.', 375),
        ('Reprodução Assistida', 'Coleta e análise de sêmen, inseminação artificial, acompanhamento reprodutivo especializado.', 425),
        ('Microshipagem', 'Implantação de microchips para identificação e registro em bancos de dados nacionais/internacionais.', 115);
    
    WHEN 'cli_serv' THEN
        INSERT INTO CLI_SERV(nome, descricao, preco) VALUES
        ('Banho e Tosa', 'Higienização e corte de pelos realizados por tosadores ou auxiliares especializados', 80),
        ('Transporte', 'Serviço de busca e entrega executado por motoristas especializados ou auxiliares.', 65),
        ('Corte de Unhas', 'Procedimento estético realizado por auxiliares ou tosadores.', 30),
        ('Hospedagem', 'Hospedagem temporária com cuidados básicos realizados por auxiliares ou cuidadores.', 55),
        ('Bandagem e Curativos', 'Troca de bandagens e cuidados pós-operatórios básicos por auxiliares treinados.', 40);
    
    WHEN 'veterinario' THEN
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
    
    WHEN 'vet_funcao' THEN
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
    
    WHEN 'cli_funcao' THEN
        INSERT INTO CLI_FUNCAO (cod_cli_serv_fk, cod_cli_fk) VALUES 
        (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
        (1, 2), (2, 2), (3, 2), (5, 2),
        (1, 3), (3, 3), (5, 3);
    
    WHEN 'vet_atend' THEN
        INSERT INTO VET_ATEND 
        (cod_vet_funcao_fk, cod_pet_fk, valor, diagnostico, dt_atend, avaliacao, status) VALUES

        --o Cebolinha já registrou todos os seus serviços
        (1, 1, 350, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 7, 'agendado'),
        (2, 2, 140, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 6, 'finalizado'),
        (3, 3, 115, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 8, 'cancelado'),

        --o Cascão registrou 2/3 de seus serviços
        (4, 4, 350, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 7, 'finalizado'),
        (5, 5, 140, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 10, 'finalizado'),

        --o Chico Bento registrou 2/3 de seus serviços
        (7, 7, 350, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 9, 'cancelado'),
        (9, 9, 115, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 8, 'agendado'),

        --o Mônica já registrou todos os seus serviços
        (10, 10, 350, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 10, 'agendado'),
        (11, 6, 140, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 10, 'finalizado'),

        --o Magali já registrou 1/3 de seus serviços 
        (14, 8, 140, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 8, 'finalizado'),

        --o Scooby já registrou todos seus serviços
        (16, 1, 375, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 6, 'finalizado'),
        (17, 2, 425, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 7, 'finalizado'),

        --o Salsicha registrou nenhum de seus serviços

        --o Fred já registrou todos seus serviços 
        (20, 3, 375, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 6, 'finalizado'),
        (21, 4, 425, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 10, 'agendado'),

        --o Daphne registrou 1/2 de seus serviços
        (23, 5, 425, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 8, 'finalizado'),

        --o Velma já registrou todos seus serviços (e repetiu 1 deles)
        (24, 6, 375, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 8, 'finalizado'),
        (25, 7, 425, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 7, 'finalizado'),
        (24, 8, 375, 'vazio', (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 9, 'finalizado');
    
    WHEN 'cli_atend' THEN
        INSERT INTO CLI_ATEND 
        (cod_cli_funcao_fk, cod_pet_fk, valor, dt_atend, avaliacao, status) VALUES

        --o Clínica Ouro registrou 3/5 dos seus serviços (2, 3, 4) de (1, 2, 3, 4, 5)
        (2, 2, 65, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 10, 'finalizado'),
        (3, 3, 30, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 8, 'finalizado'),
        (4, 4, 55, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 7, 'finalizado'),

        --o Clínica Prata registrou 3/4 dos seus serviços (1, 2, 5) de (1, 2, 3, 5)
        (6, 6, 80, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 10, 'finalizado'),
        (7, 7, 65, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 10, 'finalizado'),
        (7, 7, 65, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 7, 'agendado'),
        (9, 9, 40, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 7, 'finalizado'),
        (9, 9, 40, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 8, 'cancelado'),
        (9, 9, 40, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 8, 'finalizado'),

        --o Clínica Bronze registrou 3/3 dos seus serviços (1, 3, 5)
        (11, 11, 30, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 9, 'agendado'),
        (12, 12, 40, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 10, 'agendado'),
        (12, 12, 40, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 10, 'finalizado'),
        (11, 11, 30, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 9, 'finalizado'),
        (10, 10, 80, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 9, 'cancelado'),
        (11, 11, 30, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 7, 'finalizado'),
        (10, 10, 80, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 10, 'finalizado'),
        (10, 10, 80, (gerar_data() || ' ' || gerar_hora())::TIMESTAMP, 6, 'finalizado');
    END CASE;
    RAISE NOTICE 'Tabela % foi populada!', nome_tabela;
    END;
    $$ LANGUAGE plpgsql;
    """

# SELECT popular_todas_tabelas();
def popular_todas_tabelas():
    """
    CREATE OR REPLACE FUNCTION popular_todas_tabelas() RETURNS VOID AS $$
    DECLARE
        tabelas TEXT[] := ARRAY[
            'especie', 'porte', 'raca', 'tutor', 'clinica', 'especialidade', 'pet',
            'vet_serv', 'cli_serv', 'veterinario', 'vet_funcao', 'cli_funcao', 'vet_atend', 'cli_atend'
        ];
        tabela TEXT;
    BEGIN
        FOREACH tabela IN ARRAY tabelas
        LOOP
            PERFORM popular_tabela(tabela);
            RAISE INFO 'Tabela % populada', tabela;
            
            -- Pequena pausa para garantir que a transação seja commitada
            -- (opcional, mas pode ajudar com dependências)
            PERFORM pg_sleep(0.5);
        END LOOP;
        RAISE INFO 'Todas as tabelas foram povoadas!';
    END;
    $$ LANGUAGE plpgsql;
    """
