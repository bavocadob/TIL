import sys

input = sys.stdin.readline
MAX_SCORE = 147

m = int(input())

for _ in range(m):
    remaining_points = [MAX_SCORE, MAX_SCORE]
    scores = [0, 0]
    match_decided_turn = 0
    current_turn = 0
    previous_points = 0

    n = int(input())
    points_sequence = list(map(int, input().split()))

    for turn_index, points in enumerate(points_sequence, start=1):
        if points == 0:
            if previous_points == 1:
                remaining_points[current_turn] -= 7
            current_turn = 1 - current_turn
        else:
            scores[current_turn] += points
            if points == 1:
                remaining_points[current_turn] -= 1
                remaining_points[1 - current_turn] -= 8
            else:
                if previous_points == 1:
                    remaining_points[current_turn] -= 7
                else:
                    remaining_points[current_turn] -= points
                    remaining_points[1 - current_turn] -= points

        if (scores[0] - scores[1] > remaining_points[1] or scores[1] - scores[0] > remaining_points[
            0]) and match_decided_turn == 0:
            match_decided_turn = turn_index

        previous_points = points

    if match_decided_turn == 0:
        match_decided_turn = n

    print(match_decided_turn)
