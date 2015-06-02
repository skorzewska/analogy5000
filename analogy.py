#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import sys
import codecs


# def unicode_csv_reader(unicode_csv_data):
#     # csv.py doesn't do Unicode; encode temporarily as UTF-8:
#     csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
#                             delimiter='\t')
#     for row in csv_reader:
#         # decode UTF-8 back to Unicode, cell by cell:
#         yield [unicode(cell, 'utf-8') for cell in row]


# def utf_8_encoder(unicode_csv_data):
#     for line in unicode_csv_data:
#         yield line.encode('utf-8')


def read_corpus():
    lexicon = {}
    with open("train.tab", 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            if row[1] in lexicon:
                lexicon[row[1]][row[2]] = row[0]
            else:
                lexicon[row[1]] = {row[2]:row[0]}
    return lexicon


def replace_in_dict(dictionary, what, with_what):
    result = {}
    for key, value in dictionary.items():
        result[key] = value.replace(what, with_what, 1)
    return result


def find_analogy(lexicon, ending, stem):
    for key, value in lexicon.items():
        if key.endswith(ending):
            keystem = key[:-len(ending)]
            return replace_in_dict(value, keystem, stem)
    return False 

def inflect(lexicon, word):
    for i in range(len(word)):
        result = find_analogy(lexicon, word[i:], word[:i])
        if result:
            break
    return result


if __name__ == '__main__':
    lexicon = read_corpus()
    for key, value in inflect(lexicon, sys.argv[1]).items():
        print ('{}\t{}'.format(value, key))