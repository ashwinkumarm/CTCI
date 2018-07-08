class ClassCompName:
    def __init__(self, f_name, l_name, grade):
        self.f_name = f_name
        self.l_name = l_name
        self.grade = grade

    def __lt__(self, other):
        return other.l_name < self.l_name

    # def __gt__(self, other):
    #     return other.l_name > self.l_name
    #
    # def __le__(self, other):
    #     return other.l_name <= self.l_name
    #
    # def __ge__(self, other):
    #     return other.l_name >= self.l_name

    # def __ne__(self, other):
    #     return other.l_name == self.l_name
    #
    def __eq__(self, other):
        return other.l_name == self.l_name


persons = [ClassCompName('ash', 'ash', 1), ClassCompName('ash1', 'ash', 1), ClassCompName('win', 'win', 2), ClassCompName('kum', 'kum', 3), ClassCompName('ar', 'ar', 4)]

persons.sort()
prev = persons[0]
for p in range(1, len(persons)):
    if persons[p] == prev:
        print(persons[p].l_name)
    prev = persons[p]



