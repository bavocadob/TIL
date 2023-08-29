def solution(code):
    if '0' in code or code == '':
        return 0

    dp = [0] * (len(code) + 1)
    dp[0] = dp[1] = 1
    for i in range(2, len(code) + 1):
        if code[i - 1] == '.':
            dp[i] = dp[i - 1]
            continue
        if code[i - 2] == '1' or (code[i - 2] == '2' and int(code[i - 1]) <= 6):
            dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000
        else:
            dp[i] = dp[i - 1]
    # print(dp)
    return dp[len(code)]


c = input()
c = c.replace('20', '.').replace('10', '.').strip()

print(solution(c))
