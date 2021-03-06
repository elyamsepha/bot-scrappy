import requests
from lxml import html
from bs4 import BeautifulSoup
import re

header = {
	'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75"
}

URL = "https://www.mercadolivre.com.br/ofertas#nav-header"

response = requests.get(URL, headers=header)
print("codigo de requesição: ", response.status_code)

content = response.content
site = BeautifulSoup(content, 'html.parser')

num = 1

nomes = []
precos = []


post = site.find('p', attrs={'class': "promotion-item__title"})
for nome in site.find_all('p', attrs={'class': "promotion-item__title"}):
    for n in nome:
    	nomes.append(n)
    	
for preco in site.find_all('span', attrs={'class': "promotion-item__price"}):
	for pre in preco:
		for p in pre:
			if ('$' in p) == True:
				precos.append(p)
			else:
				pass

arq = open('itens.txt', 'w')

num = 0
for c in range(len(nomes)):
	arq.write(f'titulo: {nomes[num]}\npreço: {precos[num]}\n\n')
	num = num + 1
