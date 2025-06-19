

def sintaxe_comum_funcao():
    """
    CREATE OR REPLACE FUNCTION _()
    RETURNS VOID AS $$ 
    BEGIN
        IF THEN RAISE EXCEPTION '';
        ELSE
        INSERT INTO _ () VALUES ();
        UPDATE _ SET _ = _ WHERE _ = _;
        DELETE FROM _ WHERE _ = _;
        END IF;
        RAISE INFO '>> CONFIRMAÇÃO ---> ';
    END;
    $$ LANGUAGE plpgsql;
    """

def remover_funcao():
    """
    --o Sem parâmetro
    DROP FUNCTION IF EXISTS nome_da_funcao();

    --o Com parâmetro
    DROP FUNCTION IF EXISTS nome_da_funcao(par1, par2);

    --o Exemplo
    DROP FUNCTION IF EXISTS nome_da_funcao(text, integer, double_precision);
    """

def renomear_funcao():
    """
    ALTER FUNCTION nome_atual() RENAME TO novo_nome;
    """
