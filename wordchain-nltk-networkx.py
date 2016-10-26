#!/bin/env python3
from requests import get
import re
from nltk.metrics import *
import networkx
import itertools
import sys
import argparse


# load file
def load_words_file(url):
    filecontent = get(url).text
    return re.findall(r'<pre>(.*?)</pre>', filecontent, re.S)[0].replace('\n', ' ').strip().split(' ')

def get_word_pairs(words):
    wordsfilter = filter(lambda x: edit_distance(x[0], x[1]) == 1, itertools.product(words, words))
    return wordsfilter

def main():
    parser = argparse.ArgumentParser(description='Word chain: word1 word2 url')
    parser.add_argument('word1', default='clock', nargs='?', help="first word")
    parser.add_argument('word2', default='watch', nargs='?', help="second word")
    parser.add_argument('url', default='https://raw.githubusercontent.com/gbraad/python-word-chain/master/5letter.html', nargs='?', help="url of word file")
    args = parser.parse_args()
    
    words = load_words_file(args.url);
    words = get_word_pairs(words)

    G = networkx.Graph()
    G.add_edges_from(words)
    print('Shortest path between "%s" and "%s" is:' % (args.word1, args.word2))
    print(networkx.shortest_path(G, args.word1, args.word2))


if __name__ == '__main__':
    main()	
