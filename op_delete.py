

def logica_funcoes_deletar():
    """
    * Esperam somente a chave primária na tabela
    * O processo de remoção não acontece em cascata 
    * Ao invés disso, as chaves estrangeiras recebem um "SET NULL" na criação das tabelas
    * Acontecem eventos diferentes para chaves PK e FK
    * Ao remover uma linha que é uma chave PK, essa linha é removida e os dependentes ficam com NULL
    * Ao remover uma linha que é uma chave FK, essa linha é removida sem afetar a tabela da chave PK
    * Exemplo: ESPECIE e RACA (chave PK de ESPECIE vai como FK para RACA)
    * Se eu deleto de ESPECIE: linha é removida da tabela ESPECIE | linha relacionada de RACA ficam com FK nulo   
    * Se eu deleto de RACA:    linha é removida da tabela RACA    | linha relacionada de ESPECIE continua lá   
    """

def delete_modelo():
    """
    CREATE OR REPLACE FUNCTION remover_() RETURNS INTEGER AS $$
    BEGIN
        IF NOT EXISTS(SELECT 1 FROM  WHERE cod_ = _cod_) THEN RAISE EXCEPTION
        '>> CANCELAMENTO ---> chave de consulta do código de ... não consta na base de dados';
        ELSE
        RAISE INFO '>> CONFIRMAÇÃO ---> Novo ... adicionado à base de dados';
        END IF;
        RAISE INFO '>> CONFIRMAÇÃO ---> Remoção da ... efetuada com sucesso';
        RETURN
    END;
    $$ LANGUAGE plpgsql;
    """

# Por enquanto, com as 5 primeiras tabelas
def remover_padrao():
    """
    CREATE OR REPLACE FUNCTION remover_padrao(nomeTabela TEXT, chave_pk INT ) RETURNS INTEGER AS $$
    DECLARE 
    procedimento INTEGER;
    BEGIN
    CASE LOWER(nomeTabela)
        WHEN 'especie' THEN procedimento := remover_especie(chave_pk);
        WHEN 'porte' THEN procedimento := remover_porte(chave_pk);
        WHEN 'raca' THEN procedimento := remover_raca(chave_pk);
        WHEN 'tutor' THEN procedimento := remover_tutor(chave_pk);
        WHEN 'pet' THEN procedimento := remover_pet(chave_pk);
        ELSE RAISE EXCEPTION 'Tabela % não consta nesse modelo de negócios.', nomeTabela;
    END CASE;
    RETURN procedimento;
    END;
    $$ LANGUAGE plpgsql;
    """



###################################################################################################
# DROP FUNCTION remover_especie(int)
# Afeta linhas em RACA
# TESTADA
def remover_especie():
    """
    CREATE OR REPLACE FUNCTION remover_especie(_cod_esp INT) RETURNS INTEGER AS $$
    BEGIN
    IF NOT EXISTS(SELECT 1 FROM ESPECIE WHERE cod_esp = _cod_esp) THEN RAISE EXCEPTION 
    '>> CANCELAMENTO ---> chave de consulta do código de espécie não consta na base de dados';
    ELSE
        DELETE FROM ESPECIE WHERE cod_esp = _cod_esp;
        RAISE NOTICE '>> CONFIRMAÇÃO ---> Remoção da espécie efetuada com sucesso';
    END IF;
    RETURN 100;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION remover_porte(int)
# Afeta linhas em RACA
# TESTADA
def remover_porte(cod_pt_val: int):
    """
    CREATE OR REPLACE FUNCTION remover_porte(_cod_pt INT) RETURNS INTEGER AS $$
    BEGIN
        IF NOT EXISTS(SELECT 1 FROM PORTE WHERE cod_pt = _cod_pt) THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> chave de consulta do código do porte não consta na base de dados';
        ELSE
        DELETE FROM PORTE WHERE cod_pt = _cod_pt;
        RAISE NOTICE '>> CONFIRMAÇÃO ===== Remoção do porte efetuada com sucesso';
    END IF;
    RETURN 200;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION remover_raca(int)
# Afeta linhas em PET
# TESTADA
def remover_raca(cod_raca_val: int):
    """
    CREATE OR REPLACE FUNCTION remover_raca(_cod_raca INT) RETURNS INTEGER AS $$
    BEGIN
        IF NOT EXISTS(SELECT 1 FROM RACA WHERE cod_raca = _cod_raca) THEN RAISE EXCEPTION 
        '>> CANCELAMENTO ---> chave de consulta do código da raça não consta na base de dados';
        ELSE
            DELETE FROM RACA WHERE cod_raca = _cod_raca;
            RAISE NOTICE '>> CONFIRMAÇÃO ---> Remoção da raça efetuada com sucesso';
        END IF;
    RETURN 300;
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION remover_tutor(int)
# Afeta linhas em PET
# TESTADA
def remover_tutor():
    """
    CREATE OR REPLACE FUNCTION remover_tutor(_cod_tutor INT) RETURNS INTEGER AS $$
    BEGIN
    IF NOT EXISTS(SELECT 1 FROM TUTOR WHERE cod_tutor = _cod_tutor) THEN
        RAISE EXCEPTION '>> CANCELAMENTO --> chave de consulta do código do tutor não consta na base de dados';
    ELSE
        DELETE FROM TUTOR WHERE cod_tutor = _cod_tutor;
        RAISE NOTICE '>> CONFIRMAÇÃO --> Remoção do tutor efetuada com sucesso';
    END IF;
    RETURN 400;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################



###################################################################################################
# DROP FUNCTION remover_pet(int)
# Afeta linhas em CLI_ATEND, VET_ATEND
# TESTADA
def remover_pet():
    """
    CREATE OR REPLACE FUNCTION remover_pet(_cod_pet INT) RETURNS INTEGER AS $$
    DECLARE
    cod_pet_existe BOOLEAN;
    BEGIN
        cod_pet_existe := consultar_fk(_cod_pet, 'pet');
        DELETE FROM PET WHERE cod_pet = _cod_pet;
        RAISE INFO '>> CONFIRMAÇÃO ---> Remoção do pet efetuada com sucesso';
        RETURN 500;
    END;
    $$ LANGUAGE plpgsql;
    """
###################################################################################################
