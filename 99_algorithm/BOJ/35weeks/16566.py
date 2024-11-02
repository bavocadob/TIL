import sys

input = sys.stdin.readline


def find(idx):
    if parents[idx] == idx:
        return idx

    temp = find(parents[idx])

    parents[idx] = temp
    return temp


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa == pb:
        return

    if pa < pb:  # pa가 더 커야 함
        pa, pb = pb, pa

    parents[pb] = pa


def upper_bound(target):
    left = 0
    right = M - 1

    while left <= right:
        mid = (left + right) // 2

        if target >= cards[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left


N, M, K = map(int, input().split())

cards = sorted(list(map(int, input().split()))) + [int(1e9)]

query = list(map(int, input().split()))

parents = [i for i in range(M + 1)]

for q in query:
    pos = upper_bound(q)

    card_idx = find(pos)
    print(cards[card_idx])
    union(card_idx, card_idx + 1)
