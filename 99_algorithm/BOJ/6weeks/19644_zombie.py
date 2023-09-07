import sys

input = sys.stdin.readline

L = int(input())

# 사거리 , 데미지
r, damage = map(int, input().split())

# 지뢰
c = int(input())

prefix_sum = [0] * (L + 1)

# 사거리가 6이라 했을때
# 3 3 3 3 3 3 상태에서 3번 폭탄 터뜨리면
# 3 3 3 0 0 0이 되는데 이때 3번 격발하면 앞에 셋은 순서대로 4 , 5, 6의 데미지로 죽고
# 뒤의 셋은 앞에 다가왔을때 다시 3부터 시작해야함


for i in range(1, L + 1):
    zombie = int(input())
    curr_damage = prefix_sum[i - 1] - prefix_sum[max(0, i - r)]
    if curr_damage + damage >= zombie:
        prefix_sum[i] = prefix_sum[i - 1] + damage
    else:
        c -= 1
        if c < 0:
            print('NO')
            break
        prefix_sum[i] = prefix_sum[i - 1]
else:
    print('YES')