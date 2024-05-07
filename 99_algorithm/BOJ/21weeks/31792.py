from collections import OrderedDict

N = int(input())

A = OrderedDict()

for _ in range(N):
    query = list(map(int, input().split()))

    if len(query) > 1:
        if query[0] == 1:
            A[query[1]] = A.setdefault(query[1], 0) + 1
        else:
            A[query[1]] = min(A.setdefault(query[1], 0) - 1, 0)

            if A[query[1]] == 0:
                del A[query[1]]
    elif len(query) == 1:
        for key, val in A.items():
            print(key, val)
