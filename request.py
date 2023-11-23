from bs4 import BeautifulSoup
import requests  # pip install requests

link = "https://coinmarketcap.com/"
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")