from copy import deepcopy


def parens(n):
    res = []
    cr = [None for i in range(2 * n)]
    _parens(cr, res, n, n, 0)
    return res


def _parens(cr, res, lr, rr, i):
    if lr < 0 or rr < lr:
        return
    elif lr == 0 and rr == 0:
            res.append(''.join(deepcopy(cr)))
    else:
        cr[i] = '('
        _parens(cr, res, lr - 1, rr, i+1)
        cr[i] = ')'
        _parens(cr, res, lr, rr - 1, i+1)


print(parens(3))
