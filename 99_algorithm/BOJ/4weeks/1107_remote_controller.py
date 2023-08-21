N = int(input())

min_cnt = abs(100 - N)
ch_len = len(str(N))

M = int(input())

if M == 10:
    input()
    print(min_cnt)
elif M == 0:
    print(min(min_cnt, ch_len))
else:
    broken = list(map(int, input().split()))
    button = [True] * 10
    for b in broken:
        button[b] = False

    for i in range(1000000):
        valid = True
        str_val = str(i)
        for char in str(i):
            if not button[int(char)]:
                valid = False
                break
        if valid:
            min_cnt = min(min_cnt, abs(i - N) + len(str_val))

    print(min_cnt)
