nome = """
Título: LB NATAL 2022 12 50
Produto: VT LB NATAL 2022 12 50
Anunciante: LE BISCUIT
CNPJ do Anunciante: 16.233.389/0006-60
Agência: ARTPLAN COMUNICACAO SA
CNPJ da Agência: 33.673.286/0009-82
Duração: 15”
CRT: 2022034137012-6
Produtora: LAMPARINA ANIMAÇÃO E PRODUÇÃO DE VÍDEOS LTDA
CNPJ da Produtora: 15.667.476/0001-58
Direção: Adriano Fontes Passos
Ano de Produção: 2022
Data: 06/12/2022
"""

#print(nome.index(':'))

#titulo = nome[0:7]  
#print(nome - titulo)

linhas = nome.split('\n')

for palavras in linhas:
    if ':' in linhas:
        print(linhas - ':')