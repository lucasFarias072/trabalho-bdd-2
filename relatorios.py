

def modelo_inicial():
    """
    CREATE OR REPLACE FUNCTION ...() RETURNS TABLE() AS $$
    BEGIN
      SET search_path = public;
      RETURN QUERY
    END;
    $$ LANGUAGE plpgsql;
    """

def testes_tabela_cli_atend():
    """
    --o mudar 'int' p/ valores congruentes a suas linhas de tabela

    INSERT INTO CLI_ATEND(cod_cli_funcao_fk, cod_pet_fk, valor, dt_atend, avaliacao, status) 
    VALUES(2, 2, 65, '2025-06-11 08:11:00', 10, 'finalizado')
    
    UPDATE CLI_ATEND SET dt_atend = '2025-06-11 08:11:00' WHERE cod_cli_atend = int;
    
    DELETE FROM CLI_ATEND WHERE cod_cli_atend = int;
    """

###################################################################################################
# SELECT get_rank_lucro_por_clinica('Bronze', false);
# SELECT get_rank_lucro_por_clinica('', true);
def get_rank_lucro_por_clinica():
    """
    CREATE OR REPLACE FUNCTION get_rank_lucro_por_clinica(nome_clinica TEXT, ver_todas BOOLEAN) 
    RETURNS TABLE(nome VARCHAR(70), lucro_clinica FLOAT) AS $$
    BEGIN
      SET search_path = public;
      --o Bronze[260] [10, 11, 12] [10, 11, 12, 13, 14, 15, 16] (resultado bateu) 
      --o Ouro[150] [1, 2, 3, 4, 5] [1, 2, 3] (resultado bateu)
      --o Prata[225] [6, 7, 8, 9] [4, 5, 6, 7, 8, 9] (resultado bateu)
      --o Lucro das clínicas
      IF ver_todas THEN
      RETURN QUERY
      SELECT cli.nome, SUM(cat.valor) lucro_da_clinica FROM CLINICA cli
      JOIN CLI_FUNCAO cf ON cf.cod_cli_fk = cli.cod_cli
      JOIN CLI_ATEND cat ON cat.cod_cli_funcao_fk = cf.cod_cli_funcao
      GROUP BY cli.nome, cat.status
      HAVING cat.status = 'finalizado'
      ORDER BY lucro_da_clinica DESC;
      ELSE
      RETURN QUERY
      SELECT cli.nome, SUM(cat.valor) lucro_da_clinica FROM CLINICA cli
      JOIN CLI_FUNCAO cf ON cf.cod_cli_fk = cli.cod_cli
      JOIN CLI_ATEND cat ON cat.cod_cli_funcao_fk = cf.cod_cli_funcao
      GROUP BY cli.nome, cat.status
      HAVING cat.status = 'finalizado'
      AND cli.nome = nome_clinica;
      END IF;
    END;
    $$ LANGUAGE plpgsql;
    """

# Retirado
def lucros_por_clinica_view():
    """
    CREATE OR REPLACE VIEW view_lucro_clinicas AS SELECT nome, lucro_clinica FROM obter_lucro_clinica('', true);
    """

# Retirado
def lucros_por_clinica_funcao_trigger():
    """
    CREATE OR REPLACE FUNCTION monitorar_lucro_clinica() RETURNS TRIGGER AS $$
    BEGIN
      IF NEW.status != 'finalizado' THEN RAISE EXCEPTION 'cancelado';
      ELSE
        IF TG_OP = 'INSERT' THEN
          UPDATE view_lucro_clinicas
          SET lucro_clinica = lucro_clinica + NEW.valor
          WHERE nome IN(
          SELECT cli.nome FROM CLINICA cli
          JOIN CLI_FUNCAO cf ON cf.cod_cli_fk = cli.cod_cli
          JOIN CLI_ATEND cat ON cat.cod_cli_funcao_fk = cf.cod_cli_funcao
          WHERE cli.cod_cli IN (
            SELECT cs.cod_cli_serv FROM CLI_SERV cs
            JOIN CLI_FUNCAO cf ON cf.cod_cli_serv_fk = cs.cod_cli_serv
            JOIN CLI_ATEND cat ON cat.cod_cli_funcao_fk = cf.cod_cli_funcao
            WHERE cat.cod_cli_funcao_fk = NEW.cod_cli_funcao_fk 
          ) LIMIT 1);
        END IF;
      END IF;
      RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """

# Retirado
def lucros_por_clinica_trigger():
    """
    CREATE TRIGGER trigger_atualizar_lucros_clinica 
    BEFORE UPDATE OR INSERT OR DELETE ON CLI_ATEND
    FOR EACH ROW EXECUTE FUNCTION monitorar_lucro_clinica();
    """

# Implementado
def mv_rank_lucro_por_clinica():
    """
    CREATE MATERIALIZED VIEW mv_rank_lucro_por_clinica AS 
    SELECT nome, lucro_clinica FROM get_rank_lucro_por_clinica('', true);
    """

