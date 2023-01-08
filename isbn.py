from isbnlib import get_canonical_isbn
#annas_archive
import requests
from bs4 import BeautifulSoup

input = "oi eu sou um 9780440539810 texto 853250812X sem isbn"
print(get_canonical_isbn(input)) 
URL = "https://pt.annas-archive.org/isbn/"+get_canonical_isbn(input)
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
if(len(soup.find_all('h2', {'class':'mt-12 mb-1 text-3xl font-bold'}))==0):
    obj = ['', '', '', '']
    print(obj)
else:
    results = soup.find_all('a', {'class':'custom-a'})[1]
    #results['href'] / url
    details = results.find_all('div', {'class':'truncate'})
    #details[0].get_text() / format
    #details[1].get_text() / nome do livro
    #details[2].get_text() / editora
    #details[3].get_text() / autor
    new_book = [details[3].get_text(), details[1].get_text(), details[0].get_text(), results['href']]
    print(len(new_book))