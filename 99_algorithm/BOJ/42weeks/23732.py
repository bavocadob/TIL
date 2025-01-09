N = int(input())

S = input().rstrip()
idx = -1
count = 0

for i in range(1, N):
    if S[i - 1] == S[i]:
        idx = i - 1
    count += (idx + 1)

print(count)
