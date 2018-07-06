def eight_queens(n):
    results = [[]]
    columns = [0 for i in range(n)]
    _eight_queens(0, columns, results, n)
    return len(results) - 1


def _eight_queens(r, columns, results, n):
    if r == n:
        results.append(columns)
    else:
        for c in range(n):
            if check_valid(r, c, columns):
                columns[r] = c
                _eight_queens(r+1, columns, results, n)


def check_valid(r1, c1, columns):
    for r2 in range(r1):
        c2 = columns[r2]
        if c2 == c1:
            return False

        if abs(c2 - c1) == r1 - r2:
            return False

    return True


print(eight_queens(8))