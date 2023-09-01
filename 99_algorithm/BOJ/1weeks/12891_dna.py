# 부분 문자열 길이에 따른 DNA 요소들을 슬라이딩 윈도우를 통해 문자열을 순회하면서 유동적으로 값을 계산

# 슬라이딩 윈도우에 저장된 DNA들을 바탕으로 옳은 DNA 문자열인지 판단.
def is_valid_pwd(dna, pwd):
    for i in range(len(dna)):
        if dna[i] > pwd[i]:
            return False

    return True


str_len, pwd_len = map(int, input().split())

dna_string = input()

min_dna = list(map(int, input().split()))

# A C G T 순서
pwd = [0] * 4

# A C G T 순서로 딕셔너리에 저장하면 if로 분류하지 않고 dict값에 맞춰서 판별 가능
pwd_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

for i in range(pwd_len):
    if pwd_dict.get(dna_string[i]) is not None:
        pwd[pwd_dict.get(dna_string[i])] += 1

valid_cnt = int(is_valid_pwd(min_dna, pwd))

for i in range(pwd_len, str_len):
    # 이전 인덱스의 DNA 문자에 해당하는 값 제거
    if pwd_dict.get(dna_string[i - pwd_len]) is not None:
        pwd[pwd_dict.get(dna_string[i - pwd_len])] -= 1
    # 현재 인덱스의 DNA 문자에 해당하는 값 추가
    if pwd_dict.get(dna_string[i]) is not None:
        pwd[pwd_dict.get(dna_string[i])] += 1

    # 변경된 문자열을 바탕으로 옳은 DNA 문자열인지 판단
    if is_valid_pwd(min_dna, pwd):
        valid_cnt += 1

print(valid_cnt)
