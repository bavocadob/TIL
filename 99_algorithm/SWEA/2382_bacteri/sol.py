import sys

sys.stdin = open('input.txt')

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(T):

    N, M, K = map(int, input().split())

    community = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        remove_list = []
        # 군집 하나씩 이동 시키기
        for i in range(len(community)):
            community[i][0], community[i][1] = community[i][0] + dx[community[i][3] - 1], community[i][1] + dy[
                community[i][3] - 1]
            
            # 벽에 닿았을 때
            if community[i][0] in [0, N - 1] or community[i][1] in [0, N - 1]:
                # 개체수 감소
                community[i][2] //= 2
                # 방향전환
                if community[i][3] % 2:
                    community[i][3] += 1
                else:
                    community[i][3] -= 1
                # 0마리면 군집 제거
                if community[i][2] == 0:
                    remove_list.append(community[i])
        # 정렬(같은 군집찾기위해)
        community.sort()
        
        # 같은 군집일 경우 큰 군집에 합치고 작은 군집 제거리스트에 담기(정렬시 뒤에 군집이 더큼)
        for i in range(len(community) - 1):
            if community[i][0] == community[i + 1][0] and community[i][1] == community[i + 1][1]:
                community[i + 1][2] += community[i][2]
                remove_list.append(community[i])
        
        # 삭제할 군집 제거
        for i in range(len(remove_list)):
            community.remove(remove_list[i])

    result = 0
    # 남은 군집의 군집 수 합산
    for i in range(len(community)):
        result += community[i][2]

    # for c input.txt community:
    #     print(c)

    print(f'#{tc + 1} {result}')

