N = int(input())
numbers = list(map(int, input().split()))
last_occurrence = {}
deleted = {}

for i in range(N):
    last_occurrence[numbers[i]] = i

current = numbers[0]
ans = 0

for i in range(1, N):
    if numbers[i] == current or deleted.get(numbers[i], False):
        continue

    if i < last_occurrence[current]:
        ans += 1
        if last_occurrence[numbers[i]] < last_occurrence[current]:
            deleted[current] = True
            current = numbers[i]
        else:
            deleted[numbers[i]] = True
    else:
        current = numbers[i]

print(ans)