# 주의할 점 역의 번호가 2 ^ 32 -1 까지 주어짐 약 42억(메모리 초과 주의)
# 주의할 점 2. 순환선이 있음 visited만 잘하면 될거 같긴한데 어떻게 방문처리를 할까?
# 간선과 방문처리 모두를 dict로 하면 풀 수 있을까

from collections import deque

N = int(input())

metro = [list(map(int, input().split())) for _ in range(N)]

