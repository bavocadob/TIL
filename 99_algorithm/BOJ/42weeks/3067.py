import sys

input = sys.stdin.readline

n = int(input())
pops, popy, popi, pop_start = [], [], [], []
max_population = 0

for _ in range(n):
    y, inc, s, start = map(int, input().split())
    popy.append(y)
    popi.append(inc)
    pops.append(s)
    pop_start.append(start)

for i in range(n):
    temp = pops[i] + (popi[i] * popy[i])

    for j in range(n):
        if j == i:
            continue

        curr_year = (popy[i] + pop_start[i]) - pop_start[j]

        if curr_year < 0:
            curr_size = 0
        else:
            curr_size = popi[j] * curr_year + pops[j]

        years_after = curr_year - popy[j]

        if years_after >= 0:
            curr_size = popi[j] * popy[j] + pops[j]
            curr_size -= popi[j] * years_after
            curr_size = max(0, curr_size)

        temp += curr_size

    max_population = max(max_population, temp)

print(max_population)
