import annas_archive as anna
import sys

try:
    books = anna.search(sys.argv[1])
except IndexError:
    books = anna.search(input("Author or book name:\n"))
    
for book in books:
    for field in book:
        print(f'{field}\n')
    print('\n')