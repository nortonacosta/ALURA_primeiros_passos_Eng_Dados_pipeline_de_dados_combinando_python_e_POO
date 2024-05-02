from processamento_dados import Dados


caminho_json = 'data_raw/dados_empresaA.json'
caminho_csv = 'data_raw/dados_empresaB.csv'

#===========================================================
#Extract
#Lendos as colunas
print('========= Lendo Dados da Coluna: =========\n')
dados_empresaA = Dados.leitura_dados(caminho_json, 'json')
print(f'Dados coluna Json: {dados_empresaA.nome_colunas}')
dados_empresaB = Dados.leitura_dados(caminho_csv, 'csv')
print(f'Dados colunas csv {dados_empresaB.nome_colunas}')
print('===========================================\n')
#===========================================================

#===========================================================
#Transform
#transformando novas colunas
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

print('========= transformando novas colunas =========')
dados_empresaB.renomear_colunas(key_mapping)
print(dados_empresaB.nome_colunas)
print('===========================================\n')

print('========= Quantidade de linha das colunas =========')
print(f'Quantidade de linhas Empresa A: {dados_empresaA.quantidade_linhas}')
print(f'Quantidade de linhas Empresa B: {dados_empresaB.quantidade_linhas}')
print('===========================================\n')

print('========= Fusão do dados das empresas A e B =========')
dados_fusão = Dados.juntando_dados_EmpresaA_EmpresaB(dados_empresaA, dados_empresaB)
print(f'Dados das colunas após a fusão: {dados_fusão.nome_colunas}')
print(f'Quantidade de linhas após fusão:  {dados_fusão.quantidade_linhas}')
print('===========================================\n')
#===========================================================

#===========================================================
#Load
print('========= salvando dados =========')
caminho_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusão.salvando_dados(caminho_dados_combinados)
print(caminho_dados_combinados)
#===========================================================