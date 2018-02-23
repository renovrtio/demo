import os
import re

def update_file_name(dir_path):
    '''
    修改chk文件家文件名称，改成现有文件名+后缀名.chk
    '''
    # 1、判断路径是否存在
    if os.path.exists(dir_path):
        print('路径存在')
    else:
        os.makedirs(dir_path)

    # 2、获取路径所有文件和文件价，如果是文件修改文件名
    for file_name in os.listdir(dir_path):
        full_file_path = os.path.join(dir_path, file_name)
        # print(full_file_path)
        if os.path.isfile(full_file_path):
            # print(full_file_path)
            # (filepath, file_name) = os.path.split(file_name)
            # print(filepath + '\n' + file_name)
            (shotname, extension) = os.path.splitext(file_name)
            new_file_path = os.path.join(dir_path, shotname + extension + '.chk')
            os.rename(full_file_path, new_file_path)
            # print(shotname + '\n' + extension)
        # else:
        #     print(file_name + '\t' + '路径是文件夹')

def read_file(dir_path):
    '''
    读取文件头
    '''
    # 1、判断路径是否存在
    if os.path.exists(dir_path):
        print('路径存在')
    else:
        os.makedirs(dir_path)

    # 2、获取路径所有文件和文件价
    for file_name in os.listdir(dir_path):
        full_file_path = os.path.join(dir_path, file_name)
        # print(full_file_path)
        if os.path.isfile(full_file_path):
            with open(full_file_path, 'rb+') as f_obj:
                file_head = f_obj.read(100)
                # print(file_head)
                # file_type = b'\x47\x49\x46\x38'
                print(file_head)
                # if file_type in file_head:
                #     print('gif')
                # print(file_name, file_head)

def head_is_intype(file_head, chk_path):
    dir_file_type = {}
    dir_file_type_key = ''
    with open(chk_path, 'r', encoding='utf-8') as ckh_obj:
        while True:
            dir_file_type_info = {}
            line = ckh_obj.readline()
            if line:
                line = line.strip()
                if '[' in line:
                    line = line[1:-2]
                    dir_file_type_key = line
                    dir_file_type[line] = dir_file_type_info
                elif '=' in line:
                    type_info = line.split('=')
                    # print('-' + line + '-')
                    info_key, info_value = type_info[0].strip(), type_info[1].strip()
                    # print(info_key, info_value)
                    if 'headmark0' in line:
                        lines = re.findall((r'..'), info_value)
                        info_value = r'\x' + r'\x'.join(lines)

                    dir_file_type[dir_file_type_key][info_key] = info_value
    
            else:
                print('-' + line + '-')
                break
            # print(dir_file_type)
    # file_type = r'\x47\x49\x46\x38\x13'
    for value in dir_file_type.values():
        # print(value, type(value))
        if value['headmark0'] in file_head:
            print(value['postfix'])
    

            

if __name__ == '__main__':
    pwd = os.getcwd()
    dir_path = pwd + r'\chk'
    # print(dir_path)
    # update_file_name(dir_path)
    read_file(dir_path)

    # head_is_intype('dsafasd', r'D:\python_work\demo\chkrec.cfg')