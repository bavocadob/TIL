import sys

input = sys.stdin.readline

N, K, D = map(int, input().split())

algorithm = [0] * (K + 1)

students = []

for _ in range(N):
    _, level = map(int, input().split())
    A = list(map(int, input().split()))
    students.append((level, A))

students.sort()

left = right = ans = 0

algo_cnt = 0
while True:
    while (students[right][0] - students[left][0]) > D:
        for algo in students[left][1]:
            algorithm[algo] -= 1
            if not algorithm[algo]:
                algo_cnt -= 1
        left += 1
        min_level = students[left][0]

    duplicated = 0
    for algo in students[right][1]:
        if not algorithm[algo]:
            algo_cnt += 1
        algorithm[algo] += 1

        if algorithm[algo] == (right - left + 1):
            duplicated += 1

    ans = max(ans, (right - left + 1) * (algo_cnt - duplicated))
    right += 1

    if right == N:
        break

print(ans)
