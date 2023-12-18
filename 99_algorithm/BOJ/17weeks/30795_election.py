def get_data(map_a, map_b):
    data = input().rstrip().split()
    cnt = 1

    data_idx = 0

    while cnt <= 80:
        tmp_name = ''
        while data[data_idx] != 'Group':
            tmp_name += data[data_idx] + ' '
            data_idx += 1
        tmp_name = tmp_name.rstrip()
        data_idx += 1
        tmp_group = data[data_idx]
        data_idx += 2
        tmp_team = data[data_idx]
        data_idx += 1

        tmp_character = '.'.join([tmp_name, tmp_group, tmp_team])
        map_a[tmp_character] = cnt
        map_b[cnt] = tmp_character
        cnt += 1


# map_A => Name to Rank
# map_B => Rank to Name
size = 80
MOD = 16
expect_map_A = dict()
expect_map_B = dict()

rst_map_A = dict()
rst_map_B = dict()

get_data(expect_map_A, expect_map_B)
get_data(rst_map_A, rst_map_B)

cinderella = [0] * (size + 1)

for rank in range(1, size + 1):
    cinderella_pt = 0

    character = rst_map_B[rank]
    expected_rank = expect_map_A.get(character, size + 2)

    # 현재티어, 예상티어 계산
    tier = ((rank - 1) // MOD) + 1
    expected_tier = ((expected_rank - 1) // MOD) + 1

    # 1번 조건 처리
    if expected_tier > tier:
        cinderella_pt += (expected_tier - tier) * 10000

    # 2번 조건 처리
    if not (rank - 1) % MOD:
        if expected_tier > tier:
            cinderella_pt += 20000
        else:
            cinderella_pt += 10000

    # 3번 조건 처리
    if tier == 1 and expected_tier != 1:
        p = 0

        for expected_tgt_rank in range(1, expected_rank):
            tgt_character = expect_map_B.get(expected_tgt_rank)
            actual_tgt_rank = rst_map_A.get(tgt_character, 82)
            if expected_tgt_rank <= 16 and actual_tgt_rank > 16:
                p += 1

        cinderella_pt += p * 30000

    cinderella[rank] = cinderella_pt

cinderella_idx = cinderella.index(max(cinderella))

cinderella_data = rst_map_B.get(cinderella_idx).split('.')
print(cinderella_data[1])
print(cinderella_data[2])
print(cinderella_data[0])
