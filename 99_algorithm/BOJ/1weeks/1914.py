

def solution(depth, start, end):
    if depth == 1:
        print(start, end)
        return

    solution(depth - 1, start, 6 - start - end)
    print(start, end)
    solution(depth - 1, 6 - start - end, end)


N = int(input())

print(2 ** N - 1)
if N <= 20:
    solution(N, 1, 3)