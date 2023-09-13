N, K = map(int, input().split())

ans = 0
while True:
    temp = bin(N)[2:][::-1]
    print(temp)
    temp_count = temp.count('1')
    if temp_count <= K:
        break

    water = 2 ** temp.index('1')
    N += water
    ans += water

print(ans)
