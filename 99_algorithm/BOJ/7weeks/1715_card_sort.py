import heapq
import sys

input = sys.stdin.readline

N = int(input())

cards = [int(input()) for _ in range(N)]

heapq.heapify(cards)

cnt = 0
while len(cards) != 1:

    a = heapq.heappop(cards) + heapq.heappop(cards)
    cnt += a
    heapq.heappush(cards, a)
print(cnt)
