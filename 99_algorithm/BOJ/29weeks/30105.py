N = int(input())


A = list(map(int, input().split()))

A_set = set(A)

rst = []


for i in range(1, N):
    gap = A[i] - A[0]

    temp_set = set()

    for num in A:
        if num in temp_set:
            if num + gap in A_set:
                temp_set.add(num + gap)
        else:
            if not num + gap in A_set:
                break

            temp_set.add(num)
            temp_set.add(num + gap)

    if len(temp_set) == N:
        rst.append(gap)

print(len(rst))
print(*rst)
