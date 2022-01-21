import json
import requests
from unidecode import unidecode




def request_tabela_situacao_tributaria_icms():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=3&idTabela=17')

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
            'Pacote':'Tabelas de Caracteristicas dos Documentos',
            'Tabela':'Tabela Documentos Fiscais do ICMS',
            'Versao': dados_identados[0][7:8],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=3&idTabela=17',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4, 
        )

    with open('Fiscal_ICMS.json', 'w') as f:
        f.write(json_dados)


def request_tabela_situacao_emitente():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=3&idTabela=16')

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
            'Pacote':'Tabelas de Caracteristicas dos Documentos',
            'Tabela':'Tabela de Indicador de Emitente',
            'Versao': dados_identados[0][7:10],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=3&idTabela=16',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4, 
        )

    with open('Emitente.json', 'w') as f:
        f.write(json_dados)




def request_tabela_situacao_documento():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=3&idTabela=18')

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
            'Pacote':'Tabelas de Caracteristicas dos Documentos',
            'Tabela':'4.1.2- Tabela Situacao do Documento',
            'Versao': dados_identados[0][7:8],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=3&idTabela=18',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4, 
        )

    with open('Situacao_documento.json', 'w') as f:
        f.write(json_dados)


