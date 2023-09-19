# import sys
#
# input = sys.stdin.readline
#
# G = int(input())
# P = int(input())
#
# visited = [False] * G
# gate_dict = {i: i for i in range(G)}
#
# for _ in range(P):
#     gate = int(input()) - 1
#     for i in range(gate_dict[gate], -1, -1):
#         if not visited[i]:
#             visited[i] = True
#             gate_dict[gate] = i
#             break
#     else:
#         break
#
# print(sum(visited))

def find(n):
    if p[n] < 0: return n
    p[n] = find(p[n])
    return p[n]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b: return
    p[a] += p[b]
    p[b] = a
    print(p)


import sys

input = sys.stdin.readline
G = int(input())
p = [-1] * (G + 1)
P = int(input())
for i in range(P):
    g = find(int(input()))
    if g:
        union(g - 1, g)
    else:
        print(i)
        break
else:
    print(G)

