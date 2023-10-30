import heapq
import sys

input = sys.stdin.readline


def solution():
    n = int(input())

    min_q = []
    max_q = []
    min_del_cnt = 0
    max_del_cnt = 0
    cnt = 0

    for _ in range(n):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)
            cnt += 1
        else:
            if min_del_cnt + max_del_cnt >= cnt:
                continue

            if num == 1:
                max_del_cnt += 1
                heapq.heappop(max_q)
            else:
                min_del_cnt += 1
                heapq.heappop(min_q)

            if min_del_cnt + max_del_cnt == cnt:
                min_q = []
                max_q = []

    if min_del_cnt + max_del_cnt == cnt:
        print('EMPTY')
    else:
        print(-heapq.heappop(max_q), heapq.heappop(min_q))


T = int(input())

for tc in range(T):
    solution()
