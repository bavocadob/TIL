import sys
# from collections import deque

# input = sys.stdin.readline
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())

    students = []

    for _ in range(N):
        temp = list(map(int , input().split()))
        x = (min(temp) - 1) // 2
        y = (max(temp) - 1) // 2
        students.append((x, y))

    students.sort()
    # print(students)
    cnt = 0

    while students:
        x, y = students.pop(0) # 제일 앞방 출발
        index = 0
        while index < len(students):
            xx, yy = students[index]
            if y < xx:  # n번째 학생이 n+1번째 학생을 안만나면 n + 1번째 학생을 다시 출발시킴
                y = yy
                students.pop(index)
                index -= 1
            index += 1
        cnt += 1

    print(f'#{tc + 1} {cnt}')
