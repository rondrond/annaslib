import requests
from bs4 import BeautifulSoup
from isbnlib import get_canonical_isbn


def search(user_input, limit=5):
    if not get_canonical_isbn(user_input):
        annas_url = "https://pt.annas-archive.org/search?q="+user_input
        page = requests.get(annas_url, timeout=2)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all(class_="h-[125]")
        books = []

        for book in results:
            try:
                if len(books) < int(limit):
                    pure_text = book.get_text().strip().split('\n')
                    new_book = [pure_text[3],
                                pure_text[1],
                                pure_text[0],
                                book.find_all("div")[6].get_text(),
                                "https://pt.annas-archive.org"+book.find("a")['href']]
                    books.append(new_book)
            except IndexError:
                pass
        return books
    else:
        annas_url = "https://pt.annas-archive.org/isbn/" + \
            get_canonical_isbn(user_input)
        page = requests.get(annas_url, timeout=2)
        soup = BeautifulSoup(page.content, "html.parser")
        text = soup.find(
            class_='relative top-[-1] pl-4 grow overflow-hidden')
        pure_text = text.get_text().strip().split('\n')
        link = soup.find('a', {
                         'class': 'custom-a flex items-center relative left-[-10] px-[10] py-2 hover:bg-[#00000011]'})['href']
        if len(text) == 0:
            obj = []
            return obj
        else:
            results = soup.find_all('a', {'class': 'custom-a'})[1]
            # results['href'] / annas_url
            details = results.find_all('div', {'class': 'truncate'})
            # details[0].get_text() / format
            # details[1].get_text() / nome do livro
            # details[2].get_text() / editora
            # details[3].get_text() / autor
            new_book = [[pure_text[3], pure_text[1], pure_text[1],
                         "https://pt.annas-archive.org"+link]]
            return new_book


test = []
