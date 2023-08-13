# 멍멍이 쓰다듬기

# N의 제곱만큼의 숫자를 만들려면 1부터 N의 제곱근만큼 갔다가 다시 내려와야 한다
# 이때 N의 제곱근이 딱 떨어지지 않을 경우 1번 혹은 2번 더 반복해야 하는데
# 만약 N의 제곱근을 버림한 값을 K라고 할때 K ** 2 + K 보다 같거나 작은 경우 K * 2번만에 되고 (왜냐하면 1부터 K사이의 순서를 한번 더 밟으면 되니까)
# 그렇지 않을 경우 2번 더 밟아야 한다 1 ~ K까지 한번밟고 K를 한번 더 밟은 뒤 1~ K-1의 값을 밟아야 하니까
# 이때 만약 키차이가 나지 않을 경우 -1이 출력되므로 키차이가 같은 경우 0을 출력한다

from math import sqrt


monkey, dog = map(int, input().split())

gap = dog - monkey

root = int(sqrt(gap))

if gap == 0:
    print(0)
elif root ** 2 == gap:
    print(root * 2 - 1)
elif root ** 2 + root >= gap:
    print(root * 2)
else:
    print(root * 2 + 1)

