import sys

from collections import deque

input = sys.stdin.readline


def add_item(item_name):
    global item_idx
    if item_name not in item_to_idx:
        item_to_idx[item_name] = item_idx
        idx_to_item[item_idx] = item_name
        item_idx += 1


N = int(input())
item_to_idx = dict()
idx_to_item = dict()

connection = [list() for _ in range(N * 2)]
parent = [0] * (N * 2)

item_idx = 0

for _ in range(N):
    p, c = input().split()
    add_item(p)
    add_item(c)
    connection[item_to_idx[p]].append(item_to_idx[c])
    parent[item_to_idx[c]] += 1

queue = deque()
queue2 = deque()
ans = []
result_list = []

for i in range(item_idx):
    if not parent[i]:
        result_list.append(idx_to_item[i])
        queue.append(i)

if queue:
    result_list.sort()
    ans.extend(result_list)
    result_list.clear()

    while queue:
        while queue:
            curr = queue.popleft()
            for next_idx in connection[curr]:
                parent[next_idx] -= 1
                if not parent[next_idx]:
                    queue2.append(next_idx)
                    result_list.append(idx_to_item[next_idx])
        queue = queue2
        queue2 = deque()
        result_list.sort()
        ans.extend(result_list)
        result_list.clear()

    if sum(parent) == 0:
        print('\n'.join(ans))
    else:
        print(-1)

else:
    print(-1)
