

def logica_funcoes_inserir():
    """
    * A restrição de valor nulo nos atributos foi tirada por causa da lógica das funções de remoção
    * Com isso, se abre brecha para passar valores nulos nos parâmetros sem uma intervenção
    * Criar uma intervenção para impedir, substituindo a restrição padrão do SGBD
    * Valores com NULL implícito ou parâmetros omitidos na chamada, serão impedidos igualmente
    """

def insert_modelo():
    """
    CREATE OR REPLACE FUNCTION inserir_() RETURNS INTEGER AS $$
    BEGIN
        IF NOT EXISTS(SELECT 1 FROM  WHERE cod_ = _cod_) THEN RAISE EXCEPTION
        '>> CANCELAMENTO ---> chave de consulta do código de ... não consta na base de dados';
        ELSE
        RAISE INFO '>> CONFIRMAÇÃO ---> Novo ... adicionado à base de dados';
        END IF;
    END;
    $$ LANGUAGE plpgsql;
    """
    
# Por enquanto, com as 5 primeiras tabelas
def inserir_padrao():
    """
    CREATE OR REPLACE FUNCTION inserir_padrao(
        nomeTabela TEXT, 
        campoA VARCHAR DEFAULT NULL, 
        campoB VARCHAR DEFAULT NULL, 
        campoC VARCHAR DEFAULT NULL, 
        campoD VARCHAR DEFAULT NULL, 
        campoE VARCHAR DEFAULT NULL, 
        campoF VARCHAR DEFAULT NULL, 
        campoG VARCHAR DEFAULT NULL, 
        campoH VARCHAR DEFAULT NULL
    ) RETURNS INTEGER AS $$
    DECLARE 
    procedimento INTEGER;
    BEGIN
    CASE LOWER(nomeTabela)
        WHEN 'especie' THEN
        procedimento := inserir_especie(campoA::TEXT);
        WHEN 'porte' THEN
        procedimento := inserir_porte(campoA::TEXT, campoB::FLOAT, campoC::FLOAT);
        WHEN 'raca' THEN
        procedimento := inserir_raca(campoA::INT, campoB::INT, campoC::TEXT);
        WHEN 'tutor' THEN
        procedimento := inserir_tutor(campoA::TEXT, campoB::TEXT, campoC::TEXT, campoD::TEXT);
        WHEN 'pet' THEN
		procedimento := inserir_pet(campoA::INT, campoB::INT, campoC::TEXT, campoD::TEXT, campoE::DATE);
        ELSE
        RAISE EXCEPTION 'Tabela % não consta nesse modelo de negócios.', nomeTabela;
    END CASE;
    RETURN procedimento;
    END;
    $$ LANGUAGE plpgsql;
    """



