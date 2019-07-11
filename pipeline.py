from downloader import downloadBookRange
from parser import parse_file
from nl_parser_functioned import nltk_parser

import timeit

number_to_read_in = 500

start = timeit.default_timer()

print("")
print(str(number_to_read_in) + " books requested from web")
print("")

books = downloadBookRange(filesToRetrieve=number_to_read_in)
print("")
print(str(len(books)) + " books correctly read from web")
print("")
parsed_books = []

for book in books:
    parsed_book, title, author = parse_file(book[1])
    if len(parsed_book) > 0:
        print("#" + str(book[0]) + " headers parsed")
        parsed_books.append((parsed_book, title, author, book[0]))
    else:
        print("#" + str(book[0]) + " failed headers parsed")

print("")
print(str(len(parsed_books)) + " books correctly parsed headers")
print("")

number_parsed = nltk_parser(parsed_books)

print("")
print(str(number_parsed) + " books added to data set")
print("")

finish = timeit.default_timer()

print(str(finish - start) + ' seconds')

quit()
