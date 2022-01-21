import json
import requests
from unidecode import unidecode



def request_tabela_enquadramento_ipi():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=4&idTabela=20')

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
            'Pacote':'Tabelas do IPI',
            'Tabela':'4.5.1- Tabela de Codigos da Classe de Enquadramento do IPI',
            'Versao': dados_identados[0][7:10],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=4&idTabela=20',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('enquadramento_IPI.json', 'w') as f:
        f.write(json_dados)


def request_tabela_selo_controle():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=4&idTabela=22')

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
            'Pacote':'Tabelas do IPI',
            'Tabela':'4.5.2- Tabela de Codigo de Selo de Controle',
            'Versao': dados_identados[0][7:10],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=4&idTabela=22',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4, 
        )

    with open('Selo_controle.json', 'w') as f:
        f.write(json_dados)


def request_tabela_apuracao_ipi():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=4&idTabela=19')

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
            'Pacote':'Tabelas do IPI',
            'Tabela':'4.5.4 - Tabela Codigo de Ajuste da Apuracao do IPI',
            'Versao': dados_identados[0][7:10],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=4&idTabela=19',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4, 
        )

    with open('Apuracao_IPI.json', 'w') as f:
        f.write(json_dados)


def request_tabela_contribuintes_ipi():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=4&idTabela=1171')

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


        dados_linha = {"Atividade":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas do IPI',
            'Tabela':'4.5.5 - Classificacao de Contribuintes do IPI',
            'Versao': dados_identados[0][7:8],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=4&idTabela=1171',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4, 
        )

    with open('Contribuintes_IPI.json', 'w') as f:
        f.write(json_dados)


