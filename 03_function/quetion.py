def func_name(parm1, parm2):

    return parm1 + parm2

func_name(1, 2)
print(func_name(1,2))

def func(*args, sep = ' '):
    print(*args, sep)

func('첫', '두', '세')