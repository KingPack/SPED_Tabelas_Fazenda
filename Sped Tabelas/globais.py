import json
import requests
from unidecode import unidecode


def request_tabela_cest():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=996')

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


        dados_linha = {"Codigo_EST":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'CEST - Codigo Especificador da Substituicao Tributaria',
            'Versao': dados_identados[0][7:9],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=996',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('CEST.json', 'w') as f:
        f.write(json_dados)


def request_tabela_sped_fiscal():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=11')

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


        dados_linha = {"Codigo_leiaute":linha[0], 'versao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'3.1.1 - Tabel do Leiaute - Sped Fiscal',
            'Versao': dados_identados[0][7:9],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=11',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('sped_fiscal.json', 'w') as f:
        f.write(json_dados)


def request_tabela_reducao_z():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=8')

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


        dados_linha = {"Codigo_totalizador":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'4.4.6- Tabela de Codigos dos Totalizadores Parciais da REDUCAO Z',
            'Versao': dados_identados[0][7:10],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=8',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('reducao_z.json', 'w') as f:
        f.write(json_dados)


def request_tabela_icms():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=5')

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


        dados_linha = {"Codigo_obrigacao_recolher":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'5.4 - Tabela de Codigos das Obrigacoes do ICMS a Recolher',
            'Versao': dados_identados[0][7:10],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=5',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('ICMS.json', 'w') as f:
        f.write(json_dados)


def request_tabela_cfop():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=2')

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


        dados_linha = {"CFOP":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'Tabela Codigo Fiscal de Operacao e Prestacao - CFOP',
            'Versao': dados_identados[0][7:9],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=2',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('CFOP.json', 'w') as f:
        f.write(json_dados)


def request_tabela_ibge_municipios():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=4')

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


        dados_linha = {"Codigo_municipio":linha[0], 'Nome_municipio': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'Tabela de Muncipios do IBGE',
            'Versao': dados_identados[0][7:9],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=4',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('IBGE_Municipios.json', 'w') as f:
        f.write(json_dados)


def request_tabela_paises_ibge():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=6')

    valores = r.content
    dados_decodificados = valores.decode("unicode_escape")
    dados_sem_acento = unidecode(dados_decodificados)
    dados_identados = dados_sem_acento.split('\r\n')
    quantidade_linhas_maxima = len(dados_identados) - 1

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


        dados_linha = {"Codigo_pais":linha[0], 'Nome_pais': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'Tabela de Paises do IBGE',
            'Versao': dados_identados[0][7:9],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=6',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('IBGE_Paises.json', 'w') as f:
        f.write(json_dados)


def request_tabela_paises_siscomex():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=13')

    valores = r.content
    dados_decodificados = valores.decode("unicode_escape")
    dados_sem_acento = unidecode(dados_decodificados)
    dados_identados = dados_sem_acento.split('\r\n')
    quantidade_linhas_maxima = len(dados_identados) - 1

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


        dados_linha = {"Codigo_pais":linha[0], 'Nome_pais': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'Tabela de Paises SISCOMEX',
            'Versao': dados_identados[0][7:9],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=13',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('SISCOMEX_Paises.json', 'w') as f:
        f.write(json_dados)


def request_tabela_solventes():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=1')

    valores = r.content
    dados_decodificados = valores.decode("unicode_escape")
    dados_sem_acento = unidecode(dados_decodificados)
    dados_identados = dados_sem_acento.split('\r\n')
    quantidade_linhas_maxima = len(dados_identados) - 1

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


        dados_linha = {"Codigo_combustivel":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'Tabela de Produtos para Combustiveis / Solvente',
            'Versao': dados_identados[0][7:9],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=1',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('Solventes_Combustiveis.json', 'w') as f:
        f.write(json_dados)


def request_tabela_mercadoria():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=3')

    valores = r.content
    dados_decodificados = valores.decode("unicode_escape")
    dados_sem_acento = unidecode(dados_decodificados)
    dados_identados = dados_sem_acento.split('\r\n')
    quantidade_linhas_maxima = len(dados_identados) - 1

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


        dados_linha = {"Codigo_combustivel":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'Tabela Genero do Item de Mercadoria/Servico',
            'Versao': dados_identados[0][7:10],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=3',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('Mercadoria_servico.json', 'w') as f:
        f.write(json_dados)


def request_tabela_transporte_eletronico():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=12')

    valores = r.content
    dados_decodificados = valores.decode("unicode_escape")
    dados_sem_acento = unidecode(dados_decodificados)
    dados_identados = dados_sem_acento.split('\r\n')
    quantidade_linhas_maxima = len(dados_identados) - 1

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


        dados_linha = {"Tipo":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'Tipo de Conhecimento de Transporte Eletronico',
            'Versao': dados_identados[0][7:8],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=12',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('Transporte_eletronico.json', 'w') as f:
        f.write(json_dados)


def request_tabela_transporte_conhecimento():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=7')

    valores = r.content
    dados_decodificados = valores.decode("unicode_escape")
    dados_sem_acento = unidecode(dados_decodificados)
    dados_identados = dados_sem_acento.split('\r\n')
    quantidade_linhas_maxima = len(dados_identados) - 1

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


        dados_linha = {"Tipo":linha[0], 'Descricao': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'Tipo do Conhecimento de Transporte',
            'Versao': dados_identados[0][7:10],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=7',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('Conhecimento_transporte.json', 'w') as f:
        f.write(json_dados)


def request_tabela_codigo_uf():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=9')

    valores = r.content
    dados_decodificados = valores.decode("unicode_escape")
    dados_sem_acento = unidecode(dados_decodificados)
    dados_identados = dados_sem_acento.split('\r\n')
    quantidade_linhas_maxima = len(dados_identados) - 1

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


        dados_linha = {"Codigo_UF":linha[0], 'Sigla_UF': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'UF codigo IBGE - Sigla',
            'Versao': dados_identados[0][7:8],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=9',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('Codigo_UF.json', 'w') as f:
        f.write(json_dados)


def request_tabela_sigla_uf():
    r = requests.get('http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=10')

    valores = r.content
    dados_decodificados = valores.decode("unicode_escape")
    dados_sem_acento = unidecode(dados_decodificados)
    dados_identados = dados_sem_acento.split('\r\n')
    quantidade_linhas_maxima = len(dados_identados) - 1

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


        dados_linha = {"Codigo_UF":linha[0], 'Sigla_UF': linha[1], 'Data_inicio': data_inicio, 'Data_fim':data_fim}
        lista.append(dados_linha)

    json_dados = json.dumps(

            {
            'Pacote':'Tabelas Globais',
            'Tabela':'UF codigo IBGE - Sigla',
            'Versao': dados_identados[0][7:8],
            'Link_arquivo': 'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote=1&idTabela=10',
            'Link_site': 'http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal',
            'Dados':lista,
            }, 

        indent=4
        )

    with open('Sigla_UF.json', 'w') as f:
        f.write(json_dados)



