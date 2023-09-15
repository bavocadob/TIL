import sys

input = sys.stdin.readline

N, W = map(int, input().split())

user = [[-9999, 0, 0, 0, 0, 'default']]

for _ in range(N):
    user_name = input().rstrip()
    streak = [list(input()) for _ in range(7)]
    curr_length = 0
    record_length = 0

    curr_freeze = 0
    record_freeze = 0
    temp_freeze = 0

    curr_week = 0
    curr_day = 0

    record_week = 0
    record_day = 0

    fail_cnt = 0

    consecutive = False
    last = 'X'

    for j in range(W):
        for i in range(7):
            status = streak[i][j]
            if status == 'X':
                fail_cnt += 1
                if consecutive:
                    consecutive = False
                    if curr_length > record_length:
                        record_length = curr_length
                        record_freeze = curr_freeze
                        record_day = curr_day
                        record_week = curr_week
                    elif curr_length == record_length:
                        if record_freeze > curr_freeze:
                            record_freeze = curr_freeze
                            record_day = curr_day
                            record_week = curr_week
            elif status == 'O':
                if consecutive:
                    curr_length += 1
                    curr_freeze += temp_freeze
                    temp_freeze = 0
                else:
                    consecutive = True
                    curr_length = 1
                    curr_freeze = 0
                    temp_freeze = 0
                    curr_week = j
                    curr_day = i
            elif status == 'F':
                if consecutive:
                    temp_freeze += 1

            last = status

    if curr_length > record_length:
        record_length = curr_length
        record_freeze = curr_freeze
        record_day = curr_day
        record_week = curr_week
    elif curr_length == record_length:
        if record_freeze > curr_freeze:
            record_freeze = curr_freeze
            record_day = curr_day
            record_week = curr_week

    user.append([-record_length, record_freeze, record_week, record_day, fail_cnt, user_name])

user.sort()
# print(user)

rank = 0
for i in range(1, N + 1):
    if user[i][:5] != user[i - 1][:5]:
        rank += 1
    print(f'{rank}. {user[i][-1]}')
