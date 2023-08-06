# 백준 7507 올림피게임
# 정렬 + 그리디

import sys
input = sys.stdin.readline

for T in range(int(input())):

    N = int(input())

    schedules = [list(map(int, input().split())) for _ in range(N)]


    schedules.sort(key=lambda x: (x[0], x[1]))
    schedules.sort(key=lambda x: (x[0], x[2]))

    count = 1
    days = schedules[0][0]
    curr_time = schedules[0][2]

    for i in range(1, N):
        if days != schedules[i][0]:
            count += 1
            days = schedules[i][0]
            curr_time = schedules[i][2]
        else:
            if curr_time > schedules[i][1]:
                continue
            else:
                curr_time = schedules[i][2]
                count += 1

    print(f'Scenario #{T + 1}:\n{count}\n')

