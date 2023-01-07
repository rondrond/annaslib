import requests
import sys
from bs4 import BeautifulSoup

def search(input):
    URL = "https://pt.annas-archive.org/search?q="+input
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(class_="h-[125]")
    books = []

    for book in results:
        try:
            new_book = [book.find_all("div")[7].get_text(),
                book.find_all("div")[5].get_text(), 
                book.find_all("div")[4].get_text(),
                book.find_all("div")[6].get_text(),
                "https://pt.annas-archive.org"+book.find("a")['href']]
            books.append(new_book)
        except IndexError:
            pass
    return books

try:
    books = search(sys.argv[1])
except IndexError:
    books = search(input("Author or book name:\n"))
    
for book in books:
    for field in book:
        print(f'{field}\n')
    print('\n')