# 주의할 점 역의 번호가 2 ^ 32 -1 까지 주어짐 약 42억(메모리 초과 주의)
# 주의할 점 2. 순환선이 있음 visited만 잘하면 될거 같긴한데 어떻게 방문처리를 할까?
# 간선과 방문처리 모두를 dict로 하면 풀 수 있을까

from collections import deque

N = int(input())

metro = [list(map(int, input().split())) for _ in range(N)]

target = int(input())

visited = dict()
metro_line = dict()

for index, m in enumerate(metro):
    for i in range(1, len(m)):
        if m[i] not in metro_line:
            metro_line[m[i]] = [index]

        if i > 1:
            metro_line[m[i]].append(m[i - 1])
        if i < len(m) - 1:
            metro_line[m[i]].append(m[i + 1])

queue = deque([0])
visited[0] = 0  # 환승횟수

while queue:
    curr_line = queue.pop()
    for i in range(1, len(metro_line[curr_line])):
        if metro_line[curr_line][i] not in visited:
            queue.append(metro_line[curr_line][i])
            if metro_line[metro_line[curr_line][i]][0] == metro_line[curr_line][0]:
                visited[metro_line[curr_line][i]] = visited[curr_line]
            else:
                visited[metro_line[curr_line][i]] = visited[curr_line] + 1
        else:

            if metro_line[metro_line[curr_line][i]][0] == metro_line[curr_line][0]:
                visited[metro_line[curr_line][i]] = min(visited[curr_line], visited[metro_line[curr_line][i]])

if target in visited:
    result = 10
    for m in metro:
        print(m)
        if target in m:
            for mm in m:
                result = min(result, visited[mm])

    print(result)
else:
    print(-1)

print(visited)
