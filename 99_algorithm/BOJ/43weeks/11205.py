def can_move_cows(m, l, M, L, tm, tl):
    def move_crane(start, target):
        return abs(start - target)

    def case1():
        time = 0
        crane = 0

        time += move_crane(crane, m)
        crane = m
        time += move_crane(crane, M)
        crane = M
        if time > tm:
            return float('inf')

        time += move_crane(crane, l)
        crane = l
        time += move_crane(crane, L)
        crane = L
        if time > tl:
            return float('inf')

        return time

    def case2():
        time = 0
        crane = 0

        time += move_crane(crane, l)
        crane = l
        time += move_crane(crane, m)
        crane = m

        time += move_crane(crane, M)
        crane = M
        if time > tm:
            return float('inf')

        time += move_crane(crane, m)
        crane = m
        time += move_crane(crane, L)
        crane = L
        if time > tl:
            return float('inf')

        return time

    def case3():
        time = 0
        crane = 0

        time += move_crane(crane, l)
        crane = l
        time += move_crane(crane, L)
        crane = L
        if time > tl:
            return float('inf')

        time += move_crane(crane, m)
        crane = m
        time += move_crane(crane, M)
        crane = M
        if time > tm:
            return float('inf')

        return time

    def case4():
        time = 0
        crane = 0

        time += move_crane(crane, m)
        crane = m
        time += move_crane(crane, l)
        crane = l

        time += move_crane(crane, L)
        crane = L
        if time > tl:
            return float('inf')

        time += move_crane(crane, l)
        crane = l
        time += move_crane(crane, M)
        crane = M
        if time > tm:
            return float('inf')

        return time

    result = min(case1(), case2(), case3(), case4())
    return "possible" if result != float('inf') else "impossible"


m, l = map(int, input().split())
M, L = map(int, input().split())
tm, tl = map(int, input().split())

print(can_move_cows(m, l, M, L, tm, tl))
