import sys

input = sys.stdin.readline


def transform_string(st):
    while True:
        for pattern, replacement in rules.items():
            if pattern in st:
                st = st.replace(pattern, replacement, 1)
                break
        else:
            break
    return st


rules = {
    "aa": "",
    "bb": "",
    "cc": "",
    "baba": "abab",
    "caca": "acac",
    "cbcb": "bcbc",
    "cbcabab": "bcbcaba"
    # abcbcbcbcba
}

n = int(input().strip())
for _ in range(n):
    s = input().strip()
    result = transform_string(s)
    print("closed" if result == "" else "open")
