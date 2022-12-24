import requests
from bs4 import BeautifulSoup

# Faz a solicitação HTTP para o site
URL = 'http://www.geralinks.com.br'
page = requests.get(URL)

# Analisa o HTML da página
soup = BeautifulSoup(page.content, 'html.parser')

# Cria um arquivo XML vazio
with open('rss.xml', 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<rss version="2.0">\n')
    f.write('  <channel>\n')
    f.write('    <title>Geralinks</title>\n')

# Encontra todos os elementos com a tag <h2> que possuem a classe "title"
titles = soup.find_all('h2', class_='title')

# Adiciona os títulos e links de cada artigo encontrado ao arquivo XML
for title in titles:
    link = title.find('a')['href']
    with open('rss.xml', 'a') as f:
        f.write(f'    <item>\n')
        f.write(f'      <title>{title.text}</title>\n')
        f.write(f'      <link>{link}</link>\n')
        f.write(f'    </item>\n')

# Finaliza o arquivo XML
with open('rss.xml', 'a') as f:
    f.write('  </channel>\n')
    f.write('</rss>\n')
