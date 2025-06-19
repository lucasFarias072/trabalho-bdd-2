

def logica_funcoes_alterar():
    """
    * Parâmetros nulos ou omitidos são esperados
    * Se eu passo nulo, é por dois motivos:
        --o O parâmetro é no mínimo o segundo da função sendo usada
        --o Eu não quero alterar esse atributo
    * Criar uma intervenção com o COALESCE na sintaxe do UPDATE
    * O valor nulo é trocado pelo valor atual dentro do COALESCE
    """

def update_modelo():
    """
    CREATE OR REPLACE FUNCTION atualizar_() RETURNS INTEGER AS $$
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
def atualizar_padrao():
    """
    CREATE OR REPLACE FUNCTION atualizar_padrao(
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
        WHEN 'especie' THEN procedimento := atualizar_especie(campoA::INT, campoB::TEXT);
        WHEN 'porte' THEN procedimento := atualizar_porte(campoA::INT, campoB::TEXT, campoC::FLOAT, campoD::FLOAT);
        WHEN 'raca' THEN procedimento := atualizar_raca(campoA::INT, campoB::INT, campoC::INT, campoD::TEXT);
        WHEN 'tutor' THEN procedimento := atualizar_tutor(campoA::INT, campoB::TEXT, campoC::TEXT, campoD::TEXT, campoE::TEXT);
        WHEN 'pet' THEN procedimento := atualizar_pet(campoA::INT, campoB::INT, campoC::INT, campoD::TEXT, campoE::TEXT, campoF::DATE);
        ELSE RAISE EXCEPTION 'Tabela % não consta nesse modelo de negócios.', nomeTabela;
    END CASE;
    RETURN procedimento;
    END;
    $$ LANGUAGE plpgsql;
    """



###################################################################################################
# DROP FUNCTION atualizar_especie(int, text)
# TESTADO
def atualizar_especie():
    """
    CREATE OR REPLACE FUNCTION atualizar_especie(_cod_esp INT, _nome TEXT) RETURNS INTEGER AS $$
    BEGIN
        IF NOT EXISTS(SELECT 1 FROM ESPECIE WHERE cod_esp = _cod_esp) THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> chave de consulta da espécie não consta na base de dados';
        ELSEIF LENGTH(_nome) < 3 THEN RAISE EXCEPTION '>> CANCELAMENTO ---> nome atualizado da espécie é muito curto';
        ELSE
            UPDATE ESPECIE SET nome = COALESCE(_nome, nome) WHERE cod_esp = _cod_esp;
            RAISE NOTICE '>> CONFIRMAçÃO ---> Especie recebeu atualização';
        END IF;
    RETURN 1;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION atualizar_porte(int, text, double precision, double precision)
# TESTADO
def atualizar_porte():
    """
    CREATE OR REPLACE FUNCTION atualizar_porte(_cod_pt INT, _nome TEXT, _peso_min FLOAT, _peso_max FLOAT) RETURNS INTEGER AS $$
    BEGIN
        IF NOT EXISTS(SELECT 1 FROM PORTE WHERE cod_pt = _cod_pt) THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> chave de consulta do código do porte não consta na base de dados';
        ELSEIF EXISTS(SELECT 1 FROM PORTE WHERE nome = _nome) THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> nome de porte já consta na base de dados';
        ELSEIF LENGTH(_nome) < 3 THEN RAISE EXCEPTION '>> CANCELAMENTO ---> nome atualizado do porte é muito curto';
        ELSEIF _peso_min <= 0 THEN RAISE EXCEPTION '>> CANCELAMENTO ---> peso mínimo atualizado do porte não pode ser: negativo nem nulo';
        ELSEIF _peso_min >= _peso_max THEN RAISE EXCEPTION '>> CANCELAMENTO ---> peso mínimo atualizado do porte não pode ser: maior/igual ao peso máximo';
        ELSEIF EXISTS(SELECT 1 FROM PORTE WHERE peso_min = _peso_min) THEN RAISE EXCEPTION '>> CANCELAMENTO ---> peso mínimo não pode se repetir na base de dados';
        ELSEIF EXISTS(SELECT 1 FROM PORTE WHERE peso_max = _peso_max) THEN RAISE EXCEPTION '>> CANCELAMENTO ---> peso máximo não pode se repetir na base de dados';
        ELSE
            UPDATE PORTE 
            SET nome = COALESCE(_nome, nome), 
            peso_min = COALESCE(_peso_min, peso_min), 
            peso_max = COALESCE(_peso_max, peso_max) 
            WHERE cod_pt = _cod_pt;
            RAISE NOTICE '>> CONFIRMAÇÃO ---> Porte recebeu atualização';
        END IF;
    RETURN 2;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION atualizar_raca(int, int, int, text)
# TESTADO
def atualizar_raca():
    """
    CREATE OR REPLACE FUNCTION atualizar_raca(_cod_raca INT, _cod_esp INT, _cod_pt INT, _nome TEXT) RETURNS INTEGER AS $$
    BEGIN
        IF NOT EXISTS(SELECT 1 FROM RACA WHERE cod_raca = _cod_raca) THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> chave de consulta do código da raça não consta na base de dados';
        ELSEIF NOT EXISTS(SELECT 1 FROM ESPECIE WHERE cod_esp = _cod_esp) AND _cod_esp IS NOT NULL THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> código de espécie atualizado não existe na base de dados';
        ELSEIF NOT EXISTS(SELECT 1 FROM PORTE WHERE cod_pt = _cod_pt) AND _cod_pt IS NOT NULL THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> código de porte atualizado não existe na base de dados';
        ELSEIF LENGTH(_nome) < 3 THEN RAISE EXCEPTION '>> CANCELAMENTO ---> nome atualizado da raça é muito curto';
        ELSE
            UPDATE RACA 
            SET nome = COALESCE(_nome, nome), 
            cod_esp_fk = COALESCE(_cod_esp, cod_esp_fk),
            cod_pt_fk = COALESCE(_cod_pt, cod_pt_fk)
            WHERE cod_raca = _cod_raca;
            RAISE NOTICE '>> CONFIRMAÇÃO ---> RACA recebeu atualização';
    END IF;
    RETURN 3;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION atualizar_tutor(int, text, text, text, text)
# TESTADO
def atualizar_tutor():
    """
    CREATE OR REPLACE FUNCTION atualizar_tutor(
        _cod_tutor INT, _cpf TEXT, _nome TEXT, _email TEXT, _telefone TEXT
    ) RETURNS INTEGER AS $$
    BEGIN
    IF NOT EXISTS(SELECT 1 FROM TUTOR WHERE cod_tutor = _cod_tutor) THEN RAISE EXCEPTION
    '>> CANCELAMENTO --> chave de consulta do tutor não consta na base de dados';
    ELSEIF LENGTH(_cpf) != 11 THEN RAISE EXCEPTION '>> CANCELAMENTO --> cpf atualizado deve possuir 11 dígitos numéricos';
    ELSEIF NOT eh_numero(_cpf) THEN RAISE EXCEPTION '>> CANCELAMENTO --> cpf atualizado deve conter apenas números';
    ELSEIF LENGTH(_nome) < 3 THEN RAISE EXCEPTION '>> CANCELAMENTO --> nome do tutor atualizado é muito curto';
    ELSEIF NOT validar_email_basico(_email) THEN RAISE EXCEPTION '>> CANCELAMENTO --> email atualizado de formato inválido';
    ELSEIF LENGTH(_telefone) != 11 THEN RAISE EXCEPTION '>> CANCELAMENTO --> telefone atualizado deve possuir 11 dígitos numéricos';
    ELSEIF NOT eh_numero(_telefone) THEN RAISE EXCEPTION '>> CANCELAMENTO --> telefone atualizado deve conter apenas números';
    ELSE 
        UPDATE TUTOR 
        SET cpf = COALESCE(_cpf, cpf), nome = COALESCE(_nome, nome), email = COALESCE(_email, email), telefone = COALESCE(_telefone, telefone)
        WHERE cod_tutor = _cod_tutor;
        RAISE INFO '>> CONFIRMAÇÃO --> Tutor recebeu atualização';
    END IF;
    RETURN 4;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION atualizar_pet(int, int, int, text, text, date)
# TESTADO
# Usa funções externas: [consultar_fk, ver_se_texto_curto, validar_data]
def atualizar_pet():
    """
    CREATE OR REPLACE FUNCTION atualizar_pet(
	_cod_pet INT, _cod_raca INT, _cod_tutor INT, _nome TEXT, _sexo TEXT, _dt_cadastro DATE
    ) RETURNS INTEGER AS $$
    DECLARE
    cod_pet_existe BOOLEAN;
    cod_raca_existe BOOLEAN;
    cod_tutor_existe BOOLEAN;
    texto_eh_curto BOOLEAN;
    dt_cadastro_valida DATE;
    BEGIN
        cod_pet_existe := consultar_fk(_cod_pet, 'pet');
        cod_raca_existe := consultar_fk(_cod_raca, 'raca');
        cod_tutor_existe := consultar_fk(_cod_tutor, 'tutor');
        texto_eh_curto := ver_se_texto_curto(_nome, 'nome atualizado do pet');
        IF UPPER(_sexo) NOT IN ('M', 'F') THEN RAISE EXCEPTION '>> CANCELAMENTO ---> sexo do pet só macho ou fêmea'; 
        ELSEIF EXTRACT(DOW FROM _dt_cadastro) <= 0 OR EXTRACT(DOW FROM _dt_cadastro) > 5 THEN RAISE EXCEPTION
        '>> CANCELAMENTO ---> data do cadastro não é dia útil';
        END IF;
        dt_cadastro_valida := validar_data(_dt_cadastro);
        IF NOT _dt_cadastro <= CURRENT_DATE THEN RAISE EXCEPTION '>> CANCELAMENTO ---> data de cadastro no futuro não existe';
        END IF;
        
        UPDATE PET
        SET cod_raca_fk = COALESCE(_cod_raca, cod_raca_fk),
        cod_tutor_fk = COALESCE(_cod_tutor, cod_tutor_fk),
        nome = COALESCE(_nome, nome),
        sexo = COALESCE(_sexo, sexo),
        dt_cadastro = COALESCE(_dt_cadastro, dt_cadastro)
        WHERE cod_pet = _cod_pet;
        
        RAISE INFO '>> CONFIRMAÇÃO ---> Novo pet adicionado à base de dados';
        RETURN 5;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################
