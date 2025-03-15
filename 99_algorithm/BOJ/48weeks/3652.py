def solve(num, denum):
    path = []

    while num != denum:
        if num > denum:
            path.append('R')
            num -= denum
            num, denum = denum, num
        else:
            path.append('L')
            denum -= num
            num, denum = denum, num

    print(''.join(path))


# 입력 받기
num, denum = map(int, input().split('/'))
solve(num, denum)
