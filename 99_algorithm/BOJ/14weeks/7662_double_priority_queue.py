import heapq
import sys

input = sys.stdin.readline


def solution():
    n = int(input())

    min_q = []
    max_q = []
    deleted = []
    cnt = 0

    for _ in range(n):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            heapq.heappush(min_q, (num, cnt))
            heapq.heappush(max_q, (-num, cnt))
            deleted.append(False)
            cnt += 1
        else:
            if num == 1:
                while max_q and deleted[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    deleted[max_q[0][1]] = True
                    heapq.heappop(max_q)
            elif num == -1:
                while min_q and deleted[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    deleted[min_q[0][1]] = True
                    heapq.heappop(min_q)

    while max_q and deleted[max_q[0][1]]:
        heapq.heappop(max_q)
    while min_q and deleted[min_q[0][1]]:
        heapq.heappop(min_q)

    if not (min_q and max_q):
        print('EMPTY')
    else:
        print(-max_q[0][0], min_q[0][0])


T = int(input())

for tc in range(T):
    solution()
