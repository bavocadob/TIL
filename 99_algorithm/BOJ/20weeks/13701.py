from collections import OrderedDict

d = OrderedDict()


A = list(map(int,input().split()))

for a in A:
    d[a] = 1

print(' '.join(map(str, d.keys())))