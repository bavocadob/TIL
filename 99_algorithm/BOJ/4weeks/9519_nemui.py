def rotate(str_list):
    new_str = [''] * len(str_list)

    for i in range(len(str_list)):
        if i % 2:
            new_str[i] = str_list[len(str_list) - 1 - (i // 2)]
        else:
            new_str[i] = str_list[i // 2]
    return new_str


N = int(input())

origianl_str = list(input())

cycle = len(origianl_str)


for _ in range(10):
    origianl_str = rotate(origianl_str)
    print(''.join(origianl_str))


