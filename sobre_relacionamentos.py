

# Salto da tabela VET_FUNCAO com: VET_SERV, VET
def vet_funcao_PARA_vet_serv_E_veterinario():
    """
    SELECT vs.cod_vet_serv, vs.nome FROM VET_SERV vs
    JOIN VET_FUNCAO vf ON vf.cod_vet_serv_fk = vs.cod_vet_serv
    JOIN VETERINARIO vet ON vet.crmv = vf.crmv_fk
    """

# Salto da tabela CLI_FUNCAO com: CLI_SERV, CLINICA
def cli_funcao_PARA_cli_serv_E_clinica():
    """
    SELECT cs.nome FROM CLI_SERV cs
    JOIN CLI_FUNCAO cf ON cf.cod_cli_serv_fk = cs.cod_cli_serv
    JOIN CLINICA cli ON cli.cod_cli = cf.cod_cli_fk
    """
