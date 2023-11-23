from bs4 import BeautifulSoup  # pip install beautifulsoup4

# em alguns sites o webscraping usando o BS não é permitido, verificar as regras antes de fazer requisições

# carregando a página html que está local, o r significa modo de leitura, armazenando na variável arquivo
with open("Pagina Hashtag.html", "r", encoding="utf-8") as arquivo:
    site = BeautifulSoup(arquivo, "html.parser")  # conectando o arquivo com o BS
    # html.parser vai ler o html e o traduz para o BS

# print(site)  # imprime o conteúdo após o parse do html pelo BS
# print(site.prettify())  # método que melhora a apresentação da leitura do HTML

titulo = site.title  # traz toda a tag 'title' do html
titulo = site.title.text  # traz somente o conteúdo texto da tag

titulo = site.find("title")  # uma outra maneira de buscar uma tag do html
h1 = site.find("h1")  # por padrão, o primeiro parâmetro em forma de string faz a busca pela tag do html

barra_navegacao = site.find("nav")  # pega todo o elemento NAV do html, inclusive elementos 'filho'
link = barra_navegacao.find("a")  # pega, dentro da tag 'nav', o primeiro elemento 'a' dentro dela
links = barra_navegacao.find_all("a")  # armazena em uma lista todos os elementos 'a' contidos em 'nav'
print(links[0].attrs)  # pega o primeiro elemento da lista de links e transforma em um dicionário contendo os atributos
# exemplo coletando o valor do atributo "href" com a funcionalidade demonstrada acima:
url_link = links[0]["href"]  # traz apenas o valor do atributo 'href' do primeiro elemento de links

for link in links:
    print(link["href"])

# =======================================
# ENCONTRANDO ELEMENTOS COM VÁRIAS REGRAS
# =======================================

# traz elementos de tags diferentes ao mesmo tempo
elementos_navegacao = barra_navegacao.find_all(["a", "button"])
# buscando através da classe. atenção para o underline após o 'class', por se tratar de palavra reservada
subtitulo = site.find(class_="tit")
# buscando através do id
cabecalho = site.find(id="header")
# funciona para qualquer outro atributo existente no html
cabecalho2 = site.find(role="banner")
# também é possível colocar vários parâmetros na busca
cabecalho3 = site.find(id="header", role="banner")
# caso haja hífen no nome do atributo, deve-se colocar em um dicionário de parâmetros
logo = site.find("img", {"data-ll-status": "loaded"})
# o primeiro atributo (tag) é posicional, deve ser sempre declarada como primeiro parâmetro
# caso haja mais parâmetros, deve-se continuar passando através do dicionário:
logo = site.find("img", {"data-ll-status": "loaded", "class": "custom-logo"})

# =======================================
# BUSCA POR TEXTO
# =======================================

# texto é igual
foco_mercado = site.find(string="Foco no Mercado")  # encontra o texto, e não o elemento

# contém no texto
import re  # importando a biblioteca regular expressions, são códigos que representam um padrão de texto
textos = site.find_all(string=re.compile("alunos"))  # usa-se o método compile, passando a regra como parâmetro

# =======================================
# PARENTS E CONTENTS
# =======================================

# busca o elemento e seu respectivo conteúdo acima ao qual 'textos' está contido
parent = textos[0].parent
parent = textos[0].parent.parent  # segundo elemento acima

# retorna uma lista com todos os elementos contigos na barra de navegacao, elementos abaixo
elementos = barra_navegacao.contents
botao = barra_navegacao.contents[1]  # pegando elementos específicos dentro da lista
