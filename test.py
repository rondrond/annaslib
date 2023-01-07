import requests
from bs4 import BeautifulSoup

URL = "https://pt.annas-archive.org/search?q=deleuze"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
#results = soup.find(id="mb-4");
results = soup.find_all(class_="h-[125]")

# eu consigo acessar os resultados pelo results[], printando nome do autor
print(results[0].find_all("div")[7].get_text())
print(results[1].find_all("div")[7].get_text())

# mas não consigo rodar dentro da lista e organizar os itens pra limpá-los, dá o erro:  IndexError: list index out of range
books = []

for book in results:
    new_book = [book.find_all("div")[7].get_text(),
            book.find_all("div")[5].get_text(), 
            book.find_all("div")[4].get_text(),
            book.find_all("div")[6].get_text(),
            book.find("a")['href']]
    books.append(new_book)
