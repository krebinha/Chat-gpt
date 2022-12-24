import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Faz uma requisição HTTP GET para a página
response = requests.get('https://geralinks.com.br')

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
  # Obtém o conteúdo da resposta como uma string
  html_string = response.content

  # Cria um objeto Beautiful Soup a partir da string HTML
  soup = BeautifulSoup(html_string, 'html.parser')
  
  # Cria um elemento raiz para o documento XML
  root = ET.Element('root')
  
  # Encontra todas as tags <a> que contêm um atributo 'href'
  links = soup.find_all('a', href=True)
  
  # Adiciona os links encontrados como elementos filhos do elemento raiz
  for link in links:
    ET.SubElement(root, 'link').text = link['href']
  
  # Cria um objeto ElementTree a partir do elemento raiz
  tree = ET.ElementTree(root)
  
  # Escreve o documento XML em um arquivo
  tree.write('links.xml', encoding='utf-8', xml_declaration=True)
else:
  print("Erro ao fazer a requisição:", response.status_code)
