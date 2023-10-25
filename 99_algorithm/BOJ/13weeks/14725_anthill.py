import sys

input = sys.stdin.readline


class Trie:
    def __init__(self, val, depth):
        self.val = val
        self.depth = depth
        self.child = dict()

    def dfs(self):
        for w in sorted(self.child.keys()):
            node = self.child[w]
            print(('--' * (node.depth)) + node.val)
            node.dfs()


N = int(input())

root = Trie("", -1)

for _ in range(N):
    _, *words = input().split()
    # word_cnt = int(word_cnt)
    curr = root
    for i, word in enumerate(words):
        if word in curr.child:
            curr = curr.child[word]
            continue

        new_word = Trie(word, i)
        curr.child[word] = new_word
        curr = new_word

root.dfs()
