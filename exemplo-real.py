from bs4 import BeautifulSoup
import requests  # pip install requests
import re

link = "https://coinmarketcap.com/"
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")

tabela = site.find("tbody")
linhas = tabela.find_all("tr")
for linha in linhas:
    try:
        print(linha.find(class_="kKpPOn").text)  # encontrando o nome da moeda
        print(linha.find(string=re.compile("\$")))  # buscando a moeda pelo texto, contrabarra vai antes por conta de o $ ser um caracter especial em regular expressions
    except AttributeError:
        break

'''
colocamos a consulta acima dentro de um try de AttributeError pois, o BS trabalha com os dados estáticos do HTML
como na pagina em questão temos a tabela que carrega gradualmente com o descer do mouse, o BS não consegue
carregar os dados dinamicamente, só o que foi passado na requisição da url
'''

# outra forma de fazer a mesma coisa:

for linha in linhas:
    try:
        texto_linha = linha.get_text(separator=";")  # pega a linha toda da tabela, separando os textos por ;
        lista_textos = texto_linha.split(";")
        nome = lista_textos[1]
        preco = lista_textos[4]
        print(nome, preco)
    except IndexError:
        break