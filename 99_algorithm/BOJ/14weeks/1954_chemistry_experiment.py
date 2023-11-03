import sys

input = sys.stdin.readline

N = int(input())
reagents = []

for _ in range(N):
    a, b = map(int, input().split())

    reagents.append((a, b))

M = int(input())
ans = 0
if N != 1:
    for i in range(1, M):
        cnt = i
        target = reagents[0][0] * i + reagents[0][1]
        flag = True
        for j in range(1, N):
            a, b = reagents[j]
            temp = target - b
            if temp < 0 or temp % a:
                flag = False
                break
            cnt += temp // a

        if flag and cnt == M:
            ans = target
            break
else:
    ans = reagents[0][0] * M + reagents[0][1]
print(ans)
