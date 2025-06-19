

# Tabelas adicionadas até o momento: [RACA, TUTOR, PET]
# Função usada em funções: INSERT, UPDATE 
# AND chave_fk IS NOT NULL: quando for passado NULL como parâmetro, essa função ignora e deixa o NULL passar
def consultar_fk():
    """
    CREATE OR REPLACE FUNCTION consultar_fk(chave_fk INT, tabela TEXT) RETURNS BOOLEAN AS $$
    BEGIN
        IF tabela = 'raca' THEN
            IF NOT EXISTS(SELECT 1 FROM RACA WHERE cod_raca = chave_fk) AND chave_fk IS NOT NULL THEN RAISE EXCEPTION
            '>> CANCELAMENTO ---> chave de consulta do código de raça não consta na base de dados'; END IF;
        ELSEIF tabela = 'tutor' THEN
            IF NOT EXISTS(SELECT 1 FROM TUTOR WHERE cod_tutor = chave_fk) AND chave_fk IS NOT NULL THEN RAISE EXCEPTION
            '>> CANCELAMENTO ---> chave de consulta do código do tutor não consta na base de dados'; END IF;
        ELSEIF tabela = 'pet' THEN
            IF NOT EXISTS(SELECT 1 FROM PET WHERE cod_pet = chave_fk) AND chave_fk IS NOT NULL THEN RAISE EXCEPTION
            '>> CANCELAMENTO ---> chave de consulta do código do pet não consta na base de dados'; END IF;
        END IF;
    RETURN TRUE;
    END;
    $$ LANGUAGE plpgsql;
    """

def eh_numero():
    """
    CREATE OR REPLACE FUNCTION eh_numero(texto TEXT)
    RETURNS BOOLEAN AS $$
    BEGIN
        PERFORM texto::NUMERIC;
        RETURN TRUE;
    EXCEPTION WHEN invalid_text_representation THEN
        RETURN FALSE;
    END;
    $$ LANGUAGE plpgsql;
    """

def gerar_data():
    """
    CREATE OR REPLACE FUNCTION gerar_data() RETURNS DATE AS $$
    DECLARE ano INT; mes INT; dia INT; data_criada DATE; dia_semana_int INT; eh_dia_util BOOLEAN;
    BEGIN
    ano := EXTRACT(YEAR FROM CURRENT_DATE) - FLOOR(RANDOM() * 2 + 1) + FLOOR(RANDOM() * 2);
    mes := FLOOR(RANDOM() * 12 + 1);
    IF mes = 2 THEN dia := FLOOR(RANDOM() * 26 + 1);
    ELSE dia := FLOOR(RANDOM() * 30 + 1);
    END IF;
    data_criada := (ano || '-' || mes || '-' || dia)::DATE AS data_mock;
    IF data_criada > CURRENT_DATE THEN data_criada := CURRENT_DATE; END IF;

    --o Essa parte é para tratar não enviar datas que não são dias úteis: envia uma data genérica que é dia útil
    --o Isso se dá pelas regras do modelo, que aceita consultas entre segunda à sexta
    dia_semana_int := EXTRACT(DOW FROM data_criada);
    eh_dia_util := dia_semana_int > 0 AND dia_semana_int <= 5;
    IF NOT eh_dia_util THEN
    data_criada := '2025-06-10';
    END IF;
    RETURN data_criada;
    END;
    $$ LANGUAGE plpgsql;
    """

def gerar_hora():
    """
    CREATE OR REPLACE FUNCTION gerar_hora() RETURNS TIME AS $$
    DECLARE h INT; minuto INT; seg INT; hora_criada TEXT; chance_zero_min BOOLEAN; chance_zero_seg BOOLEAN;
    BEGIN
        h := FLOOR(RANDOM() * 17 + 1);
        minuto := FLOOR(RANDOM() * 59 + 1);
        seg := FLOOR(RANDOM() * 59 + 1);
        chance_zero_min := minuto < seg;
        chance_zero_seg := (minuto - seg) < h;
        IF chance_zero_min THEN minuto := 0; ELSE minuto := minuto; END IF;
        IF chance_zero_seg THEN seg := 0; ELSE seg = seg; END IF;
        IF h < 8 THEN h := h + (8 - h);
        END IF;
        RETURN (h || ':' || minuto::TEXT || ':' || seg::TEXT);
    END;
    $$ LANGUAGE plpgsql;
    """

# EXEMPLO ---> get_dia_semana(EXTRACT(DOW FROM cat.dt_atend)) 
# EXEMPLO ---> get_dia_semana(EXTRACT(DOW FROM '2025-06-19 00:00:00'))
def get_dia_semana():
    """
    CREATE OR REPLACE FUNCTION get_dia_semana(dia NUMERIC) RETURNS TEXT AS $$
    DECLARE dia_semana TEXT;
    BEGIN
    IF dia = 0 THEN RETURN 'Domingo';
    ELSEIF dia = 1 THEN dia_semana := 'Segunda-feira';
    ELSEIF dia = 2 THEN dia_semana := 'Terça-feira';
    ELSEIF dia = 3 THEN dia_semana := 'Quarta-feira';
    ELSEIF dia = 4 THEN dia_semana := 'Quinta-feira';
    ELSEIF dia = 5 THEN dia_semana := 'Sexta-feira';
    ELSE dia_semana := 'Sábado';
    END IF;
    RETURN dia_semana;
    END;
    $$ LANGUAGE plpgsql;
    """

def validar_data():
    """
    CREATE OR REPLACE FUNCTION validar_data(_data DATE) RETURNS DATE AS $$
    BEGIN
        RETURN _data::DATE;
    EXCEPTION 
        WHEN invalid_datetime_format THEN
            RAISE EXCEPTION '>> CANCELAMENTO ---> Data de cadastro com formato incorreto. O correto é YYYY-MM-DD';
        WHEN datetime_field_overflow THEN
            RAISE EXCEPTION '>> CANCELAMENTO ---> Data de cadastro inválida. O correto é YYYY-MM-DD';
    END;
    $$ LANGUAGE plpgsql;
    """

def validar_email_basico():
    """
    CREATE OR REPLACE FUNCTION validar_email_basico(email TEXT)
    RETURNS BOOLEAN AS $$
    BEGIN
        -- Validação muito básica: tem @ e ponto depois do @
        RETURN email ~* '^[^@]+@[^@]+\.[^@]+$';
    END;
    $$ LANGUAGE plpgsql;
    """

def ver_se_texto_curto():
    """
    CREATE OR REPLACE FUNCTION ver_se_texto_curto(texto TEXT, rotulo TEXT) RETURNS BOOLEAN AS $$
    BEGIN
    IF LENGTH(texto) < 3 THEN RAISE EXCEPTION '>> CANCELAMENTO ---> % é muito curto', rotulo; END IF;
    RETURN TRUE;
    END;
    $$ LANGUAGE plpgsql;
    """
