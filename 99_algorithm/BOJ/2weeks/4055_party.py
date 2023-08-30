# 파티가 좋아
# 아직 못품

day = 1

while True:
    n = int(input())

    if n == 0: break

    party_time = []
    for i in range(n):
        party_time.append(list(map(int, input().split())))

    party_time.sort(key=lambda x: (x[1], x[0]))

    curr_hour = 0

    # print(party_time)

    visited = [0] * 25
    for start, end in party_time:
        if start == end:
            continue

        for i in range(start, end):
            if visited[i] < 2:
                visited[i] += 1
                break

    # print(visited)
    print(f'On day {day} Emma can attend as many as {sum(visited)} parties.')
    day += 1
