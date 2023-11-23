from request import site
from bs4 import BeautifulSoup
import re

tbody = site.find("tbody")
linhas = tbody.find_all("tr")

for linha in linhas:
    try:
        nome = linha.find(class_="kKpPOn").text,
        codigo = linha.find(class_="coin-item-symbol").text,
        valores = linha.find_all_next(string=re.compile("\$"))  # lendo todos os valores da linha
        preco = valores[0],
        percentuais = valores = linha.find_all_next(string=re.compile("%"))
        var_1h = "",
        var_24h = "",
        var_7d = "",
        market_cap = valores[2],
        volume = valores[3]
        dict = {"nome": nome, "codigo": codigo, "preco": preco, "market_cap": market_cap, "volume": volume}
    except AttributeError:
        break
