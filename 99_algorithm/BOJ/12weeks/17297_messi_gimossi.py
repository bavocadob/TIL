def solution(N, messi_idx):
    if N <= 2:
        return messi_idx

    if messi_idx <= messi[N - 1]:
        return solution(N - 1, messi_idx)
    elif messi_idx == messi[N - 1] + 1:
        return 6
    else:
        return solution(N - 2, messi_idx - 1 - messi[N - 1])


result = ' Messi Gimossi'
messi = [0, 5, 13]

M = int(input())

while messi[-1] < M:
    siiiiiu = messi[-2] + messi[-1] + 1
    messi.append(siiiiiu)

rst_idx = solution(len(messi), M)
if rst_idx == 6:
    print('Messi Messi Gimossi')
else:
    print(result[rst_idx])
