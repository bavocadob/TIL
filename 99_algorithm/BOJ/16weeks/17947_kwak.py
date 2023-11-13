import sys

input = sys.stdin.readline
N, M, K = map(int, input().rstrip().split())

cards = {i for i in range(1, N * 4 + 1)}

for _ in range(N):
    a, b = map(int, input().rstrip().split())
    cards.discard(a)
    cards.discard(b)

my_a, my_b = map(int, input().rstrip().split())
cards.discard(my_a)
cards.discard(my_b)

my_score = abs(my_b % K - my_a % K)

scores = []

for i in cards:
    scores.append(i % K)

scores.sort()

left = 0
right = len(scores) // 2
ans = 0
while right < len(scores):
    if scores[right] - scores[left] > my_score:
        ans += 1
        right += 1
        left += 1
    else:
        right += 1

print(ans)
