from collections import defaultdict

N = int(input())

numbers = list(map(int, input().split()))
visited = defaultdict(bool)

left = right = 0

ans = 0
while left < N and right < N:
    if not visited[numbers[right]]:
        visited[numbers[right]] = True
        right += 1
        ans += right - left
    else:
        visited[numbers[left]] = False
        left += 1

print(ans)
