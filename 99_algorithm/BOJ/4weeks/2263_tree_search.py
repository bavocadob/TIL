import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(node):
    print(node.val, end=' ')
    if node.left is not None:
        preorder(node.left)
    if node.right is not None:
        preorder(node.right)


def solution(in_l, in_r, po_l, po_r):
    if (in_l > in_r) or (po_l > po_r):
        return None

    node = Node(postorder[po_r])

    root_index = inorder_index_lst[postorder[po_r]]
    left_length = root_index - in_l

    node.left = solution(in_l, root_index - 1, po_l, po_l + left_length - 1)
    node.right = solution(root_index + 1, in_r, po_l + left_length, po_r - 1)

    return node


N = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_index_lst = [-1] * (N + 1)
for i in range(N):
    inorder_index_lst[inorder[i]] = i

# root = Node(postorder[-1])
root = solution(0, N - 1, 0, N - 1)
preorder(root)
