

def excessoes():
    """
    --o Para atributos nulos nas chamadas de funções de inserção
    RAISE EXCEPTION '===== CANCELAMENTO ===== Valores de parâmetros nulos não são permitidos';
    
    --o Para textos muito curtos
    RAISE EXCEPTION '===== CANCELAMENTO ===== Nome da/de/do muito curto.';

    --o Para sucesso na inserção
    RAISE NOTICE '===== SUCESSO ===== Novo/Nova adiciona/o à base de dados: %.', _;

    --o Para quando a nova instância já tiver algo idêntico na tabela
    RAISE EXCEPTION '===== CANCELAMENTO ===== Nome novo da/de/do já consta na base de dados.';
    """
