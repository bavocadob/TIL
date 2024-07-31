def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            return False
    return True


def dfs(num, cnt):
    if cnt == N:
        print(num)
        return

    for i in range(1, 10, 2):
        temp = num * 10 + i
        if is_prime(temp):
            dfs(temp, cnt + 1)


N = int(input())

for n in [2, 3, 5, 7]:
    dfs(n, 1)
