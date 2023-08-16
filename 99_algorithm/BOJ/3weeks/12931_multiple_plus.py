N = int(input())

target = [0] * N

arr = list(map(int, input().split()))

cnt = 0

while arr != target:
    half = True
    for i in range(N):
        if arr[i] % 2 != 0:
            half = False
            break

    if half:
        for i in range(N):
            arr[i] = arr[i] >> 1
    else:
        for i in range(N):
            if arr[i] > 0 and arr[i] % 2 == 1:
                arr[i] -= 1
                break
    cnt += 1


print(cnt)