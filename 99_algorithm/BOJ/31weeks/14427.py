import heapq
import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

queue = []

for i in range(N):
    heapq.heappush(queue, (numbers[i], i))

Q = int(input())

for _ in range(Q):
    inp = input().rstrip()

    if len(inp) > 1:
        _, idx, val = map(int, inp.split())

        heapq.heappush(queue, (val, idx - 1))
        numbers[idx - 1] = val
    else:
        while numbers[queue[0][1]] != queue[0][0]:
            heapq.heappop(queue)

        print(queue[0][1] + 1)
