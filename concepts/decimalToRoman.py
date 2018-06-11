from collections import OrderedDict


def createDict():
    dict_roman = OrderedDict()
    dict_roman[1000] = 'M'
    dict_roman[900] = 'CM'
    dict_roman[500] = 'D'
    dict_roman[400] = 'CD'
    dict_roman[100] = 'C'
    dict_roman[90] = 'XC'
    dict_roman[50] = 'L'
    dict_roman[40] = 'XL'
    dict_roman[10] = 'X'
    dict_roman[5] = 'V'
    dict_roman[4] = 'IV'
    dict_roman[1] = 'I'

    return dict_roman


def decimalToRoman(decimal):
    roman_dict = createDict()
    roman = []
    while decimal > 0:
        for k in roman_dict.keys():
            q,r = divmod(decimal, k)
            if q >= 1:
                decimal = r
                roman += [roman_dict[k]] * q
                if decimal == 0:
                    break

    return ''.join(roman)


print(decimalToRoman(35))
print(decimalToRoman(994))
print(decimalToRoman(1995))
print(decimalToRoman(2015))