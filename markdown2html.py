#!/usr/bin/python3
import sys
from os.path import exists

"""
A markdown to html file
    arg 1: Markdown file
    arg 2: output file name (HTML)
"""

markdownHeader = {'#': '<h1> </h1>', '##': '<h2> </h2>', '###': '<h3> </h3>',
                  '####': '<h4> </h4>', '#####': '<h5> </h5>', '######': '<h6> </h6>'}

if __name__ == '__main__':

    """
    Check if number of arguments == 2
    """

    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    """
    Check if input file is a correct markdown file
    """
    if "." in sys.argv[1]:
        newArr = sys.argv[1].split('.')
        if len(newArr) != 2:
            sys.stderr.write('Bad Markdown file\n')
            exit(1)
        if newArr[1] != "md":
            sys.stderr.write('First argument must a markdown file\n')

    """
    Check if markdown file exist
    """
    if exists(sys.argv[1]) == False:
        sys.stderr.write('Missing {}\n'.format(sys.argv[1]))
        exit(1)

    """
    Opening the markdown file for file operations
    """

    with open(sys.argv[1]) as markdown:
        line = True
        while line:
            line = markdown.readline()
            if line.startswith('#'):  # Headings operation
                hash = line.split(' ')[0]

                with open(sys.argv[2], 'a') as htmlFile:
                    hashL = len(hash) + 1
                    htmlFile.write('{}{}{}\n'.format(
                        markdownHeader[hash].split(' ')[0], line[hashL: -1], markdownHeader[hash].split(' ')[1]))

            else:
                with open(sys.argv[2], 'a') as htmlFile:
                    htmlFile.write(line)

    exit(0)
