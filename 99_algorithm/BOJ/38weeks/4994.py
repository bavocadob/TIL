from collections import deque


def solve(n):
    queue = deque()
    queue.append(1)

    while queue:
        curr = queue.popleft()
        if curr % n == 0:
            return curr

        queue.append(curr * 10)
        queue.append(curr * 10 + 1)


ans_dict = {}
while True:
    N = int(input())

    if N == 0:
        break

    if N not in ans_dict:
        ans = solve(N)
        ans_dict[N] = ans

    print(ans_dict[N])
