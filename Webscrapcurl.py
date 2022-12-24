import requests
from bs4 import BeautifulSoup

# Faz a solicitação HTTP para o site
URL = 'https://geralinks.com.br/entretenimento'
page = requests.get(URL)

# Analisa o HTML da página
soup = BeautifulSoup(page.content, 'html.parser')

# Cria um arquivo XML vazio
with open('rss.xml', 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<rss version="2.0">\n')
    f.write('  <channel>\n')
    f.write('    <title>Geralinks</title>\n')

# Encontra todos os elementos com a tag <a>
links = soup.find_all('a')

# Adiciona os links de cada elemento <a> encontrado ao arquivo XML
for link in links:
    with open('rss.xml', 'a') as f:
        f.write(f'    <item>\n')
        f.write(f'      <link>{URL}{link["href"]}</link>\n')
        f.write(f'    </item>\n')

# Finaliza o arquivo XML
with open('rss.xml', 'a') as f:
    f.write('  </channel>\n')
    f.write('</rss>\n')
