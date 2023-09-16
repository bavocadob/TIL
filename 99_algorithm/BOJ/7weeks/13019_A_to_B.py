A = input()
B = input()


if sorted(list(A)) != sorted(list(B)):
    print(-1)
else:
    a_idx = b_idx = len(A) - 1
    cnt = 0
    while a_idx >= 0 and b_idx >= 0:
        if A[a_idx] == B[b_idx]:
            a_idx -= 1
            b_idx -= 1
        else:
            a_idx -= 1
            cnt += 1

    print(cnt)
