import sys

input = sys.stdin.readline


def get_prime(limit):
    rst = [True] * (limit + 1)
    rst[0] = rst[1] = False

    for num in range(2, int(limit ** 0.5) + 1):
        if rst[num]:
            for multiple in range(num * num, limit + 1, num):
                rst[multiple] = False

    return rst


lim = 10_000_000
is_prime = get_prime(lim)

T = int(input())


def dfs(val, visited, digits, depth):
    global ans

    if is_prime[val] and val not in ans_nums:
        ans += 1
        ans_nums.add(val)

    if depth == len(visited):
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            dfs(val + digits[i] * (10 ** depth), visited, digits, depth + 1)
            visited[i] = False


for _ in range(T):
    D = list(map(int, input().strip()))
    V = [False] * len(D)
    ans = 0
    ans_nums = set()
    dfs(0, V, D, 0)
    print(ans)