# Implementado
def atualizar_mv_rank_lucro_por_clinica():
    """
    CREATE OR REPLACE FUNCTION atualizar_mv_rank_lucro_por_clinica() RETURNS TRIGGER AS $$
    BEGIN
        IF NEW.status = 'finalizado' OR OLD.status = 'finalizado' THEN
            REFRESH MATERIALIZED VIEW mv_rank_lucro_por_clinica;
        END IF;
        
        RETURN COALESCE(NEW, OLD);
    END;
    $$ LANGUAGE plpgsql;
    """

# Implementado
def trigger_atualizar_mv_rank_lucro_por_clinica():
    """
    CREATE TRIGGER trigger_atualizar_mv_rank_lucro_por_clinica
    AFTER INSERT OR UPDATE OR DELETE ON CLI_ATEND
    FOR EACH ROW EXECUTE FUNCTION atualizar_mv_rank_lucro_por_clinica();
    """
###################################################################################################



###################################################################################################
def get_rank_qtd_atend_por_horario():
    """
    CREATE OR REPLACE FUNCTION get_rank_qtd_atend_por_horario() RETURNS TABLE(horario NUMERIC, qtd BIGINT) AS $$
    BEGIN
      SET search_path = public;
      RETURN QUERY
      SELECT EXTRACT(HOUR FROM dt_atend) horario, COUNT(EXTRACT(HOUR FROM dt_atend)) qtd_atendimentos FROM CLI_ATEND
      GROUP BY EXTRACT(HOUR FROM dt_atend)
      ORDER BY qtd_atendimentos DESC;
    END;
    $$ LANGUAGE plpgsql;
    """

def mv_rank_qtd_atend_por_horario():
    """
    CREATE MATERIALIZED VIEW mv_rank_qtd_atend_por_horario AS 
    SELECT horario, qtd FROM get_rank_qtd_atend_por_horario();
    """

# Não usado (ainda implementado)
def i_mv_rank_qtd_atend_por_horario():
    """
    CREATE INDEX i_mv_rank_qtd_atend_por_horario ON mv_rank_qtd_atend_por_horario(qtd DESC);
    """

def atualizar_mv_rank_qtd_atend_por_horario():
    """
    CREATE OR REPLACE FUNCTION atualizar_mv_rank_qtd_atend_por_horario() RETURNS TRIGGER AS $$
    BEGIN
        IF TG_OP = 'INSERT' OR TG_OP = 'DELETE' 
      OR 
        (TG_OP = 'UPDATE' AND OLD.dt_atend IS DISTINCT FROM NEW.dt_atend) THEN
            REFRESH MATERIALIZED VIEW mv_rank_qtd_atend_por_horario;
        END IF;
        
        RETURN COALESCE(NEW, OLD);
    END;
    $$ LANGUAGE plpgsql;
    """

def trigger_atualizar_mv_rank_qtd_atend_por_horario():
    """
    CREATE TRIGGER trigger_atualizar_mv_rank_qtd_atend_por_horario
    AFTER INSERT OR UPDATE OR DELETE ON CLI_ATEND
    FOR EACH ROW
    EXECUTE FUNCTION atualizar_mv_rank_qtd_atend_por_horario();
    """
###################################################################################################



###################################################################################################
def get_rank_qtd_atend_por_dia_semana():
    """
    CREATE OR REPLACE FUNCTION get_rank_qtd_atend_por_dia_semana() RETURNS TABLE(dia_semana TEXT, qtd BIGINT) AS $$
    BEGIN
      SET search_path = public;
      RETURN QUERY
      SELECT get_dia_semana(EXTRACT(DOW FROM cat.dt_atend)) dia_semana, COUNT(EXTRACT(DOW FROM cat.dt_atend)) qtd FROM CLI_ATEND cat
      GROUP BY dia_semana
      ORDER BY qtd DESC;
    END;
    $$ LANGUAGE plpgsql;
    """

def mv_rank_qtd_atend_por_dia_semana():
    """
    CREATE MATERIALIZED VIEW mv_rank_qtd_atend_por_horario AS 
    SELECT horario, qtd FROM get_rank_qtd_atend_por_horario();
    """

def atualizar_mv_rank_qtd_atend_por_dia_semana():
    """
    CREATE OR REPLACE FUNCTION atualizar_mv_rank_qtd_atend_por_dia_semana() RETURNS TRIGGER AS $$
    BEGIN
      IF TG_OP = 'INSERT' OR TG_OP = 'DELETE' 
        OR 
      (TG_OP = 'UPDATE' AND OLD.dt_atend IS DISTINCT FROM NEW.dt_atend) THEN
        REFRESH MATERIALIZED VIEW mv_rank_qtd_atend_por_dia_semana;
      END IF;

      RETURN COALESCE(NEW, OLD);
    END;
    $$ LANGUAGE plpgsql;
    """

def trigger_atualizar_mv_rank_qtd_atend_por_dia_semana():
    """
    CREATE TRIGGER trigger_atualizar_mv_rank_qtd_atend_por_dia_semana
    AFTER INSERT OR UPDATE OR DELETE ON CLI_ATEND
    FOR EACH ROW
    EXECUTE FUNCTION atualizar_mv_rank_qtd_atend_por_dia_semana();
    """
###################################################################################################
