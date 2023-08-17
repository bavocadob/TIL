# 한줄 텍스트의 틱택토 최종상태 여부 검증
import sys

# input = sys.stdin.readline


def get_winner(tt):
    cnt = {'X':0, 'O':0}
    winner = None
    diagonal1 = tt[0]
    diagonal2 = tt[2]


    dia1 = True
    dia2 = True
    for i in range(3):
        if tt[i * 3] == tt[i * 3 + 1] == tt[i * 3 + 2]:
            if tt[i * 3] != '.':
                cnt[tt[i * 3]] += 1

        if tt[i] == tt[i + 3] == tt[i + 6]:
            if tt[i] != '.':
                cnt[tt[i]] += 1

        if tt[i * 4] != diagonal1:
            dia1 = False

        if tt[(i + 1) * 2] != diagonal2:
            dia2 = False

    if dia1:
        cnt[diagonal1] += 1
    if dia2:
        cnt[diagonal2] += 1

    if cnt['O'] == 0 and cnt['X'] == 0:
        return None
    elif cnt['O'] > 1 and cnt['X'] > 0:
        return None
    else:
        if cnt['O'] > 0:
            return 'O'
        elif cnt['X'] > 0:
            return 'X'


def solution(ttt: str):
    x_count = ttt.count('X')
    o_count = ttt.count('O')

    # o가 더 많거나 x가 o보다 2개 더 많으면 잘못됨
    if o_count > x_count or x_count - 1 > o_count:
        return False

    if o_count < 3 and x_count < 3:
        return False

    # 승자가 둘인 경우도 틀림
    winner = get_winner(ttt)

    # 승자가 없거나 승자가 없는데 바둑판이 꽉차지 않은 경우
    if winner is None and ttt.count('.') > 0:
        return False

    # O가 이기면 x와 개수가 같아야함 ,X가 이기면 O보다 X가 많아야 함
    if winner is not None:
        if (winner == 'O' and o_count != x_count) or (winner == 'X' and o_count >= x_count):
            return False

    # 다 통과하면 return
    return True


if __name__ == '__main__':
    while True:
        tic_tac_toe = input().rstrip()

        if tic_tac_toe == 'end':
            break

        if solution(tic_tac_toe):
            print('valid')
        else:
            print('invalid')
