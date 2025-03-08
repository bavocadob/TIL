import sys

input = sys.stdin.readline


def solve_case(month, days, dpw):
    mc = 1
    left = days % dpw
    mw = days // dpw + (1 if left else 0)
    arr = [0, mw]

    while left:
        temp = days + left
        mc += 1
        left = temp % dpw
        mw += temp // dpw
        mw += (1 if left else 0)
        arr.append(mw)

    ans = (month // mc) * mw + arr[month % mc]
    return ans


T = int(input())

results = []
for i in range(T):
    m, d, w = map(int, input().split())
    result = solve_case(m, d, w)
    results.append(f"Case #{i + 1}: {result}")

print("\n".join(results))
