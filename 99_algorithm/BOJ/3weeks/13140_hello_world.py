visited = [False] * 10

valid = False
result = []


def solution(depth, value, arr):
    global valid, result
    if valid:
        return

    if depth == 7 and value == target:
        valid = True
        result = arr[:]
        return
    elif depth == 7 or value > target:
        return

    if depth < 2:
        for i in range(1, 10):
            if not visited[i]:
                visited[i] = True
                arr.append(i)
                solution(depth + 1, value + i * 10000, arr)
                visited[i] = False
                arr.pop()
    elif depth == 2:
        for i in range(10):
            if not visited[i]:
                visited[i] = True
                arr.append(i)
                solution(depth + 1, value + i * 1001, arr)
                visited[i] = False
                arr.pop()
    elif depth == 3:
        for i in range(10):
            if not visited[i]:
                visited[i] = True
                arr.append(i)
                solution(depth + 1, value + i * 1000, arr)
                visited[i] = False
                arr.pop()
    elif depth == 4:
        for i in range(10):
            if not visited[i]:
                visited[i] = True
                arr.append(i)
                solution(depth + 1, value + i * 120, arr)
                visited[i] = False
                arr.pop()
    elif depth == 5:
        for i in range(10):
            if not visited[i]:
                visited[i] = True
                arr.append(i)
                solution(depth + 1, value + i * 100, arr)
                visited[i] = False
                arr.pop()
    elif depth == 6:
        for i in range(10):
            if not visited[i]:
                visited[i] = True
                arr.append(i)
                solution(depth + 1, value + i * 1, arr)
                visited[i] = False
                arr.pop()


target = int(input())
# if target >= 184011 or 33985 >= target:
#     print('No Answer')
# else:
solution(0, 0, [])
if result:
    print('  ', result[0], result[3], result[4], result[4], result[2], sep='')
    print('+ ', result[1], result[2], result[5], result[4], result[6], sep='')
    print('-------')
    if target > 99999:
        print(' ', target,sep='')
    else:
        print('  ', target, sep='')
else:
    print('No Answer')