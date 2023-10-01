import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def get_min_a_to_b():
    for i in range(1, 101):
        if a_to_b_dict[i]:
            return (i, min(a_to_b_dict[i]) + 1)


def get_min_b_to_c():
    for i in range(1, 101):
        if b_to_c_dict[i]:
            return (i, min(b_to_c_dict[i]) + N + 1)


def a_to_b_modify(index, value):
    global a_to_b_idx, a_to_b_min
    prev_val = a_to_b[index]
    a_to_b_dict[prev_val].remove(index)
    a_to_b_dict[value].add(index)
    a_to_b[index] = value

    if index + 1 == a_to_b_idx:
        if value <= a_to_b_min:
            a_to_b_min = value
        else:
            a_to_b_min, a_to_b_idx = get_min_a_to_b()
    else:
        if value == a_to_b_min and index + 1 < a_to_b_idx:
            a_to_b_idx = index + 1
        elif value < a_to_b_min:
            a_to_b_min = value
            a_to_b_idx = index + 1


def b_to_c_modify(index, value):
    global b_to_c_idx, b_to_c_min
    prev_val = b_to_c[index]
    b_to_c_dict[prev_val].remove(index)
    b_to_c_dict[value].add(index)
    b_to_c[index] = value

    if index + N + 1 == b_to_c_idx:
        if value <= b_to_c_min:
            b_to_c_min = value
        else:
            b_to_c_min, b_to_c_idx = get_min_b_to_c()
    else:
        if value == b_to_c_min and index + N + 1 < b_to_c_idx:
            b_to_c_idx = index + N + 1
        elif value < b_to_c_min:
            b_to_c_min = value
            b_to_c_idx = index + N + 1


a_to_b = list(map(int, input().split()))
b_to_c = list(map(int, input().split()))

a_to_b_dict = {i: set() for i in range(1, 101)}
b_to_c_dict = {i: set() for i in range(1, 101)}

for i in range(N):
    a_to_b_dict[a_to_b[i]].add(i)

for i in range(M):
    b_to_c_dict[b_to_c[i]].add(i)

a_to_b_min, a_to_b_idx = get_min_a_to_b()
b_to_c_min, b_to_c_idx = get_min_b_to_c()

K = int(input())
for _ in range(K):
    command = input().rstrip()
    if command == 'L':
        print(a_to_b_idx, b_to_c_idx)
    else:
        command = command.split()
        idx = int(command[1])
        val = int(command[2])
        if idx <= N:
            a_to_b_modify(idx - 1, val)
        else:
            b_to_c_modify(idx - N - 1, val)
