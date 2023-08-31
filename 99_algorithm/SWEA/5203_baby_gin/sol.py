import sys

sys.stdin = open('input.txt')

T = int(input())


def triplet(player, number):
    return cnt[player][number] >= 3


def r(player):
    c = 0

    for num in cnt[player]:
        if num == 0:
            c = 0
        else:
            c += 1
        if c == 3:
            return True

    return False


for tc in range(T):

    cnt = [[0] * 10 for _ in range(2)]

    turn = 0
    for card in list(map(int, input().split())):
        cnt[turn][card] += 1

        if triplet(turn, card) or r(turn):
            print(f'#{tc + 1} {turn + 1}')
            break
        turn = (turn + 1) % 2
    else:
        print(f'#{tc + 1} 0')

