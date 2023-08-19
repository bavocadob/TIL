import sys
input = sys.stdin.readline

N = int(input())

reports = [list(map(int, input().split())) for _ in range(N)]

reports.sort(key=lambda x: x[1])


curr_day = reports[0][1]
curr_start = reports[0][1] - reports[0][0]
curr_spare = 0

for i in range(1, N):
    curr_spare += (reports[i][1] - curr_day) - reports[i][0]
    curr_day = reports[i][1]

    if curr_spare < 0:
        curr_start += curr_spare
        curr_spare = 0

print(curr_start)
