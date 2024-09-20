import sys

input = sys.stdin.readline


def build(t, nums, left, right, node):
    if left == right:
        t[node] = nums[left]
        return t[node]

    l_node = node * 2
    r_node = node * 2 + 1

    mid = (left + right) // 2

    t[node] = build(t, nums, left, mid, l_node) * build(t, nums, mid + 1, right, r_node)
    return t[node]


def update(t, idx, val, left, right, node):
    if left == right:
        t[node] = val
        return

    mid = (left + right) // 2

    if left <= idx <= mid:
        update(t, idx, val, left, mid, node * 2)
    else:
        update(t, idx, val, mid + 1, right, node * 2 + 1)

    t[node] = t[node * 2] * t[node * 2 + 1]


def query(t, fm, to, left, right, node):
    if right < fm or left > to:
        return 1

    if left >= fm and right <= to:
        return t[node]

    mid = (left + right) // 2

    return query(t, fm, to, left, mid, node * 2) * query(t, fm, to, mid + 1, right, node * 2 + 1)


while True:
    try:
        N, K = map(int, input().split())

        numbers = [0]
        for char in input().split():

            temp = int(char)
            if temp > 0:
                numbers.append(1)
            elif temp < 0:
                numbers.append(-1)
            else:
                numbers.append(0)

        tree = [1] * (N * 4)

        build(tree, numbers, 0, N, 1)

        for _ in range(K):
            cmd, a, b = input().split()
            a, b = int(a), int(b)
            if cmd == 'C':
                if b > 0:
                    b = 1
                elif b < 0:
                    b = -1
                update(tree, a, b, 0, N, 1)
            else:
                temp = query(tree, a, b, 0, N, 1)

                if temp > 0:
                    sys.stdout.write('+')
                elif temp < 0:
                    sys.stdout.write('-')
                else:
                    sys.stdout.write('0')
        print()
    except:
        break
