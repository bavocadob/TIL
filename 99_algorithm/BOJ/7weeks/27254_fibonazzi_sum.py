# 문제 = N을 피보나치 수들의 합으로 표현하는 모든 경우의 수를 나타내라
# 이때 한개의 숫자는 K번까지 사용 가능

def backtrack(fibo_idx, fibo_cnt, val, numbers: list):
    # print(numbers, fibo_idx, val)
    if fibo_idx == 10:
        return

    if val >= N:
        if val == N:
            print('+'.join(numbers))
        return

    if fibo_cnt == K:
        backtrack(fibo_idx + 1, 0, val, numbers)
    else:

        numbers.append(str(fibonacci[fibo_idx]))
        backtrack(fibo_idx, fibo_cnt + 1, val + fibonacci[fibo_idx], numbers)
        numbers.pop()

        if val + fibonacci[fibo_idx + 1] <= N:
            backtrack(fibo_idx + 1, 0, val, numbers)


N = int(input())
K = int(input())

# n범위가 100이므로 100이하의 피보나치 초기화
fibonacci = [1, 2, 3]
for i in range(3, 11):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

backtrack(0, 0, 0, [])
