import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())

    connect_dict = {i: {i} for i in range(N)}

    k = int(input())

    for _ in range(k):
        x, y = map(int, input().split())
        connect_dict[x].update(connect_dict[y])
        temp = connect_dict[min(connect_dict[x])]
        temp.update(connect_dict[x])
        connect_dict[x] = temp
        connect_dict[y] = temp

    print(f'Scenario {tc + 1}:')

    m = int(input())
    # print(connect_dict)
    for _ in range(m):
        x, y = map(int, input().split())
        if connect_dict[x] & connect_dict[y]:
            connect_dict[x].update(connect_dict[y])
            connect_dict[y] = connect_dict[x]
            print(1)
        else:
            print(0)

    connect_dict.clear()

