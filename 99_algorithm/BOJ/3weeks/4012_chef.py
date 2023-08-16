import sys

sys.stdin = open('input.txt')


def get_cases(idx, lst):
    global N
    if idx == N:
        if len(lst) == N // 2:
            combi.append(lst[:])
        return

    lst.append(idx)
    get_cases(idx + 1, lst)
    lst.pop()
    get_cases(idx + 1, lst)


T = int(input())

for tc in range(3):

    N = int(input())

    foods = [list(map(int, input().split())) for _ in range(N)]

    combi = []

    get_cases(0, [])

    min_gap = int(1e9)
    for c in combi:
        print(c)
    for i in range(len(combi) // 2):
        a = combi[i]
        b = combi[len(combi) - 1 - i]
        sum_of_a = 0
        sum_of_b = 0

        for i in a:
            for j in a:
                if i != j:
                    sum_of_a += foods[i][j]

        for i in b:
            for j in b:
                if i != j:
                    sum_of_b += foods[i][j]

        min_gap = min(min_gap, abs(sum_of_a - sum_of_b))

    print(f'#{tc + 1} {min_gap}')
