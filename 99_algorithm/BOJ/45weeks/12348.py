N = int(input())
l = len(str(N))
idx = max(1, N - l * 9)

for i in range(idx, N):
    num = i
    total = num + sum(map(int, str(num)))

    if total == N:
        print(i)
        exit(0)

print(0)
