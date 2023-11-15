import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())

cards = [True] * (N * 4 + 1)

for _ in range(M):
    a, b = map(int, input().split())
    cards[a] = cards[b] = False

my_a, my_b = map(int, input().split())
cards[my_a] = cards[my_b] = False

my_score = abs(my_b % K - my_a % K)

scores = []

for i in range(1, N * 4 + 1):
    if cards[i]:
        scores.append(i % K)

scores.sort()

left = 0
right = len(scores) // 2
ans = 0
while right < len(scores) and ans < M - 1:
    if scores[right] - scores[left] > my_score:
        ans += 1
        right += 1
        left += 1
    else:
        right += 1

print(ans)
