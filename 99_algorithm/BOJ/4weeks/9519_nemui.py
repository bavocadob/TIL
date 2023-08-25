def rotate(str_list):
    new_str = [''] * len(str_list)

    for i in range(len(str_list)):
        if i % 2:
            new_str[i] = str_list[len(str_list) - 1 - (i // 2)]
        else:
            new_str[i] = str_list[i // 2]
    return new_str


N = int(input())

original_str = list(input())
string_lst = original_str[:]

cycle = 0

while True:
    string_lst = rotate(string_lst)
    cycle += 1
    if string_lst == original_str:
        break

N %= cycle

while N != cycle:
    string_lst = rotate(string_lst)
    N += 1

print(''.join(string_lst))
