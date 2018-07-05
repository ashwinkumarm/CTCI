def clean_strands():

    lines = ['NEWDNASEQUENCE', 'CCCCTTTGAGAGA', 'AGATCTCTCTC',
         'TGATGCATCCCGGA', 'GGAAAATCCCC',
         'RRASDLKJASDLKLAJ', 'CC', 'A', 'CTCTATATATATA']
    validSet = set()
    validSet.add('A')
    validSet.add('T')
    validSet.add('G')
    validSet.add('C')


    cleaned_list = []

    for line in lines:
        flag = True
        if len(line) > 10 and len(line) < 100:
            for c in line:
                if c not in validSet or c.islower():
                    flag = False
                    break
        else:
            flag = False

        if flag == True:
            cleaned_list.append(line)

    print(cleaned_list)

clean_strands()