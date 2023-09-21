'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


def prim(start):
    visited = [0] * (V + 1)
    visited[start] = 1
    # 가중치 누적값
    result = 0

    # heap 사용하지 않는다 -> 모든 정점 조사
    for _ in range(1, V):
        # 다음 조사 대상
        next = 0
        # 가중치 비교 대상
        min_val = int(1e9)
        for i in range(V + 1):
            if visited[i] == 1:
                for j in range(V + 1):
                    # 한번 방문한 적 있었던 i의 인접노드 j
                    # 인접행렬을 진출 가능한 노드에 대해서만 가중치를 기록
                    if arr[i][j] > 0 and not visited[j] and min_val > arr[i][j]:
                        next = j
                        min_val = arr[i][j]

        result += min_val
        visited[next] = 1

    return result


# 노드 간선
V, E = map(int, input().split())

arr = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    # 진출 진입 가중치
    S, E, W = map(int, input().split())
    arr[S][E] = W
    arr[E][S] = W

print(prim(0))