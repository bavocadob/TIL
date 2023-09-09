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

                if sum(diffs) > R:
                    break

        if len(diffs) > 1 and L <= sum(diffs) <= R and max(diffs) - min(diffs) >= X:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
