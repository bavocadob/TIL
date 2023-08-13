# 민식어
# 정렬하기
# 이게 왜 골드 5지

minsik_dict = {'a': 'a', 'b': 'b', 'k': 'c', 'd': 'd', 'e': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'l': 'i', 'm': 'j',
               'n': 'k', 'c': 'l', 'o': 'm', 'p': 'n', 'r': 'o', 's': 'p', 't': 'q', 'u': 'r', 'w': 's', 'y': 't'}

dictionary = []

N = int(input())

for _ in range(N):
    dictionary.append(input().replace('ng', 'c'))

dictionary.sort(key=lambda x: ''.join([minsik_dict[char] for char in x]))

for word in dictionary:
    print(word.replace('c', 'ng'))
