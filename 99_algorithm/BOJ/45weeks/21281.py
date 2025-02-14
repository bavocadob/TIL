N = int(input())
digits = [int(d) for d in str(N)][::-1]
digits.append(0)

ss = digits[0]

for k in range(1, len(digits)):
    if digits[k] < 9 and 0 <= ss - 1 <= k * 9:
        break
    ss += digits[k]

digits[k] += 1
ss -= 1

for p in range(k):
    digits[p] = min(ss, 9)
    ss -= digits[p]

if digits[-1] == 0:
    digits.pop()

result = ''.join(map(str, digits[::-1]))
print(result)
