# 물병
# 이 코드는 브루트포스
# 비트마스킹 공부해서 다시 풀기

def solution(bottle, lim):
    result = 0

    while True:
        curr = bottle + result
        cnt = 0
        while curr > 0:
            cnt += curr % 2
            curr //= 2
        if cnt > lim:
            result += 1
        else:
            return result


n, k = map(int, input().split())

print(solution(n, k))
