# Written by Ryan West

import requests

# Modify these to change book range. Keep printToFile false to have the texts returned, each as a tuple of
# (book number, book text in one long string).
def downloadBookRange(startNum=1000, filesToRetrieve=5, printToFile=False):

    curFile = startNum

    # list of all books so far
    books = []

    while curFile < startNum + filesToRetrieve:

        filename = str(curFile) + '.txt'
        filepath = 'books/' + filename
        url = 'http://www.gutenberg.org/files/' + str(curFile) + '/' + filename
        url2 = 'http://www.gutenberg.org/files/' + str(curFile) + '/' + str(curFile) + '-0.txt'

        r = requests.get(url)
        if r.status_code == 200:
            if printToFile:
                with open(filepath, 'w') as f:
                    f.write(r.text)
            else:
                books.append((curFile, r.text))
            print('Book #' + str(curFile) + ' retrieved.')
        else:
            r = requests.get(url2)
            if r.status_code == 200:
                if printToFile:
                    with open(filepath, 'w') as f:
                        f.write(r.text)
                else:
                    books.append((curFile, r.text))
                print('Book #' + str(curFile) + ' retrieved (using ' + str(curFile) + '-0.txt).')
            else:
                print('Book #' + str(curFile) + ' failed: ' + str(r.status_code))
        curFile += 1

    if not printToFile:
        return books