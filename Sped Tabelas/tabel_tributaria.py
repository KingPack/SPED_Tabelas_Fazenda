import json
import requests
from unidecode import unidecode


def request_tabela_situacao_tributaria_icms():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=5&idTabela=130')

    valores = r.content
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
            data_fim = False

        else:
            dia_fim = linha[3][0:2]
            mes_fim = linha[3][2:4]
            ano_fim = linha[3][4:8]

            data_fim = f'{dia_fim}/{mes_fim}/{ano_fim}'


        dados_linha = {"Codigo":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas de Situacao Tributaria',
            'Tabela':'Tabela Codigo da Situacao Tributaria - CST (ICMS)',
            'Versao': dados_identados[0][7:8],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=5&idTabela=130',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4, 
        )

    with open('Situacao_Tributaria_ICMS.json', 'w') as f:
        f.write(json_dados)


def request_tabela_situacao_tributaria_cofins():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=5&idTabela=23')

    valores = r.content
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
            data_fim = False

        else:
            dia_fim = linha[3][0:2]
            mes_fim = linha[3][2:4]
            ano_fim = linha[3][4:8]

            data_fim = f'{dia_fim}/{mes_fim}/{ano_fim}'


        dados_linha = {"Codigo":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas de Situacao Tributaria',
            'Tabela':':Tabela Codigo de Situacao Tributaria da COFINS',
            'Versao': dados_identados[0][7:10],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=5&idTabela=23',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4, 
        )

    with open('Situacao_Tributaria_COFINS.json', 'w') as f:
        f.write(json_dados)


def request_tabela_situacao_tributaria_pis():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=5&idTabela=27')

    valores = r.content
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
            data_fim = False

        else:
            dia_fim = linha[3][0:2]
            mes_fim = linha[3][2:4]
            ano_fim = linha[3][4:8]

            data_fim = f'{dia_fim}/{mes_fim}/{ano_fim}'


        dados_linha = {"Codigo":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas de Situacao Tributaria',
            'Tabela':':Tabela Codigo de Situacao Tributaria do PIS',
            'Versao': dados_identados[0][7:10],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=5&idTabela=27',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4, 
        )

    with open('Situacao_Tributaria_PIS.json', 'w') as f:
        f.write(json_dados)


def request_tabela_situacao_tributaria_cst_ipi():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=5&idTabela=26')

    valores = r.content
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
            data_fim = False

        else:
            dia_fim = linha[3][0:2]
            mes_fim = linha[3][2:4]
            ano_fim = linha[3][4:8]

            data_fim = f'{dia_fim}/{mes_fim}/{ano_fim}'


        dados_linha = {"Codigo":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas de Situacao Tributaria',
            'Tabela':':Tabela Codigo de Tributacao IPI - CST_IPI',
            'Versao': dados_identados[0][7:10],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=5&idTabela=26',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4, 
        )

    with open('Situacao_Tributaria_CST_IPI.json', 'w') as f:
        f.write(json_dados)

