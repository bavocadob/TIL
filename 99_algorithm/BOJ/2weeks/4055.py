# 파티가 좋아
# 아직 못품

day = 1

while True:
    n = int(input())

    if n == 0 : break

    party_time = []
    for i in range(n):
        party_time.append(list(map(int, input().split())))

    party_time.sort(key=lambda x: (x[0], x[1]))

    half_of_hour = False
    curr_hour = 0

    cnt = 0
    for party in party_time:
        if party[1] < curr_hour:
            continue

        if party[0] <= curr_hour < party[1]:
            cnt += 1
            if half_of_hour:
                half_of_hour = False
                curr_hour += 1
            else:
                half_of_hour = True
        elif curr_hour < party[0]:
            cnt += 1
            curr_hour = party[0]
            half_of_hour = True

    print(f'On day {day} Emma can attend as many as {cnt} parties.')
    day += 1