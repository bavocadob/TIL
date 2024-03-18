from collections import Counter
import math

n, q = map(int, input().split())
V = list(map(int, input().split()))
C = Counter(V)

for _ in range(q):
    o, x = map(int, input().split())
    if o & 1:
        if x == 0:
            print(int(C[0] > 0 and (C[0] > 1 or len(V) - C[0] > 0)))
            continue

        flag = 0
        for i in range(1, int(math.sqrt(x)) + 1):
            if x % i == 0 and x // i < 10001:
                p, q = i, x // i
                if C[p] and C[q]:
                    flag = int(p ^ q != 0 or C[p] > 1)
                    break

        print(flag)
    else:
        C[V[x - 1]] -= 1
        C[0] += 1
        V[x - 1] = 0
