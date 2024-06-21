import sys

input = sys.stdin.readline


def solve():
    if start_hole and end_hole and cnt4 != cnt1 + 1:
        print(-1)
        return
    if not start_hole and not end_hole and cnt1 != cnt4 + 1:
        print(-1)
        return
    if start_hole ^ end_hole:
        if cnt1 != cnt4:
            print(-1)
            return
        if cnt1 == 0:
            if start_hole and len(left_hole) > 0:
                print(-1)
                return
            if end_hole and len(left_dent) > 0:
                print(-1)
                return

    left_hole.sort()
    left_dent.sort()

    last_change = 0
    need_hole = not start_hole
    hole_iter = iter(left_hole)
    dent_iter = iter(left_dent)
    hole_end = False
    dent_end = False

    while True:
        if need_hole:
            try:
                puzzle_num, puzzle_spec = next(hole_iter)
                if puzzle_spec == 1:
                    need_hole = False
                    last_change = len(result) - 1
                result.append(puzzle_num)
            except StopIteration:
                hole_end = True
        else:
            try:
                puzzle_num, puzzle_spec = next(dent_iter)
                if puzzle_spec == 4:
                    need_hole = True
                    last_change = len(result) - 1
                result.append(puzzle_num)
            except StopIteration:
                dent_end = True

        if hole_end and need_hole:
            break
        if dent_end and not need_hole:
            break

    for i in range(last_change + 1):
        print(result[i], end=" ")
    for a, _ in hole_iter:
        print(a, end=" ")
    for a, _ in dent_iter:
        print(a, end=" ")
    for i in range(last_change + 1, len(result)):
        print(result[i], end=" ")
    print(last)


n = int(input())

start_hole = False
end_hole = False
cnt1 = 0
cnt4 = 0

left_hole = []
left_dent = []
result = []
last = 0

for i in range(n):
    x, a = map(int, input().split())
    if x == 5 or x == 6:
        result.append(a)
    elif x == 7 or x == 8:
        last = a
    if x == 5:
        start_hole = True
    elif x == 7:
        end_hole = True
    elif x == 1:
        cnt1 += 1
    elif x == 4:
        cnt4 += 1
    if x == 1 or x == 2:
        left_hole.append((a, x))
    elif x == 3 or x == 4:
        left_dent.append((a, x))

solve()