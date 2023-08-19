N, K = map(int, input().split())

kids = list(map(int, input().split()))

gap = [0] * (N - 1)

for i in range(N - 1):
    gap[i] = kids[i + 1] - kids[i]
gap.sort(reverse=True)

print(sum(gap[K - 1:]))