import heapq

N = int(input())

A = list(map(int, input().split()))

heapq.heapify(A)

ans = 1
cur = heapq.heappop(A)

while A:
    temp = heapq.heappop(A)

    if cur == temp:
        heapq.heappush(A, temp * 2)
        cur = heapq.heappop(A)

    else:
        cur = temp
        ans += 1

print(ans)
