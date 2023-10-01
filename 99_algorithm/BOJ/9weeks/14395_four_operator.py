from collections import deque

S, T = map(int, input().split())

if S == T:
    print('0')
else:

    visited = {S}

    queue = deque()
    queue.append((S, ''))
    # queue.append((1, '/'))

    while queue:
        curr, s = queue.popleft()
        if curr == T:
            print(s)
            break

        if 1 <= curr ** 2 <= int(1e9) and curr ** 2 not in visited:
            visited.add(curr ** 2)
            queue.append((curr ** 2, s + '*'))

        if 1 <= curr * 2 <= int(1e9) and curr * 2 not in visited:
            visited.add(curr * 2)
            queue.append((curr * 2, s + '+'))

        if 1 <= curr // curr <= int(1e9) and curr // curr not in visited:
            visited.add(curr // curr)
            queue.append((curr // curr, s + '/'))
    else:
        print(-1)
