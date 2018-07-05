def triple_step(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)


def triple_step_bottomup(n):
    count_steps = [0 for i in range(n)]
    count_steps[0] = 1
    count_steps[1] = 2
    count_steps[2] = 4

    i = 3
    while i < n:
        count_steps[i] = count_steps[i-1] + count_steps[i-2] + count_steps[i-3]
        i += 1

    return count_steps[n-1]


print(triple_step_bottomup(8))