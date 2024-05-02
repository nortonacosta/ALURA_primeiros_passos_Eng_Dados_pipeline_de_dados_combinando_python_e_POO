import csv
import json


class Dados:

    def __init__(self, dados):
        self.dados = dados
        self.nome_colunas = self.__obter_colunas()
        self.quantidade_linhas = self.__tamanho_dados_()

    #Leitura dos dados

    def __leitura_json(caminho):
        dados_json = []
        with open(caminho, 'r') as arquivo:
            dados_json = json.load(arquivo)
        return dados_json

    def __leitura_csv(caminho):
        dados_csv = []
        with open(caminho, 'r') as arquivo:
            spamreader = csv.DictReader(arquivo, delimiter=',')
            #spamreader é um nome padrao da varável de acordo com a documentação
            #O metodo reader do csv exige dois parametros(file e um demiliter) que separa os dados com (, ; ou |)
            for linha in spamreader:
                dados_csv.append(linha)

        return dados_csv        

    @classmethod
    def leitura_dados(cls, caminho, tipo_dados):
        dados = []
        if tipo_dados == 'csv':
            dados = cls.__leitura_csv(caminho)    
        elif tipo_dados == 'json':
            dados = cls.__leitura_json(caminho)
          
        return cls(dados)

    #Leitura das colunas e renomeando

    def __obter_colunas(self):
        return list(self.dados[-1].keys())
    
    def renomear_colunas(self, key_mapping):
        novos_dados = []

        for dicionario_antigo in self.dados:
            dicionario_temporario = {}
            for chave_antiga, valor in dicionario_antigo.items():
                dicionario_temporario[key_mapping[chave_antiga]] = valor
            novos_dados.append(dicionario_temporario)
        
        self.dados =  novos_dados
        self.nome_colunas = self.__obter_colunas()

    # quantodade de dados
    def __tamanho_dados_(self):
        return len(self.dados)
    
    #Juntando dados das empresas A e B
    def juntando_dados_EmpresaA_EmpresaB(dadosA, dadosB):    
        lista_combinada = []
        
        lista_combinada.extend(dadosA.dados)
        lista_combinada.extend(dadosB.dados)
        return Dados(lista_combinada)
    
    #Carregamento dos dados
    def __transformando_dados_tabela_(self):
    
        dados_combinados_tabela = [self.nome_colunas]

        for linha in self.dados:
            linha_nova = []
            for coluna in self.nome_colunas:
                linha_nova.append(linha.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha_nova)
        
        return dados_combinados_tabela
    
    #Salvando dados    
    def salvando_dados(self, caminho):

        dados_combinados_tabela = self.__transformando_dados_tabela_()

        with open(caminho, 'w') as arquivo:
            escrever = csv.writer(arquivo)
            escrever.writerows(dados_combinados_tabela)

    
