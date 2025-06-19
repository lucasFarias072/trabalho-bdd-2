

def consultaA():
    """
    --o A clínica que presta todos os serviços de clínica
    
    SELECT cli.nome FROM CLINICA cli
    JOIN CLI_FUNCAO cl ON cl.cod_cli_fk = cli.cod_cli
    JOIN CLI_SERV cs ON cs.cod_cli_serv = cl.cod_cli_serv_fk
    GROUP BY cli.nome
    HAVING COUNT(DISTINCT cs.cod_cli_serv) = (SELECT COUNT(DISTINCT cod_cli_serv) FROM CLI_SERV);
    """

# Conversível em função
def consultaB():
    """
    --o Serviços prestados por clínica
    
    SELECT cs.cod_cli_serv, cs.nome FROM CLI_SERV cs
    JOIN CLI_FUNCAO cf ON cf.cod_cli_serv_fk = cs.cod_cli_serv
    JOIN CLINICA cli ON cli.cod_cli = cf.cod_cli_fk
    WHERE cli.nome = 'Prata';
    """

def consultaC():
    """
    --o Serviços registrados pela médica Velma
    
    SELECT vs.nome FROM VET_SERV vs
    JOIN VET_FUNCAO vf ON vf.cod_vet_serv_fk = vs.cod_vet_serv
    WHERE vf.cod_vet_funcao IN(
    SELECT va.cod_vet_funcao_fk FROM VET_ATEND va
    JOIN VET_FUNCAO vf ON vf.cod_vet_funcao = va.cod_vet_funcao_fk
    JOIN VETERINARIO vet ON vet.crmv = vf.crmv_fk
    WHERE vet.nome = 'Velma')
    """

def consultaD():
    """
    --o Médicos que trabalham na clínica Ouro
    
    SELECT vet.nome FROM VETERINARIO vet
    JOIN CLINICA cli ON cli.cod_cli = vet.cod_cli_fk
    WHERE cli.nome = 'Bronze';
    """
