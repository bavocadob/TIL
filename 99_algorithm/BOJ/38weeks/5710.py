import sys

input = sys.stdin.readline


def usage_to_cost(usage):
    cost = 0
    cost += min(usage, 200) // 2
    usage -= 200
    if usage > 0:
        cost += min(usage, 29700) // 3
        usage -= 29700
        if usage > 0:
            cost += min(usage, 4950000) // 5
            usage -= 4950000
            if usage > 0:
                cost += usage // 7
    return cost


def cost_to_usage(cost):
    usage = 0
    usage += min(cost, 100) * 2
    cost -= 100
    if cost > 0:
        usage += min(cost, 9900) * 3
        cost -= 9900
        if cost > 0:
            usage += min(cost, 990000) * 5
            cost -= 990000
            if cost > 0:
                usage += cost * 7
    return usage


while True:
    total_cost, diff = map(int, input().split())
    if total_cost == 0 and diff == 0:
        break

    total = usage_to_cost(total_cost)
    low, high = 0, total

    while low <= high:
        mid = (low + high) // 2
        u1 = mid
        u2 = total - mid

        c1 = cost_to_usage(u1)
        c2 = cost_to_usage(u2)

        if c2 - c1 == diff:
            print(c1)
            break

        if c2 - c1 > diff:
            low = mid + 1
        else:
            high = mid - 1
