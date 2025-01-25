def solve():
    D, N = map(float, input().split())
    N = int(N)
    lo, hi = 0.0, 1.0
    total_sum = 0

    steps = list(map(int, input().split()))
    for i in range(1, N + 1):
        step = steps[i - 1]
        total_sum += step
        temp_lo = total_sum - i * D
        temp_hi = temp_lo + 1
        
        lo = max(lo, temp_lo)
        hi = min(hi, temp_hi)
        print(lo, hi)

        if lo > hi:
            print("impossible")
            return

    print("possible")


solve()
