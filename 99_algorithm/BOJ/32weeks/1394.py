MOD = 900528
words = input().rstrip()
pw_dict = dict()

for i in range(len(words)):
    pw_dict[words[i]] = i + 1

pw = input().rstrip()
ans = 0
temp = 1

for i in range(len(pw) - 1, -1, -1):
    ch = pw[i]

    ans += pw_dict[ch] * temp
    temp *= len(words)

    ans %= MOD
    temp %= MOD

print(ans)
