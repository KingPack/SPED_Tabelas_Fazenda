import json
import requests

from unidecode import unidecode


url_requests = open('./seila.json', 'r')

linha = url_requests.readlines()


print(linha)

def find_algo(pacote, tabela):

    for pack in url_requests["Pacote"]:

        if pack == pacote:

            for table in url_requests["Pacote"][pacote]:

                if table == tabela:
                    url = url_requests["Pacote"][pacote][tabela]
                    table_request(url)
                    break

                else:
                    print("essa tabela nao")

            break

        else:
            print('Num tenho')



    return "ok"

def table_request(url):

    req_table = requests.get(url)

    valores = req_table.content
    dados_decodificados = valores.decode("unicode_escape")
    dados_sem_acento = unidecode(dados_decodificados)
    dados_identados = dados_sem_acento.split('\r\n')

    quantidade_linhas_maxima = len(dados_identados)-1

    lista = []

    for linha in dados_identados[1:quantidade_linhas_maxima]:
        
        linha = linha.split('|')

        dia_inicio = linha[2][0:2]
        mes_inicio = linha[2][2:4]
        ano_inicio = linha[2][4:8]
            
        data_inicio = f'{dia_inicio}/{mes_inicio}/{ano_inicio}'

        if not linha[3]:
            data_fim = None

        else:
            dia_fim = linha[3][0:2]
            mes_fim = linha[3][2:4]
            ano_fim = linha[3][4:8]

            data_fim = f'{dia_fim}/{mes_fim}/{ano_fim}'


        dados_linha = {"Codigo":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas de Classes de Consumo',
            'Tabela':'4.4.1- Tabela Classificacao de Itens de Energia Eletrica, Servicos de Comunicacao e Telecomunicacao',
            'Versao': dados_identados[0][7:8],
            'Link_arquivo': url,
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )


    return json_dados






pacote = "Tabelas Genericas - ICMS"
tabela = "Tabela de Códigos de Receita - GNRE"

# find_algo(pacote, tabela)