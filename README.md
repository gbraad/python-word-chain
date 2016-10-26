Word Chain
==========


## Preparation
```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install requests nltk networkx
```


## Implementation #1
Using NLTK to determine the word distance and NetworkX to traverse the graph.

using `5letter.html` (VERY SLOW)
```
$ python3 wordchain-nltk-networkx.py
Shortest path between "clock" and "watch" is:
['clock', 'clack', 'clach', 'coach', 'roach', 'rotch', 'ratch', 'watch']
```

## Implementation #2
Re-implemented using a simple graph generation and finding the wordchain using breadth-first-search. Significantly faster than the NetworkX approach.

using `5letter.html` (ACCEPTABLE)
```
$ python3 wordchain-simplegraph-bfs.py
Shortest path between "clock" and "watch" is:
['clock', 'clack', 'clach', 'coach', 'roach', 'rotch', 'ratch', 'watch']
```

## Note
words are not enforced to be of the same length.

```
   if len(word1) != len(word2):
        return None
```
