import sys

input = sys.stdin.readline


class Class:

    def __init__(self, credit, day, start, end):
        self.credit = credit
        self.day = day
        self.start = start
        self.end = end


def backtrack(group_idx, total_credit, class_list):
    global ans

    if total_credit == 22:
        ans += 1
        return

    if group_idx == N:
        return

    for next_class in group[group_idx]:
        if total_credit + next_class.credit > 22:
            continue

        is_valid = True
        for current_class in class_list:
            if current_class.day != next_class.day:
                continue

            if not (next_class.start >= current_class.end or next_class.end <= current_class.start):
                is_valid = False
        if not is_valid:
            continue

        class_list.append(next_class)
        backtrack(group_idx + 1, total_credit + next_class.credit, class_list)
        class_list.pop()

    backtrack(group_idx + 1, total_credit, class_list)


N = int(input())

group = [list() for _ in range(N)]

ans = 0

for i in range(N):
    size = int(input())

    for _ in range(size):
        c, d, s, e = input().split()
        c = int(c)
        d = int(d)

        s = int(''.join(s.split(':')))
        e = int(''.join(e.split(':')))

        group[i].append(Class(c, d, s, e))

backtrack(0, 0, [])
print(ans)
