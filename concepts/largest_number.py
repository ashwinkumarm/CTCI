
#
# Input: [1, 2, 3, 4] , Output: "4321"
#
# Input: [9, 5, 30, 3, 34] , Output: "9534330"
#
# Input: [0, 55, 50] , Output: "55500"

def comp(x, y):
    xy = str(x) + str(y)
    yx = str(y) + str(x)
    return int(xy) > int(yx)

input =[1, 2, 3, 4]
s_arr = sorted(input, key = comp)
largest_number ="".join([str(i) for i in s_arr])
print(largest_number)
