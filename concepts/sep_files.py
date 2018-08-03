import re


def add_to_file(filename, list):
    file = open(filename, "w")
    for line in list:
        file.write(line)
    file.close()


filename = input()
#filename = 'file1.txt'
file = open(filename, 'r')
file_c = 'c_' + filename
file_cs = 'cs_' + filename
file_cpp = 'cpp_' + filename

list_c = []
list_cs = []
list_cpp = []
for line in file:
    ext = re.findall(r'.(\w+)', line)[1]

    #ext = line[line.find(".") + 1:]
    if ext == 'c':
        list_c.append(line)
    elif ext == 'cs':
        list_cs.append(line)
    elif ext == 'cpp':
        list_cpp.append(line)

add_to_file(file_c, list_c)
add_to_file(file_cs, list_cs)
add_to_file(file_cpp, list_cpp)





