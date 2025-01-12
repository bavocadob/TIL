N = int(input())
balls = list(map(int, input().split()))
T = int(input())

cnt = 0

for i in range(1 << N):
    for j in range(N):
        if i & (1 << j):
            for k in range(N):
                if i & (1 << k):
                    if balls[j] < balls[k] and balls[j] + T >= balls[k] - T:
                        cnt += 1

ans = cnt / (1 << N)
print(ans)
