import sys

input = sys.stdin.readline


class Trie:

    def __init__(self):
        self.child = dict()
        self.end = False

    def search(self, phone):
        curr = self
        for p in phone:
            curr = curr.child[p]

        if curr.child:
            return True
        else:
            return False


def add(phone_number, root):
    curr = root

    for char in phone_number:
        if char not in curr.child:
            new = Trie()
            curr.child[char] = new

        curr = curr.child[char]
    curr.end = True
    return False


def solution():
    n = int(input())
    root = Trie()
    phones = [input().rstrip() for _ in range(n)]
    for phone in phones:
        add(phone, root)

    for phone in phones:
        if root.search(phone):
            return False

    return True


def main():
    t = int(input())

    for tc in range(t):
        if solution():
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
