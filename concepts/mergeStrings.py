def mergeStrings(listOfStrings):
    firstSet = {}
    lastSet = {}

    for i in listOfStrings:
        if i[:3] not in firstSet:
            firstSet[i[:3]] = [i]
        else:
            firstSet[i[:3]].append(i)
        if i[-3:] not in lastSet:
            lastSet[i[-3:]] = [i]
        else:
            lastSet[i[-3:]].append(i)

    first_string = ""
    for i in firstSet.keys():
        if i not in lastSet:
            first_string = firstSet[i][0]
            break

    if first_string == "":
        first_string = listOfStrings[0]

    last_string = ""
    for i in lastSet.keys():
        if i not in firstSet:
            last_string = lastSet[i][0]
            break

    if last_string == "":
        last_string = listOfStrings[-1]

    final_string = first_string
    firstSet[final_string[:3]].remove(first_string)

    if len(firstSet[final_string[:3]]) == 0:
        del firstSet[final_string[:3]]

    while True:
        if final_string[-3:] in firstSet:
            key = final_string[-3:]
            final_string += firstSet[key][0]
            del firstSet[key][0]
            if len(firstSet[key]) == 0:
                del firstSet[key]

        elif len(firstSet) == 0:
            return final_string

        else:
            raise Exception


#listOfStrings = ["aaabbbyyy", "yyyccc","cccxxxaaa", "aaaccc" ]
#listOfStrings = ["cccxxx", "xxxbbb","bbbccc" ]
#listOfStrings = ["aaabbbyyy", "yyyaaa","xxxbbb", "bbbyyy", "yyyxxx" ]
listOfStrings = ['AAACCCAATTT', 'TTTACACAGCT', 'GCTGGGCCCAGT', 'AGTGGGGGGGGG']
print(mergeStrings(listOfStrings))

