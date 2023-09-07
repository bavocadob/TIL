import sys
input = sys.stdin.readline

N, H = map(int, input().split())

# 홀수 석순(밑에서) 짝수 종유석(위에서)

# 석순 카운트
stalagmite = [0] * (H + 1)
# 종유석 카운트
stalactite = [0] * (H + 1)

for i in range(N):
    height = int(input())
    if i % 2:
        stalactite[H - height + 1] += 1
    else:
        stalagmite[height] += 1

for i in range(1, H + 1):
    stalagmite[H - i] += stalagmite[H - i + 1]
    stalactite[i] += stalactite[i - 1]

result = float('inf')
cnt = 0
for h in range(1, H + 1):
    temp = stalagmite[h] + stalactite[h]
    if temp < result:
        result = temp
        cnt = 1
    elif temp == result:
        cnt += 1

print(result, cnt)
