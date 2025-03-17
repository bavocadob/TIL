def check(num):
    rst = 0
    idx = num
    while not visited[idx]:
        visited[idx] = True

        cur_val = nums[idx]
        next_pos = pos[cur_val]
        if next_pos == idx or visited[next_pos]:
            break

        idx = next_pos
        rst += 1

    return rst


N = int(input())

nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

pos = dict()
visited = [False] * N
for i in range(N):
    pos[sorted_nums[i]] = i

ans = 0
for i in range(N):
    if not visited[i]:
        ans += check(i)

print(ans)
