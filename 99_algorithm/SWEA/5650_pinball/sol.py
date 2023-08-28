# 상 0 하 1 좌 2 우 3
# 1 하 -> 우, 좌 -> 상, 상 -> 하, 우 -> 좌
# 2. 하 -> 상, 우 -> 좌, 상 -> 우, 좌 -> 하
# 3. 하 -> 상, 좌 -> 우, 우-> 하 , 상 -> 좌

# 4. 하 -> 좌, 우 -> 상 ,상- > 하, 좌 -> 우
# 5. 하 -> 상, 상 -> 하, 좌 -> 우, 우->좌
block_dict = {1: {0: 1, 1: 3, 2: 0, 3: 2},
              2: {0: 3, 1: 0, 2: 1, 3: 2},
              3: {0: 2, 1: 0, 2: 3, 3: 1},
              4: {0: 1, 1: 2, 2: 3, 3: 0},
              5: {0: 1, 1: 0, 2: 3, 3: 2}}

T = int(input())

for tc in range(T):
    wormhole = dict()
    N = int(input())

    space = [list(map(int, input().split())) for _ in range(N)]

    wormhole_list = []
    for i in range(N):
        for j in range(N):
            if space[i][j] >= 6:
                pass
