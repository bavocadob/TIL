from collections import deque


def solution(number):
    queue = deque([(1, 0)])
    queue2 = deque()

    time = 0

    while queue:
        while queue:
            length, clipboard = queue.popleft()
            # print(length,clipboard)
            if length == number:
                return time
            if 0 < length < number and 0 <= clipboard < number:
                if not visited[length + clipboard][clipboard]:
                    visited[length + clipboard][clipboard] = True
                    queue2.append((length + clipboard, clipboard))
                if not visited[length][length]:
                    visited[length][length] = True
                    queue2.append((length, length))
                if not visited[length - 1][clipboard]:
                    visited[length - 1][clipboard] = True
                    queue2.append((length - 1, clipboard))

        time += 1
        queue = queue2
        queue2 = deque()
        # print(queue)


N = int(input())

visited = [[False] * 1001 for _ in range(2001)]

print(solution(N))
