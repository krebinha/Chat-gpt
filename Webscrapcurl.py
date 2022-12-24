import subprocess
import xml.etree.ElementTree as ET

# Executa o comando curl para fazer uma requisição HTTP GET para a página
output = subprocess.run(['curl', '-s', 'https://geralinks.com.br/'], capture_output=True).stdout

# Verifica se a requisição foi bem-sucedida
if output:
  # Cria um objeto Beautiful Soup a partir da string HTML
  soup = BeautifulSoup(output, 'html.parser')
  
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
  print("Erro ao fazer a requisição")
