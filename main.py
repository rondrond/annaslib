from lxml import html
import requests

entrada = input('Qual livro quer achar? ')
page = requests.get(f'https://pt.annas-archive.org/search?q={entrada}')

tree = html.fromstring(page.content)
books = []

i = 0
while(i<10):
    books.append([tree.xpath('/html/body/div[2]/div[2]/div[*]/a/div[2]/div[2]/text()')[i], tree.xpath('/html/body/div[2]/div[2]/div[*]/a/div[2]/div[1]/text()')[i], 'https://pt.annas-archive.org'+tree.xpath('/html/body/div[2]/div[2]/div[*]/a/@href')[i]])
    i += 1
print(f'\n encontramos {len(books)} livros, esses são seus títulos:\n')

for livro in books:
    print(f'{livro[0]}, ')
 
uai = input("\n Quer ver os detalhes de todos? y/n\n")

if uai == "y":
    for livro in books:
        print(f'Nome: {livro[0]}\nArquivo: {livro[1]}\nLink pra baixar: {livro[2]}\n')
else:
    print("vlwflw")