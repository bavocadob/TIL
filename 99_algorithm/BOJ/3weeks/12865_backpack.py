# 7

# N, K = map(int, input().split())
#
# dp = [0] * (K + 1)
#
# values = [list(map(int, input().split())) for _ in range(N)]
#
# for weight, value in values:
#     for i in range(K, weight - 1, -1):
#         dp[i] = max(dp[i], dp[i - weight] + value)
#
# print(max(dp))


# 향상된 DP 풀이
# def main():
#     n, k = map(int, input().split())
#     k += 1
#
#     bag = {0: 0}
#     data = [tuple(map(int, input().split())) for _ in range(n)]
#     data.sort(reverse=True)
#
#     for w, v in data:
#         tmp = {}
#         for v_bag, w_bag in bag.items():
#             if bag.get(nv := v + v_bag, k) > (nw := w + w_bag):
#                 tmp[nv] = nw
#
#         print(tmp)
#         print('가방', bag)
#         bag.update(tmp)
#
#     print(max(bag.keys()))
#
#
# main()

# DP 풀이
n, k = map(int, input().split())
bag = [[0 for _ in range(k+1)] for _ in range(n+1)]

for ni in range(1, n+1):
    w, v = map(int, input().split())
    for wi in range(1, k+1):
        if w > wi:
            bag[ni][wi] = bag[ni-1][wi]
        else:
            bag[ni][wi] = max(bag[ni-1][wi-w]+v, bag[ni-1][wi])

for row in bag:
    print(row)
print(bag[-1][-1])