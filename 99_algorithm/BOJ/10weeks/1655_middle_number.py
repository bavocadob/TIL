import heapq
import sys

input = sys.stdin.readline
N = int(input())

left = []
right = []

for _ in range(N):
    number = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -number)
    else:
        heapq.heappush(right, number)
    if left and right and -left[0] > right[0]:
        left_temp = -heapq.heappop(left)
        right_temp = heapq.heappop(right)

        heapq.heappush(left, -right_temp)
        heapq.heappush(right, left_temp)

    print(-left[0])