###################################################################################################
# DROP FUNCTION inserir_especie(text);
# TESTADA
def inserir_especie(_nome: str):
    """
    CREATE OR REPLACE FUNCTION inserir_especie(_nome TEXT) RETURNS INTEGER AS $$
    BEGIN
    IF LENGTH(_nome) < 3 THEN RAISE EXCEPTION '>> CANCELAMENTO ---> nome de espécie muito curta';
    ELSEIF EXISTS(SELECT 1 FROM ESPECIE WHERE nome = _nome) THEN RAISE EXCEPTION 
    '>> CANCELAMENTO ---> nome de espécie já consta na base de dados';
    ELSEIF _nome IS NULL THEN RAISE EXCEPTION '>> CANCELAMENTO ---> nome de espécie não pode ser um campo nulo';
    ELSE
        INSERT INTO ESPECIE (nome) VALUES (_nome);
        RAISE NOTICE '>> CONFIRMAÇÃO ---> nova espécie adiciona à base de dados';
    END IF;
    RETURN -1;
    END;
    $$ LANGUAGE plpgsql;
    """

    testes = """
    SELECT inserir_padrao('especie')              # ERROR:  >> CANCELAMENTO ---> Nome de espécie não pode ser um campo nulo
    SELECT inserir_padrao('especie', '')          # ERROR:  >> CANCELAMENTO ---> Nome de espécie muito curta
    SELECT inserir_padrao('especie', 'Fantasma')  # -1
    SELECT inserir_padrao('especie', 'Fantasma')  # ERROR:  >> CANCELAMENTO ---> Nome de espécie já consta na base de dados
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION inserir_porte(text, double precision, double precision);
# TESTADA
def inserir_porte(_nome: str, _peso_min: float, _peso_max: float):
    """
    CREATE OR REPLACE FUNCTION inserir_porte(_nome TEXT, _peso_min FLOAT, _peso_max FLOAT) RETURNS INTEGER AS $$
    BEGIN
        IF LENGTH(_nome) < 3 THEN RAISE EXCEPTION '>> CANCELAMENTO ---> nome do porte muito curto';
        ELSEIF EXISTS(SELECT 1 FROM PORTE WHERE nome = _nome) THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> nome do porte já consta na base de dados';
        ELSEIF _peso_min <= 0 THEN RAISE EXCEPTION '>> CANCELAMENTO ---> peso mínimo não podem ser: nulo ou negativo';
        ELSEIF _peso_max <= 0 THEN RAISE EXCEPTION '>> CANCELAMENTO ---> peso máximo não podem ser: nulo ou negativo';
        ELSEIF _peso_max <= _peso_min THEN RAISE EXCEPTION '>> CANCELAMENTO ---> peso máximo não podem ser: menor/igual ao peso mínimo.';
        ELSEIF _nome IS NULL OR _peso_min IS NULL OR _peso_max IS NULL THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> valores de parâmetros nulos não são permitidos';
        ELSE
            INSERT INTO PORTE (nome, peso_min, peso_max) VALUES (_nome, _peso_min, _peso_max);
            RAISE NOTICE '>> CONFIRMAÇÃO ---> novo porte adicionado à base de dados';
        END IF;
    RETURN -2;
    END;
    $$ LANGUAGE plpgsql;
    """

    testes = """
    SELECT inserir_padrao('porte');                       # ERROR:  >> CANCELAMENTO ---> valores de parâmetros nulos não são permitidos
    SELECT inserir_padrao('porte', NULL);                 # ERROR:  >> CANCELAMENTO ---> valores de parâmetros nulos não são permitidos
    SELECT inserir_padrao('porte', 'Fa');                 # ERROR:  >> CANCELAMENTO ---> nome do porte muito curto
    SELECT inserir_padrao('porte', 'Fantasma');           # ERROR:  >> CANCELAMENTO ---> valores de parâmetros nulos não são permitidos
    SELECT inserir_padrao('porte', 'Fantasma', '-1');     # ERROR:  >> CANCELAMENTO ---> peso mínimo não podem ser: nulo ou negativo
    SELECT inserir_padrao('porte', 'Fantasma', '0');      # ERROR:  >> CANCELAMENTO ---> peso mínimo não podem ser: nulo ou negativo
    SELECT inserir_padrao('porte', 'Fantasma', '100.1');  # ERROR:  >> CANCELAMENTO ---> valores de parâmetros nulos não são permitidos
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION inserir_raca(integer, integer, text);
# TESTADA
def inserir_raca(_cod_esp: int, _cod_pt: int, _nome: str):
    """
    CREATE OR REPLACE FUNCTION inserir_raca(_cod_esp INT, _cod_pt INT, _nome TEXT) RETURNS INTEGER AS $$
    BEGIN
        IF LENGTH(_nome) < 3 THEN RAISE EXCEPTION '>> CANCELAMENTO ---> nome de raça muito curto'; 
        ELSEIF EXISTS(SELECT 1 FROM RACA WHERE nome = _nome) THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> nome de raça já consta na base de dados';
        ELSEIF NOT EXISTS(SELECT 1 FROM ESPECIE WHERE cod_esp = _cod_esp) THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> chave de consulta do código de espécie não consta na base de dados';
        ELSEIF NOT EXISTS(SELECT 1 FROM PORTE WHERE cod_pt = _cod_pt) THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ===== Chave de consulta do código do porte não consta na base de dados';
        ELSEIF _cod_esp IS NULL OR _cod_pt IS NULL OR _nome IS NULL THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> valores de parâmetros nulos não são permitidos';
        ELSE
            INSERT INTO RACA (cod_esp_fk, cod_pt_fk, nome) VALUES (_cod_esp, _cod_pt, _nome);
            RAISE NOTICE '>> CONFIRMAÇÃO ---> nova raça adicionada à base de dados';
        END IF;
        RETURN -3;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION inserir_tutor(text, text, text, text)
# TESTADA
def inserir_tutor(_cpf: str, _nome: str, _email: str, _telefone: str):
    """
    CREATE OR REPLACE FUNCTION inserir_tutor(
        _cpf TEXT, _nome TEXT, _email TEXT, _telefone TEXT
    ) RETURNS INTEGER AS $$
    BEGIN
    IF _cpf IS NULL THEN RAISE EXCEPTION '>> CANCELAMENTO --> cpf não pode ser um campo nulo';
    ELSEIF LENGTH(_cpf) != 11 THEN RAISE EXCEPTION '>> CANCELAMENTO --> cpf deve possuir 11 dígitos numéricos';
    ELSEIF NOT eh_numero(_cpf) THEN RAISE EXCEPTION '>> CANCELAMENTO --> cpf deve conter apenas números';
    ELSEIF _nome IS NULL THEN RAISE EXCEPTION '>> CANCELAMENTO --> nome não pode ser um campo nulo';
    ELSEIF LENGTH(_nome) < 3 THEN RAISE EXCEPTION '>> CANCELAMENTO --> nome do tutor é muito curto';
    ELSEIF _email IS NULL THEN RAISE EXCEPTION '>> CANCELAMENTO --> email não pode ser um campo nulo';
    ELSEIF NOT validar_email_basico(_email) THEN RAISE EXCEPTION '>> CANCELAMENTO --> email de formato inválido';
    ELSEIF _telefone IS NULL THEN RAISE EXCEPTION '>> CANCELAMENTO --> telefone não pode ser um campo nulo';
    ELSEIF LENGTH(_telefone) != 11 THEN RAISE EXCEPTION '>> CANCELAMENTO --> telefone deve possuir 11 dígitos numéricos';
    ELSEIF NOT eh_numero(_telefone) THEN RAISE EXCEPTION '>> CANCELAMENTO --> telefone deve conter apenas números';
    ELSE 
        INSERT INTO TUTOR (cpf, nome, email, telefone) VALUES (_cpf, _nome, _email, _telefone);
        RAISE INFO '>> CONFIRMAÇÃO --> Novo tutor adicionado à base de dados';
    END IF;
    RETURN -4;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION inserir_tutor(int, int, text, text, date)
