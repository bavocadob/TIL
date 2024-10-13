N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


def get_pos(nums):
    pos = [list() for _ in range(2)]

    for i in range(N):
        pos[nums[i]].append(i)

    return pos


base_pos = get_pos(A)


def solve(start):
    temp = []
    for length in B:
        temp += [start] * length
        start = (start + 1) % 2

    temp_pos = get_pos(temp)
    if len(temp_pos[0]) != len(base_pos[0]) or len(temp_pos[1]) != len(base_pos[1]):
        return int(1e9)

    ans = 0
    for i in range(2):
        for j in range(len(temp_pos[i])):
            ans += abs(temp_pos[i][j] - base_pos[i][j])

    return ans // 2


print(min(solve(0), solve(1)))
