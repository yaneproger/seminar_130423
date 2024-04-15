

from slave import *


def input_data():

    import os

    file_names = []

    for filename in os.listdir("data"):
        file_names.append(filename)

    print(*file_names)

    source_file = str(input("Enter source file : "))

    spisok_kontaktov, rowscount, file_names = filerowsnumber_filedata(
        source_file)

    # print(*file_names)

    # print(spisok_kontaktov)
    # print(rowscount)

    print_data(source_file)
    print(f'{rowscount} entries')
    print()
    # spisok_kontaktov = file_readlines()
    # print(f'len(spisok_kontaktov)  {len(spisok_kontaktov) }')
    row_number = len(spisok_kontaktov)+1
    name = input("Enter name : ")
    surname = input("Enter surname : ")
    patronymic = input("Enter patronymic : ")
    phone = input("Enter phone :")
    address = input("Enter address :")
    contact_data = f'{row_number};{name};{surname};{patronymic};{phone};{address}\n'
    file_append(contact_data, source_file)
    print_data(source_file)


# input_data()


# print_data()
