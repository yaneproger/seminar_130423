

def filerowsnumber_filedata(input_file_name):

    import os

    file_names = []

    for filename in os.listdir("data"):
        file_names.append(filename)

    # print(file_names)

    source_file = input_file_name
    # print(f'source_file  : {source_file}')

    while source_file not in file_names:
        source_file = str(input("Enter source text file : "))

    # print(f'source_file  : {source_file}')
    # print(f'source_file type  : {type(source_file)}')
    # print("Select source file :")

    with open(source_file, 'r', encoding='utf-8') as file:
        source_file_data = file.readlines()

    # print(f'source_file_data  : {source_file_data}')
    # print(data)

    # spisok_kontaktov = source_file_data  # 4itaet fayl vozvrawaet Spisok Strok

    file_rows_number = len(source_file_data)

    return source_file_data, file_rows_number, file_names


#


# def filerowsnumber_filedata(input_file_name):

#     import os

#     file_names = []

#     for filename in os.listdir("."):
#         file_names.append(filename)

#     print(file_names)

#     source_file = input_file_name
#     # print(f'source_file  : {source_file}')

#     while source_file not in file_names:
#         source_file = str(input("Enter source text file : "))

#     print(f'source_file  : {source_file}')
#     print(f'source_file type  : {type(source_file)}')
#     # print("Select source file :")

#     with open(source_file, 'r', encoding='utf-8') as file:
#         source_file_data = file.readlines()

#     print(f'source_file_data  : {source_file_data}')
#     # print(data)

#     spisok_kontaktov = source_file_data  # 4itaet fayl vozvrawaet Spisok Strok

#     file_rows_number = len(source_file_data)

#     return source_file_data, file_rows_number, file_names

# #


#
#


def file_read(filename):
    with open(filename, 'r', encoding='UTF-8') as accounts:
        return accounts.read()


# def file_readlines():
#     with open('accounts.txt', 'r', encoding='utf-8') as accounts:
#         return accounts.readlines()


def file_append(data, filename):
    with open(filename, 'a', encoding='UTF-8') as accounts:
        accounts.write(data)


# def file_rewrite(data=''):
#     with open('accounts.txt', 'w', encoding='UTF-8') as accounts:
#         accounts.write(data)


#
#
#

def file_rewritelines(data, filename):
    with open(filename, 'w', encoding='UTF-8') as accounts:
        accounts.writelines(data)


def print_data(filename):
    return print(file_read(filename))


def print_contacts():

    import os
    file_names = []
    for filename in os.listdir("data"):
        file_names.append(filename)
    print(file_names)
    source_file = str(input("Enter source file : "))
    spisok_kontaktov, rowscount, file_names = filerowsnumber_filedata(
        source_file)

    # print(*file_names)

    # print(spisok_kontaktov)
    # print(rowscount)
    print_data(source_file)
    print(f'{rowscount} entries')
    print()

#
#
# print_contacts()


# def file_read(filename):
#     with open(filename, 'r', encoding='UTF-8') as accounts:
#         return accounts.read()


# def file_readlines():
#     with open('accounts.txt', 'r', encoding='utf-8') as accounts:
#         return accounts.readlines()


# def file_append(data, filename):
#     with open(filename, 'a', encoding='UTF-8') as accounts:
#         accounts.write(data)


# def file_rewrite(data=''):
#     with open('accounts.txt', 'w', encoding='UTF-8') as accounts:
#         accounts.write(data)


# def file_rewritelines(data, filename):
#     with open(filename, 'w', encoding='UTF-8') as accounts:
#         accounts.writelines(data)


# def print_data(filename):
#     return print(file_read(filename))


# def print_contacts():

#     import os
#     file_names = []
#     for filename in os.listdir("data"):
#         file_names.append(filename)
#     print(file_names)
#     source_file = str(input("Enter source file : "))
#     spisok_kontaktov, rowscount, file_names = filerowsnumber_filedata(
#         source_file)

#     print(*file_names)

#     print(spisok_kontaktov)
#     print(rowscount)
#     print_data(source_file)
