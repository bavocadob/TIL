M = int(input())
S = input()
ans = float('inf')

for i in range(1, M + 1):
    counter = {}
    temp = 0

    for left in range(i):
        t = 0
        for j in range(left, len(S), i):
            counter[S[j]] = counter.get(S[j], 0) + 1
            t += 1

        temp += (t - max(counter.values()))
        counter.clear()

    ans = min(ans, temp)

print(ans)
