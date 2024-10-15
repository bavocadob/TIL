import sys

input = sys.stdin.readline


def backtrack(idx):
    global ans
    if idx == N:
        ans = ''
        for num in rst:
            ans += str(num)

        return

    curr = A[0][idx]
    reversed_str = A[1][idx]

    if idx == 0:
        backtrack(idx + 1)
        if ans != '':
            return

        rst[idx] = 1
        backtrack(idx + 1)
    else:
        prev_str = A[rst[idx - 1]][idx - 1]
        if prev_str <= curr:
            backtrack(idx + 1)

        if ans != '' or prev_str > reversed_str:
            return

        rst[idx] = 1
        backtrack(idx + 1)
        rst[idx] = 0


for _ in range(int(input())):
    N = int(input())

    A = [list() for _ in range(2)]

    for _ in range(N):
        temp = input().rstrip()
        A[0].append(temp)
        A[1].append(''.join(reversed(temp)))
    ans = ''
    rst = [0] * N
    backtrack(0)
    print(ans)
