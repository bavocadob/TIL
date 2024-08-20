import sys
from functools import cmp_to_key

input = sys.stdin.readline


class Customer:
    def __init__(self, time, weight):
        self.time = time
        self.weight = weight


def compare_to(a, b):
    if a.weight * (2 * b.time + 1) > b.weight * (2 * a.time + 1):
        return -1
    elif a.weight * (2 * b.time + 1) < b.weight * (2 * a.time + 1):
        return 1
    else:
        return 0


N = int(input())

customers = []
for _ in range(N):
    t, w = map(int, input().split())
    customers.append(Customer(t, w))

customers.sort(key=cmp_to_key(compare_to))

ans = 0
cnt = 0
curr_time = 0

for customer in customers:
    curr_time += customer.time
    ans += customer.weight * (curr_time + cnt)
    curr_time += customer.time
    cnt += 1

print(ans)
