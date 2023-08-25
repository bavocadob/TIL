def main():
    N, L, R, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    A.sort()
    for i in range(1 << N):
        bm = i
        diffs = []
        for j in range(N):
            if bm & (1 << j):
                diffs.append(A[j])

    print(ans)


if __name__ == "__main__":
    main()
