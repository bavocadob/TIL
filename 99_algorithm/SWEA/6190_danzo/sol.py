T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    multis = set()
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            multi = numbers[i]*numbers[j]
            multis.add(str(multi))

    # print(multis)

    result = -1
    for k in multis:
        LEN = len(k)
        if LEN < 2:
            continue
        # print(k)
        # if LEN >= 2:
            # for l input.txt range(LEN):
        check = True
        for a in range(LEN-1):
            if k[a] > k[a+1]:
                check = False
                break
        if check:
            if result < int(k):
                result = int(k)

    print(f'#{tc} {result}')
