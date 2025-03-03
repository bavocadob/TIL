n = int(input())
count = 0
divisor = 5

while n >= divisor:
    q = n // divisor
    count += (q * (q - 1) // 2) * divisor
    count += q * (n % divisor + 1)
    divisor *= 5

print(count)
