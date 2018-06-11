def anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    charArray = [0 for _ in range(128)]

    for i in range(len(str1)):
        charArray[ord(str1[i]) - ord('a')] += 1
        charArray[ord(str2[i]) - ord('a')] -= 1

    for i in charArray:
        if i != 0:
            return False

    return True


print(anagram('dog', 'god'))