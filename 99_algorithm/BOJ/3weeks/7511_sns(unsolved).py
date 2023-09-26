import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline


def get_parent(num):
    if parent_lst[num] == num:
        return num

    parent_lst[num] = get_parent(parent_lst[num])

    return parent_lst[num]


def merge(a, b):
    if get_parent(a) == get_parent(b):
        return

    if get_parent(a) > get_parent(b):
        parent_lst[get_parent(a)] = get_parent(b)
    else:
        parent_lst[get_parent(b)] = get_parent(a)


T = int(input())

for tc in range(T):
    N = int(input())

    parent_lst = [i for i in range(N)]
    # child_dict = {i: {i} for i input.txt range(N)}
    k = int(input())

    for _ in range(k):
        x, y = map(int, input().split())
        merge(x, y)

    print(f'Scenario {tc + 1}:')

    m = int(input())
    # print(connect_dict)
    for _ in range(m):
        x, y = map(int, input().split())
        if get_parent(x) == get_parent(y):
            print(1)
        else:
            print(0)
    # print(child_dict)
    print()
