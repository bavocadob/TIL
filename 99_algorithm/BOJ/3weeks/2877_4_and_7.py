
K = int(input())

c = 2
i = 1

while K > c:
    K -= c
    c *= 2
    i += 1

result = ['4'] * i

binary_str = bin(K - 1)[2:]


for j in range(i - len(binary_str), i):
    if binary_str[j - i + len(binary_str)] == '1':
        result[j] = '7'

print(''.join(result))

# print(K, c, i)
# print()
# print(len(bin(K - 1)[2:]))

