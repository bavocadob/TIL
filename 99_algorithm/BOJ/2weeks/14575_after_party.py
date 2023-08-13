# 뒤풀이
# 될 수 있는 것 중에 가장 작은 값을 찾아야함
def calc(limit):
    alc = 0
    for i in range(N):
        alc += max(min(limit, max_list[i]), min_list[i])
    return alc


N, target = map(int, input().split())

min_list = []
max_list = []

for _ in range(N):
    x, y = map(int, input().split())
    min_list.append(x)
    max_list.append(y)

left = max(min_list)
right = max(max_list)

if sum(min_list) > target or sum(max_list) < target:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        sum_of_alc = calc(mid)
        # print('한계가', mid,'라면', sum_of_alc,'만큼')
        if sum_of_alc < target:
            left = mid + 1
        else:
            right = mid - 1
    print(left)