import annas_archive as anna
import sys

try:
    books = anna.search(sys.argv[1]tes)
except IndexError:
    books = anna.search(input("Author or book name:\n"))
    
for book in books:
    print(f'{book[1]}, de {book[0]}. {book[4]}')
# {book[2]}: 2, {book[3]}: 3,
    print('\n')