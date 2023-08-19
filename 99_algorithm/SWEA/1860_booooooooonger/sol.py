import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for tc in range(T):
#     N, time, k = map(int, input().split())
#
#     times = list(map(int, input().split()))
#     times.sort(reverse=True)
#
#     booonger = k
#     seconds = time
#     booonger_time = 0
#     possible = True
#
#     while times:
#         customer = times.pop()
#         if customer < seconds:
#             possible = False
#             break
#         else:
#             booonger_time += customer - seconds
#             booonger += (booonger_time // time) * k
#             booonger_time %= time
#             seconds = customer
#
#             if booonger <= 0:
#                 possible = False
#                 break
#
#             booonger -= 1
#
#     if possible:
#         print(f'#{tc + 1} Possible')
#     else:
#         print(f'#{tc + 1} Impossible')
#

T = int(input())
res = []


for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    visit = list(map(int, input().split()))
    visit = sorted(visit)
    check = 0

    for i in range(N):
        bread = (visit[i] // M) * K - (i + 1)
        if bread < 0:
            check = 1
            res.append('Impossible')
            break

    if not check:
        res.append('Possible')

for tc in range(1, T + 1):
    print(f'#{tc} {res[tc - 1]}')