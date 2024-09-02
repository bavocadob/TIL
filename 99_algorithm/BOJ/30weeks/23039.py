def check(exc):
    for x1, x2 in check_dict.keys():
        for y1, y2 in check_dict[(x1, x2)]:
            if exc in [x1, x2, y1, y2]:
                continue

            if (x1, x2) in adj and (y1, y2) in adj:
                return False

    return True


def solve():
    if len(adj) == 10:
        return -1

    if check(0):
        return 0

    for i in range(1, 6):
        if check(i):
            return 1

    return 2


check_dict = {(1, 3): [(2, 4), (2, 5)], (2, 4): [(3, 5), (1, 3)], (3, 5): [(2, 4), (1, 4)], (1, 4): [(2, 5), (3, 5)]}

adj = set()

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a

    adj.add((a, b))

print(solve())