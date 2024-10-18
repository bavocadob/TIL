import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    students = []
    for _ in range(M):
        a, b = map(int, input().split())
        students.append((a, b))

    books = [True] * (N + 1)
    students.sort(key=lambda x: (x[1], x[0]))

    ans = 0
    for s, e in students:
        for i in range(s, e + 1, 1):
            if books[i]:
                books[i] = False
                ans += 1
                break
    print(ans)
