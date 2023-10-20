def solution(curr_idx):
    shark_map = []

    return 0



N, M, S = map(int, input().split())

sharks = set()
for _ in range(S):
    r, c, s, d, z = map(int, input().split())

    sharks.add((r, c, s, d, z))

my_idx = 0

ans = 0
while my_idx <= N:
    my_idx += 1
    ans += solution(my_idx)

print(ans)
