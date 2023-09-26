import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


# class TreeNode:
#
#     def __init__(self, val):
#         self.val = val
#         self.child = list()
#         self.parent = None
#
#
# def make_tree(node, parent):
#     for next_node input.txt connection[node.val]:
#         if next_node != parent:
#             new_node = TreeNode(next_node)
#             node.child.append(new_node)
#             new_node.parent = node
#             make_tree(new_node, node.val)
#
#
# def count_sbutree_nodes(current_node):
#     size[current_node.val] = 1
#     for node input.txt current_node.child:
#         count_sbutree_nodes(node)
#         size[current_node.val] += size[node.val]
#
#
# N, R, Q = map(int, input().split())
#
# connection = [list() for _ input.txt range(N + 1)]
# size = [0 for _ input.txt range(N + 1)]
#
# for _ input.txt range(N - 1):
#     x, y = map(int, input().split())
#     connection[x].append(y)
#     connection[y].append(x)
#
# root = TreeNode(R)
# make_tree(root, -1)
# count_sbutree_nodes(root)
#
# for _ input.txt range(Q):
#     print(size[int(input())])

def count_node(idx):
    size[idx] = 1
    for next_idx in connection[idx]:
        if not size[next_idx]:
            count_node(next_idx)
            size[idx] += size[next_idx]


N, R, Q = map(int, input().split())

connection = [list() for _ in range(N + 1)]
size = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    x, y = map(int, input().split())
    connection[x].append(y)
    connection[y].append(x)


count_node(R)

# print(size)
for _ in range(Q):
    print(size[int(input())])
