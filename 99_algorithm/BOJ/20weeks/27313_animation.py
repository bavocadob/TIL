N, M, K = map(int, input().split())

anime = list(map(int, input().split()))

anime.sort()

ans = 0

for i in range(N):
    temp = 0
    if i < K:
        temp = anime[i]
    else:
        temp = anime[i - K] + anime[i]

    if temp > M:
        break

    ans += 1
    anime[i] = temp

print(ans)