# TESTADA
# Usa funções externas: [validar_data]
def inserir_pet(_cod_raca: int, _cod_tutor: int, _nome: str, _sexo: str, _dt_cadastro: datetime):
    """
    CREATE OR REPLACE FUNCTION inserir_pet(
        _cod_raca_fk INT, _cod_tutor_fk INT, _nome TEXT, _sexo TEXT, _dt_cadastro DATE
    ) RETURNS INTEGER AS $$
    DECLARE
    _data_correta DATE;
    BEGIN
    -- _cod_raca_fk: int, _cod_tutor_fk: int, _nome: str, _sexo: str, _dt_cadastro: str
    IF NOT EXISTS(SELECT 1 FROM RACA WHERE cod_raca = _cod_raca_fk) THEN RAISE EXCEPTION
    '>> CANCELAMENTO ---> chave de consulta do código de raça não consta na base de dados';
    ELSEIF NOT EXISTS(SELECT 1 FROM TUTOR WHERE cod_tutor = _cod_tutor_fk) THEN RAISE EXCEPTION
    '>> CANCELAMENTO ---> chave de consulta do código do tutor não consta na base de dados';
    ELSEIF LENGTH(_nome) < 3 THEN RAISE EXCEPTION '>> CANCELAMENTO ---> nome de pet é muito curto';
    ELSEIF UPPER(_sexo) NOT IN ('M', 'F') THEN RAISE EXCEPTION '>> CANCELAMENTO ---> sexo do pet só macho ou fêmea';
    ELSEIF EXTRACT(DOW FROM _dt_cadastro) <= 0 OR EXTRACT(DOW FROM _dt_cadastro) > 5 THEN RAISE EXCEPTION
    '>> CANCELAMENTO ---> data do cadastro não é dia útil';
    END IF;
    
    _data_correta := validar_data(_dt_cadastro);
    IF NOT _dt_cadastro <= CURRENT_DATE THEN RAISE EXCEPTION '>> CANCELAMENTO ---> data de cadastro no futuro não existe';
    END IF;
    INSERT INTO PET (cod_raca_fk, cod_tutor_fk, nome, sexo, dt_cadastro) VALUES (_cod_raca_fk, _cod_tutor_fk, _nome, _sexo, _dt_cadastro);
    RAISE INFO '>> CONFIRMAÇÃO ---> Novo pet adicionado à base de dados';
    RETURN -5;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################
