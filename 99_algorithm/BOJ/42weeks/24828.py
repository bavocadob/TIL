def dfs(pos, curr):
    if pos == -1:
        return curr == 0

    val = int(A[pos])
    ex = 0

    while True:
        temp = val ** ex
        if temp > curr:
            return False

        if temp % 10 == curr % 10:
            if dfs(pos - 1, (curr - temp) // 10):
                ans[pos] = ex
                return True

        ex += 1


A, B = input().split()
B = int(B)

ans = [0] * len(A)
dfs(len(A) - 1, B)

print(*ans)
