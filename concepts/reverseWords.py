
def reverseWords(str):
    words = []
    for i in str.split(' '):
        if i == " " or i == "":
            continue
        words.append(i)

    return ' '.join(reversed(words))


def reverseW(str):
    n = len(str)
    s = list(str)
    reverse(s, 0, n-1)
    reverseEachWord(s,n)
    s = trimSpaces(s, n)
    return ''.join(s)


def trimSpaces(str, n):
    i = j = 0
    res = []
    while j < n:
        while j < n and str[j] == " ":
            j += 1
        while j < n and str[j] != " ":
            str[i] = str[j]
            i += 1
            j += 1
        if j < n:
            str[i] = ' '
            i += 1
    return str[:i]


def reverseEachWord(str, n):
    i = j = 0
    while j < n:
        while i < j or (i < n and str[i] == " "):
            i += 1
        while i > j or (j < n and str[j] != " "):
            j += 1
        reverse(str, i, j-1)


def reverse(str, i , j):
    while i < j:
        temp = str[i]
        str[i] = str[j]
        str[j] = temp
        i += 1
        j -= 1


print(reverseW('hello     ashwin,       how you today?'))
