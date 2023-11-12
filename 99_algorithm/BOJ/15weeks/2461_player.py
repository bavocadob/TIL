import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')

queue = []
max_ability = 0
for i in range(N):
    A[i].sort()
    heapq.heappush(queue, (A[i][0], i, 0))  # 각 첫번째 학생과 반 번호와 순서 기입
    max_ability = max(max_ability, A[i][0])

while True:
    min_ability, class_num, class_idx = heapq.heappop(queue)
    ans = min(ans, max_ability - min_ability)

    if class_idx == M - 1:
        break
    next_ability = A[class_num][class_idx + 1]
    max_ability = max(max_ability, next_ability)

    heapq.heappush(queue, (next_ability, class_num, class_idx + 1))

print(ans)
