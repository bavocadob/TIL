import sys

input = sys.stdin.readline
N = int(input())
bit_mask = set()

numbers = list(map(int, input().split()))

for num in numbers:
    while num in bit_mask:
        bit_mask.remove(num)
        num += 1
    bit_mask.add(num)

if (bit_count := len(bit_mask)) == 2 or (bit_count == 1 and N != 1):
    print("Y")
else:
    print("N")
