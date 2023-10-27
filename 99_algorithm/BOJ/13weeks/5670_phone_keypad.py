class Trie:

    def __init__(self):
        self.child = dict()



def add_trie(w):
    pass



while True:
    try:
        N = int(input())
        words = [input().rstrip() for _ in range(N)]

        for word in words:
            add_trie(word)

    except:
        break
