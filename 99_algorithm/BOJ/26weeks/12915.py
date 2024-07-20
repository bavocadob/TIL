e, em, m, mh, h = map(int, input().split())
res = 0

while True:
    easy, medium, hard = False, False, False

    if e > 0:
        e -= 1
        easy = True
    elif em > 0:
        em -= 1
        easy = True

    if m > 0:
        m -= 1
        medium = True
    elif mh > 0 or em > 0:
        if em >= mh:
            em -= 1
            medium = True
        else:
            mh -= 1
            medium = True

    if h > 0:
        h -= 1
        hard = True
    elif mh > 0:
        mh -= 1
        hard = True

    if not (easy and medium and hard):
        break

    res += 1

print(res)
