import annas_archive as anna
import sys

limit = 5
try:
    books = anna.search(sys.argv[1], sys.argv[2])
except IndexError:
    books = anna.search(input("Author or book name:\n"), limit)
    
for book in books:
    print(f'{book[1]}, de {book[0]}. {book[4]}')
# {book[2]}: 2, {book[3]}: 3,
    print('\n')