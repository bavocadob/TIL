import sys
from collections import deque

input = sys.stdin.readline


def solve():
    day = 0

    while papers or no_papers:
        day += 1

        if papers:
            target = papers.popleft()

            if target < day:
                return False
        else:
            target = no_papers.popleft()

            if target < day:
                return False

        for j in range(min(N - 1, len(no_papers))):
            target = no_papers.popleft()
            if target < day:
                return False

    return True


N, M = map(int, input().split())

papers = []
no_papers = []

for i in range(M):
    d, t = input().split()

    if t == 'y':
        papers.append(int(d))
    else:
        no_papers.append(int(d))

papers = deque(sorted(papers))
no_papers = deque(sorted(no_papers))

if solve():
    print('Yes')
else:
    print('No')
