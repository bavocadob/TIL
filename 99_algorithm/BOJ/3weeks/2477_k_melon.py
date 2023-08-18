K = int(input())

field = []
melon_nswe = []
cnt = [0] * 5
for i in range(6):
    nswe, distance = map(int, input().split())
    field.append(distance)
    melon_nswe.append(nswe)
    cnt[nswe] += 1

a_target = cnt.index(1)
b_target = cnt.index(1, a_target + 1)

a = melon_nswe.index(a_target)
b = melon_nswe.index(b_target)

print((field[a] * field[b] - field[(a+3)%6] * field[(b+3)%6]) * K)
