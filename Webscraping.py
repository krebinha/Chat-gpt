import requests
from bs4 import BeautifulSoup

# Realizar uma solicitação HTTP GET à página da web
url = "https://geralinks.com.br"
page = requests.get(url)

# Analisar o HTML da página
soup = BeautifulSoup(page.content, "html.parser")

# Encontrar todos os elementos <a> que contenham links
links = soup.find_all("a")

# Criar o conteúdo do arquivo XML
xml = "<?xml version='1.0' encoding='UTF-8'?>\n"
xml += "<rss version='2.0'>\n"
xml += "<channel>\n"
xml += "<title>Links da página " + url + "</title>\n"

# Adicionar cada link encontrado ao arquivo XML
for link in links:
    xml += "<link>" + link["href"] + "</link>\n"

xml += "</channel>\n"
xml += "</rss>\n"

# Escrever o conteúdo do arquivo XML em um arquivo rss.xml
with open("rss.xml", "w") as f:
    f.write(xml)
