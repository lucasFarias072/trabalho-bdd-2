

class Especie:
    """
    CREATE TABLE ESPECIE (
        cod_esp SERIAL PRIMARY KEY,
        nome VARCHAR(50) 
    );
    """

class Porte:
    """
    CREATE TABLE PORTE(
        cod_pt SERIAL PRIMARY KEY,
        nome VARCHAR(50),
        peso_min FLOAT,
        peso_max FLOAT
    );
    """

# [Especie.cod_esp_fk, Porte.cod_pt_fk] 
class Raca:
    """
    CREATE TABLE RACA(
        cod_raca SERIAL PRIMARY KEY,
        cod_esp_fk INT,
        cod_pt_fk INT,
        nome VARCHAR(50),
        
        FOREIGN KEY (cod_esp_fk) REFERENCES ESPECIE(cod_esp) ON DELETE SET NULL,
        FOREIGN KEY (cod_pt_fk) REFERENCES PORTE(cod_pt) ON DELETE SET NULL
    );
    """

class Tutor:
    """
    CREATE TABLE TUTOR(
        cod_tutor SERIAL PRIMARY KEY,
        cpf VARCHAR(11),
        nome VARCHAR(70),
        email VARCHAR(50),
        telefone VARCHAR(11)
    );
    """

# [Raca.cod_raca_fk, Tutor.cod_tutor]
class Pet:
    """
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
    """

class Clinica:
    """
    CREATE TABLE CLINICA(
        cod_cli SERIAL PRIMARY KEY,
        cnpj VARCHAR(14),
        nome VARCHAR(70),
        email VARCHAR(50),
        telefone VARCHAR(11),
        bairro VARCHAR(30),
        rua VARCHAR(50)
    );
    """

class Especialidade:
    """
    CREATE TABLE ESPECIALIDADE(
        cod_espec SERIAL PRIMARY KEY,
        nome VARCHAR(70),
        descricao VARCHAR(100)
    );
    """

class Vet_Serv:
    """
    CREATE TABLE VET_SERV(
        cod_vet_serv SERIAL PRIMARY KEY,
        nome VARCHAR(70),
        descricao VARCHAR(100),
        preco FLOAT
    );
    """

class Cli_Serv:
    """
    CREATE TABLE CLI_SERV(
        cod_cli_serv SERIAL PRIMARY KEY,
        nome VARCHAR(70),
        descricao VARCHAR(100),
        preco FLOAT
    );
    """

# [Especialidade.cod_espec, Clinica.cod_cli]
class Veterinario:
    """
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
    """

# [Vet_Serv.cod_vet_serv, Veterinario.crmv]
class Vet_Funcao:
    """
    CREATE TABLE VET_FUNCAO(
        cod_vet_funcao SERIAL PRIMARY KEY,
        cod_vet_serv_fk INT,  
        crmv_fk VARCHAR(13),  

        FOREIGN KEY (cod_vet_serv_fk) REFERENCES VET_SERV(cod_vet_serv) ON DELETE SET NULL,
        FOREIGN KEY (crmv_fk) REFERENCES VETERINARIO(crmv) ON DELETE SET NULL
    );
    """

# [CLI_SERV.cod_cli_serv, CLINICA.cod_cli]
class Cli_Funcao:
    """
    CREATE TABLE CLI_FUNCAO(
        cod_cli_funcao SERIAL PRIMARY KEY,
        cod_cli_serv_fk INT, 
        cod_cli_fk INT,

        FOREIGN KEY (cod_cli_serv_fk) REFERENCES CLI_SERV(cod_cli_serv) ON DELETE SET NULL,
        FOREIGN KEY (cod_cli_fk) REFERENCES CLINICA(cod_cli) ON DELETE SET NULL
    );
    """

# Atributos alteráveis: [diagnostico, avaliacao, status]
# Tratar: CHECK (avaliacao >= 0 AND avaliacao <= 10)
# Tratar: CHECK(status IN('agendado', 'cancelado', 'finalizado'))
class Vet_Atend:
    """
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
    """

# Atributos alteráveis: [avaliacao, status]
# Tratar: CHECK (avaliacao >= 0 AND avaliacao <= 10)
# Tratar: CHECK(status IN('agendado', 'cancelado', 'finalizado'))
class Cli_Atend:
    """
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
    """
