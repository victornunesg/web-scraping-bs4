from request import site
import re

tbody = site.find("tbody")  # coletando a tabela da página html
linhas = tbody.find_all("tr")  # coletando todas as linhas da tabela
moedas = {}  # dicionário que será a resposta consolidada do scraping, contendo as informações das moedas

for linha in linhas:
    try:
        nome_moeda = linha.find(class_="kKpPOn").text
        codigo_moeda = linha.find(class_="coin-item-symbol").text
        valores = linha.find_all(string=re.compile("\$"))  # lendo todos os valores da linha
        preco = valores[0]  # o preco atual é o primeiro item da lista de valores
        percentuais = linha.find_all(string=re.compile("%"))  # separa os percentuais na busca por texto com RE
        for i, percentual in enumerate(percentuais):
            if "gUnzUB" in percentual.parent["class"]:  # classe que define o sinal de negativo na variação %
                percentuais[i] = f'-{percentual}'  # troca o texto da lista de percentuais com valor negativo

        var_1h = percentuais[0]
        var_24h = percentuais[1]
        var_7d = percentuais[2]

        market_cap = valores[2]
        volume = valores[3]

        dict = {"nome": nome_moeda, "codigo": codigo_moeda, "preco": preco, "market_cap": market_cap, "volume": volume,
                "var_1h": var_1h, "var_24h": var_24h, "var_7d": var_7d}

        # acrescenta um item no dicionário que contém o nome da moeda e os dados da mesma em 'dict'
        moedas[nome_moeda] = dict

    except AttributeError:
        break
