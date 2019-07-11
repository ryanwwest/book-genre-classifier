# Written by Ben Horrocks

import argparse
import os
import re


def parse_file(file):
    file = file.split('\n')
    end_header = re.compile('\*\*\* START OF THIS PROJECT GUTENBERG EBOOK*')
    start_body = re.compile('CONTENTS')
    end_body = re.compile('\*\*\* END OF THIS PROJECT GUTENBERG EBOOK*')
    ending_one = re.compile('POSTSCRIPT')
    ending_two = re.compile('APPENDIX')
    body = False
    result = []
    title = ''
    author = ''
    for line in file:
        if 'Title:' in line:
            title = line.split('Title:')[1]
        if 'Author:' in line:
            author = line.split('Author:')[1]
        if body:
            found = end_body.search(line) or ending_one.search(line) or ending_two.search(line)
            if found:
                return result, title, author
            if len(line) > 15:
                line = re.sub(r'[^a-zA-Z0-9\ \,\.\'\"\!\?\-]+', '', line)
                result.append(line)
        else:
            found = end_header.search(line) or start_body.search(line)
            if found:
                body = True
    return result, title, author

# parser = argparse.ArgumentParser(description='Parses a text file and removes the header and footer ')
# parser.add_argument('Files', metavar='N', type=str, nargs='+',
#                     help='an integer for the accumulator')
#
# args = parser.parse_args()
#
# files = args.Files
# print(files)
# while len(files) > 0:
#     file = files.pop(0)
#     if os.path.isfile(file):
#         f = parse_file(open(file, 'r', encoding="utf-8").read())
#         new_file = 'parsed_books/parsed' + file.split('/')[-1]
#         out = open(new_file, 'w+', encoding="utf-8")
#         for ln in f:
#             out.write(ln + '\n')
#         out.close()
#     else:
#         files_to_add = os.listdir(file)
#         for each in files_to_add:
#             # files.append(os.path.join(file, each))
#             files.append(file + '/' + each)
