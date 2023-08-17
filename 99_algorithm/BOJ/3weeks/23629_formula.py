a_to_i = {'ZERO': '0', 'ONE': '1', 'TWO': '2', 'THREE': '3', 'FOUR': '4', 'FIVE': '5', 'SIX': '6', 'SEVEN': '7',
          'EIGHT': '8', 'NINE': '9'}
i_to_a = {'0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR', '5': 'FIVE', '6': 'SIX', '7': 'SEVEN',
          '8': 'EIGHT', '9': 'NINE'}

input_formula = input()

for key in a_to_i.keys():
    input_formula = input_formula.replace(key, a_to_i[key])



curr_num = 0
curr_oper = None

result = 0

valid = True

for i, char in enumerate(input_formula):
    if char.isdigit():
        curr_num *= 10
        curr_num += int(char)

    else:
        if curr_oper is not None:
            if i == 0 or not input_formula[i - 1].isdigit():
                valid = False
                break
            if curr_oper == '+':
                result += curr_num
            elif curr_oper == '-':
                result -= curr_num
            elif curr_oper == 'x':
                result *= curr_num
            elif curr_oper == '/':
                result = int(result / curr_num)
            curr_num = 0

        else:
            result = curr_num
            curr_num = 0

        curr_oper = char

if valid:
    result = str(result)

    for key in i_to_a.keys():
        result = result.replace(key, i_to_a[key])
    print(input_formula)
    print(result)
else:
    print('Madness!')
