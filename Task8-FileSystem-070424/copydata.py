

from slave import *


def copy_contact():

    # logika
    # opisanie
    # kopirovanie stroki kontaka iz spiska iz odnogo fayla
    # i dobavlenie ee v konec drugogo spiska drugogo fayla

    # 0.pe4ataem spisok faylov
    # 1.vivodim priglawenie - iz kakogo fayla xotite kopirovat
    # 2.pe4ataem spisok kontaktov vibrannogo fayla
    # 3.predlagayem vibrat kakoy kontakt xotite kopirovat
    # 4.vivodim priglawenie - kuda xotite kopirovat
    # 5.formatiruyem i zapisivayem dannie
    #
    #
    #

    import os

    file_names = []

    for filename in os.listdir("data"):
        file_names.append(filename)

    print(*file_names)

    source_file = str(input("Enter source file : "))

    spisok_kontaktov, rowscount, file_names = filerowsnumber_filedata(
        source_file)

    # print(*file_names)
    print_data(source_file)
    # print(spisok_kontaktov)
    print(f'{rowscount} entries')
    print()

    # print(f'source_file  : {source_file}')

    # while source_file not in file_names:
    #     source_file = str(input("Enter source text file : "))

    # print(f'source_file  : {source_file}')
    # print(f'source_file type  : {type(source_file)}')
    # # print("Select source file :")

    # with open(source_file, 'r', encoding='utf-8') as file:
    #     source_file_data = file.readlines()

    # print(f'source_file_data  : {source_file_data}')
    # # print(data)

    # spisok_kontaktov = source_file_data  # 4itaet fayl vozvrawaet Spisok Strok
    # print([spisok_kontaktov])
    # print(*file_read().strip().split("\n"))
    # print_data(source_file)
    # print(f'len(spisok_kontaktov)  {len(spisok_kontaktov) }')

    contact_number_int = int(input('Enter contact number u want to copy : '))-1
    while contact_number_int < 0 or contact_number_int > len(spisok_kontaktov):
        # vibor poradkovogo nomera kontakta
        contact_number_int = int(
            input('Enter contact number u want to copy : '))-1
    #     i perevod v 4islovoy  format

    print(spisok_kontaktov[contact_number_int].split(";")[0])

    print(spisok_kontaktov[contact_number_int])

    print(file_names)

    destination_file = input("Enter destination file : ")

    destination_file_data, destination_file_rows_number, file_names = filerowsnumber_filedata(
        destination_file)

    # while destination_file not in file_names:

    #     destination_file = input("Enter destination file : ")

    # with open(destination_file, 'r', encoding='utf-8') as file:
    #     destination_file_data = file.readlines()

    print(f'destination_file_data  : {destination_file_data}')

    destination_row_number = destination_file_rows_number+1

    print(destination_row_number)

    #
    #
    #

    old_name = spisok_kontaktov[contact_number_int].split(";")[1].rstrip()
    old_surname = spisok_kontaktov[contact_number_int].split(";")[2].rstrip()
    old_patronymic = spisok_kontaktov[contact_number_int].split(";")[
        3].rstrip()
    old_phone = spisok_kontaktov[contact_number_int].split(";")[4].rstrip()
    old_Address = spisok_kontaktov[contact_number_int].split(";")[5].rstrip()

    print(spisok_kontaktov[contact_number_int].split(";")[1])
    print(spisok_kontaktov[contact_number_int].split(";")[1])
    print(spisok_kontaktov[contact_number_int].split(";")[2])
    print(spisok_kontaktov[contact_number_int].split(";")[3])
    print(spisok_kontaktov[contact_number_int].split(";")[4])
    print(spisok_kontaktov[contact_number_int].split(";")[5])

    new_contact_data = f'{destination_row_number};{old_name};{old_surname};{old_patronymic};{old_phone};{old_Address}\n'

    print(new_contact_data)

    # with open(destination_file, 'a', encoding='UTF-8') as accounts:
    #     accounts.write(new_contact_data)

    file_append(new_contact_data, destination_file)
    print_data(destination_file)


# copy_contact()

# input_file1 = input("Enter sourcefilename : ")
# input_file2 = input("Enter destinatonfilename : ")
# file_append(input_file1)


###
###
