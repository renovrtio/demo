import json
# with open('pi_digits.txt') as file_opject:
#     # print(type(file_opject))
#     # contents = file_opject.read()
#     # print(type(contents))
#     # print(contents)
#     for line in file_opject:
#         print(line.strip())

# try:
#     with open('abc.txt') as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError as file_not_found:
#     print(type(file_not_found))
#     print(file_not_found)

# with open('programming.txt', 'w', encoding='utf-8') as file_opject:
#     for var in range(55295):
#         file_opject.write(str(var) + '\t' + chr(var) + '\n')



filename = 'chkrec.cfg'
with open(filename) as f_obj:
    file_types = {}
    types = ''
    while True:
        type_data = {}
        line = f_obj.readline()
        # line = line.strip()
        if line:
            if '[' in line:
                line = line.strip()
                line = line[1:-2]
                file_types[line] = type_data
                types = line
            elif line != '\n':
                line = line.strip()
                lines = line.split('=')
                file_types[types][lines[0].strip()] = lines[1].strip()
        else:
            break
    with open('file_types.json', 'w') as type_obj:
        json.dump(file_types, type_obj)
    with open('file_types.json') as type_obj2:
        types2 = json.load(type_obj2)
    print(types2)


#     for line in f_obj.readlines():
#         line = line.strip()
#         if line != '':
#             print(line)