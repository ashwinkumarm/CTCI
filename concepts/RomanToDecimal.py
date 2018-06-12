def getValue(c):
    if c == 'M':
        return 1000
    elif c == 'D':
        return 500
    elif c == 'C':
        return 100
    elif c == 'L':
        return 50
    elif c == 'X':
        return 10
    elif c == 'V':
        return 5
    elif c == 'I':
        return 1
    else:
        return None


def romanToDecimal(roman):
    decimal = 0
    r = 0
    while r < len(roman):
        v1 = getValue(roman[r])
        if r+1 < len(roman):
            v2 = getValue(roman[r+1])
            if v1 >= v2:
                decimal += v1
                r += 1
            else:
                decimal += (v2 - v1)
                r += 2
        else:
            decimal += v1

    return decimal


print(romanToDecimal('XXC'))



