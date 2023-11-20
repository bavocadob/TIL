def solution():
    combo = 0
    skills = [0] * K
    ans = 0
    tired = 0

    for _ in range(N):
        magic = int(input())
        if magic == 0:
            tired = max(tired - R, 0)
            combo = 0
            continue

        magic -= 1
        ans += int(bases[magic] * (1 + ((combo * C) / 100)) * (1 + ((skills[magic] * mastery[magic]) / 100)))
        tired += cost[magic]
        if tired > 100:
            return -1

        combo += 1
        skills[magic] += 1

    return ans


N, K, C, R = map(int, input().split())

bases = list(map(int, input().split()))
mastery = list(map(int, input().split()))
cost = list(map(int, input().split()))
print(solution())
