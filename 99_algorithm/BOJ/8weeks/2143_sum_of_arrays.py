from collections import defaultdict

target = int(input())

N = int(input())

arr_a = [0] + list(map(int, input().split()))

M = int(input())

arr_b = [0] + list(map(int, input().split()))


for i in range(1, N + 1):
    arr_a[i] = arr_a[i - 1] + arr_a[i]
for i in range(1, M + 1):
    arr_b[i] = arr_b[i - 1] + arr_b[i]

a_candidate = defaultdict(int)

for i in range(N):
    for j in range(i + 1, N + 1):
        val = arr_a[j] - arr_a[i]
        a_candidate[val] += 1

ans = 0

for i in range(M):
    for j in range(i + 1, M + 1):
        gap = target - (arr_b[j] - arr_b[i])
        ans += a_candidate[gap]

print(ans)

# b_candidate = defaultdict(int)

# for key, value in a_candidate.items():
#     gap = target - key
#     if gap in b_candidate:
#         ans += b_candidate[gap] * value


