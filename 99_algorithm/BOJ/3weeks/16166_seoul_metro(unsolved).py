# 주의할 점 역의 번호가 2 ^ 32 -1 까지 주어짐 약 42억(메모리 초과 주의)
# 주의할 점 2. 순환선이 있음 visited만 잘하면 될거 같긴한데 어떻게 방문처리를 할까?
# 간선과 방문처리 모두를 dict로 하면 풀 수 있을까

from collections import deque

# min_transfer = 11
# find = False
#
#
# def solution(depth, cnt, metro_set: set):
#     global min_transfer, find
#     if depth == N:
#         if target in metro_set:
#             find = True
#             min_transfer = min(min_transfer, cnt)
#         return
#
#     if target in metro_set and len(metro_set) > 1:
#         find = True
#         min_transfer = min(min_transfer, cnt)
#         return
#
#     for i in range(N):
#         if not visited[i] and metro_set & metro_line[i]:
#             visited[i] = True
#             new_set = metro_set.copy()
#             new_set.update(metro_line[i])
#             solution(depth + 1, cnt + 1, new_set)
#             visited[i] = False


N = int(input())

metro_line = []

for i in range(N):
    line_len, *line = map(int, input().split())
    metro_line.append(set(line))

target = int(input())

current_metro = {0}
visited = [False] * N

transfer_cnt = 0

for i in range(N):
    new_metro = current_metro.copy()

    for j in range(N):
        if not visited[j] and current_metro & metro_line[j]:
            new_metro.update(metro_line[j])
            visited[j] = True

    current_metro = new_metro
    if target in current_metro:
        break
    transfer_cnt += 1

if target in current_metro:
    print(transfer_cnt)
else:
    print(-1)



# if find:
#     print(min_transfer - 1)
# else:
#     print('-1')
