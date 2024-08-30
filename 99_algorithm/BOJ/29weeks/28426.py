n = int(input())
i = 2

print(3, end=" ")
for _ in range(n - 2):
    print(i, end=" ")
    i += 2
if n > 1:
    print(i + (4 if n % 3 == 2 else 0))
