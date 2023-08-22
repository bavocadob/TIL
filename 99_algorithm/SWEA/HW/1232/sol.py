import sys

sys.stdin = open('input.txt')

operator = ['+', '-', '*', '/']

for tc in range(10):
    N = int(input())

    visited = [False] * (N + 1)

    tree = [None] * (N + 1)
    left_node = [0] * (N + 1)
    right_node = [0] * (N + 1)
    parent_node = [0] * (N + 1)
    for _ in range(N):
        temp = input().split()
        tree_index = int(temp[0])
        if len(temp) == 2:
            tree[tree_index] = int(temp[1])
        else:
            tree[tree_index] = temp[1]
            left_node[tree_index] = int(temp[2])
            right_node[tree_index] = int(temp[3])
            parent_node[int(temp[2])] = tree_index
            parent_node[int(temp[3])] = tree_index

    curr = 1
    while True:
        if curr == 0:
            break

        if tree[curr] in operator:
            if tree[left_node[curr]] not in operator and tree[right_node[curr]] not in operator:
                if tree[curr] == '+':
                    tree[curr] = tree[left_node[curr]] + tree[right_node[curr]]
                elif tree[curr] == '-':
                    tree[curr] = tree[left_node[curr]] - tree[right_node[curr]]
                elif tree[curr] == '*':
                    tree[curr] = tree[left_node[curr]] * tree[right_node[curr]]
                elif tree[curr] == '/':
                    tree[curr] = tree[left_node[curr]] / tree[right_node[curr]]
                # 부모 노드로
                curr = parent_node[curr]
            elif tree[left_node[curr]] in operator:
                curr = left_node[curr]
            elif tree[right_node[curr]] in operator:
                curr = right_node[curr]
        else:
            curr = parent_node[curr]

    print(f'#{tc + 1} {int(tree[1])}')
