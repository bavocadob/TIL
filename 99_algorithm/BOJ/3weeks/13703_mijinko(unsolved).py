# 미해결


def solution(height, time):
    if height < time:
        return 2 ** time

    result = solution(height - 1, time - 1)



centimeter, left_time = map(int,input().split())


print(solution(centimeter, left_time))