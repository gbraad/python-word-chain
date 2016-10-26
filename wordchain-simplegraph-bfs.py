#!/bin/env python3
from requests import get
import re
import sys
import argparse
from collections import deque
from itertools import chain


# load file
def load_words_file(url):
    filecontent = get(url).text
    return re.findall(r'<pre>(.*?)</pre>', filecontent, re.S)[0].replace('\n', ' ').strip().split(' ')


def distance_of_one(test):
    distance = 0
    for a, b in test:
        if a != b:
            distance += 1
            if distance > 1:
                # break early
                return False

    # true if distance is 1
    return distance == 1


def get_words_close(word, all_words):
    result = set()
    for test_word in all_words:
        if distance_of_one(zip(word, test_word)):
            result.add(test_word)
    return result


def get_word_graph(words):
    return {w: get_words_close(w, words) for w in words}


def find_word_chain(word1, word2, word_graph):
    word_queue = deque([word1])
    predecessors = {}

    while word_queue:
        word = word_queue.popleft()
        # check if word in graph
        for neighbor in word_graph[word]:
            # prevent taking previous words
            if neighbor not in predecessors:
                word_queue.append(neighbor)
                predecessors[neighbor] = word
                # finsihed?
                if neighbor == word2:
                    result = [word2]
                    while result[-1] != word1:
                        result.append(predecessors[result[-1]])
                    return list(reversed(result))
    return None


def main():
    parser = argparse.ArgumentParser(description='Word chain: word1 word2 url')
    parser.add_argument('word1', default='clock', nargs='?', help="first word")
    parser.add_argument('word2', default='watch', nargs='?', help="second word")
    parser.add_argument('url', default='https://raw.githubusercontent.com/gbraad/python-word-chain/master/5letter.html', nargs='?', help="url of word file")
    args = parser.parse_args()
    
    words = load_words_file(args.url);
    graph = get_word_graph(words)

    print('Shortest path between "%s" and "%s" is:' % (args.word1, args.word2))
    chain = find_word_chain(args.word1, args.word2, graph)
    print(chain)


if __name__ == '__main__':
    main()	
