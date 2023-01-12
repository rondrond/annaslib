#example: call anna.search(string input, int limit)
import annas_archive as anna
import sys

try:
    books = anna.search(sys.argv[1])
except IndexError:
    books = anna.search(input("Author or book name:\n"))
    
for book in books:
    print(f'\n{book[1]}, de {book[0]}. {book[4]}')
# {book[2]}: 2, {book[3]}: 3,99