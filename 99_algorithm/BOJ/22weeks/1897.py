import collections
import sys

input = sys.stdin.readline

d, initial_word = input().split()
dictionary_words = [input().strip() for _ in range(int(d))]
longest_word = 0

def find_next_words(current_word):
    next_words = []
    current_length = len(current_word)
    for word in dictionary_words:
        if (current_length + 1) != len(word):
            continue
        if current_word in word:
            next_words.append(word)
            continue
        i, j = 0, 0
        while j < len(word):
            if word[j] == current_word[i]:
                i += 1
            j += 1
        if i == len(current_word):
            next_words.append(word)
    return next_words

def bfs():
    global longest_word
    queue = collections.deque([initial_word])
    while queue:
        word = queue.popleft()
        longest_word = word
        next_possible_words = find_next_words(word)
        queue.extend(next_possible_words)

bfs()
print(longest_word)
