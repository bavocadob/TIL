def roman_to_arabic(roman_str):
    result = 0
    stack = [roman_str[0]]

    for i in range(1, len(roman_str)):
        if not stack:
            stack.append(roman_str[i])
        else:
            if roman_dict[roman_str[i]] > roman_dict[stack[-1]]:
                result += roman_dict[roman_str[i]] - roman_dict[stack.pop()]
            else:
                result += roman_dict[stack.pop()]
                stack.append(roman_str[i])

    while stack:
        result += roman_dict[stack.pop()]

    return result


def arabic_to_roman(arabic_num):
    result = ''
    while arabic_num > 0:

        if arabic_num >= 1000:
            result += 'M'
            arabic_num -= 1000
        elif arabic_num >= 900:
            result += 'CM'
            arabic_num -= 900
        elif arabic_num >= 500:
            result += 'D'
            arabic_num -= 500
        elif arabic_num >= 400:
            result += 'CD'
            arabic_num -= 400
        elif arabic_num >= 100:
            result += 'C'
            arabic_num -= 100
        elif arabic_num >= 90:
            result += 'XC'
            arabic_num -= 90
        elif arabic_num >= 50:
            result += 'L'
            arabic_num -= 50
        elif arabic_num >= 40:
            result += 'XL'
            arabic_num -= 40
        elif arabic_num >= 10:
            result += 'X'
            arabic_num -= 10
        elif arabic_num >= 9:
            result += 'IX'
            arabic_num -= 9
        elif arabic_num >= 5:
            result += 'V'
            arabic_num -= 5
        elif arabic_num >= 4:
            result += 'IV'
            arabic_num -= 4
        elif arabic_num >= 1:
            result += 'I'
            arabic_num -= 1
    return result


roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

input_str1 = input()
input_str2 = input()

arabic_num1 = roman_to_arabic(input_str1)
arabic_num2 = roman_to_arabic(input_str2)
roman_num = (arabic_to_roman(arabic_num1 + arabic_num2))
print(arabic_num1 + arabic_num2)
print(roman_num)
