import sys

input = sys.stdin.readline


def solution(depth, arr):
    global max_sum

    if depth == 11:
        temp_sum = 0
        for i in range(11):
            x, y = arr[i]
            temp_sum += player_status[x][y]

        max_sum = max(temp_sum, max_sum)
        return

    for i in range(11):
        if player_status[depth][i] == 0 or position_visited[i]:
            continue

        position_visited[i] = True
        arr.append((depth, i))

        solution(depth + 1, arr)

        position_visited[i] = False
        arr.pop()


T = int(input())

for _ in range(T):
    max_sum = 0
    position_visited = [False] * 11
    player_status = [list(map(int, input().split())) for _ in range(11)]
    solution(0, [])
    print(max_sum)
