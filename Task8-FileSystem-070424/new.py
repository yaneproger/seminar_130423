

def filerowsnumber_filedata(input_file_name):

    import os

    file_names = []

    for filename in os.listdir("."):
        file_names.append(filename)

    print(file_names)

    source_file = input_file_name
    # print(f'source_file  : {source_file}')

    while source_file not in file_names:
        source_file = str(input("Enter source text file : "))

    print(f'source_file  : {source_file}')
    print(f'source_file type  : {type(source_file)}')
    # print("Select source file :")

    with open(source_file, 'r', encoding='utf-8') as file:
        source_file_data = file.readlines()

    print(f'source_file_data  : {source_file_data}')
    # print(data)

    # spisok_kontaktov = source_file_data  # 4itaet fayl vozvrawaet Spisok Strok

    file_rows_number = len(source_file_data)

    return source_file_data, file_rows_number, file_names


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
#     # spisok_kontaktov = source_file_data  # 4itaet fayl vozvrawaet Spisok Strok
#     file_rows_number = len(source_file_data)
#     return source_file_data, file_rows_number, file_names

#
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


def file_rewritelines(data, filename):
    with open(filename, 'w', encoding='UTF-8') as accounts:
        accounts.writelines(data)


def print_data(filename):
    return print(file_read(filename))


def print_contacts():

    import os
    file_names = []
    for filename in os.listdir("."):
        file_names.append(filename)
    print(file_names)
    source_file = str(input("Enter source file : "))
    spisok_kontaktov, rowscount, file_names = filerowsnumber_filedata(
        source_file)

    print(*file_names)

    print(spisok_kontaktov)
    print(rowscount)
    print_data(source_file)


def input_data():

    import os

    file_names = []

    for filename in os.listdir("."):
        file_names.append(filename)

    print(file_names)

    source_file = str(input("Enter source file : "))

    spisok_kontaktov, rowscount, file_names = filerowsnumber_filedata(
        source_file)

    print(*file_names)

    print(spisok_kontaktov)
    print(rowscount)

    print_data(source_file)

    # spisok_kontaktov = file_readlines()
    print(f'len(spisok_kontaktov)  {len(spisok_kontaktov) }')
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


def search_contact():

    import os

    file_names = []

    for filename in os.listdir("."):
        file_names.append(filename)

    print(file_names)

    source_file = str(input("Enter source file : "))

    spisok_kontaktov, rowscount, file_names = filerowsnumber_filedata(
        source_file)

    print(*file_names)

    print(spisok_kontaktov)
    print(rowscount)

    # spisok_kontaktov = file_read().strip().split('\n')
    print_data(source_file)
    # print(spisok_kontaktov)
    print('Select from : \n'
          '1. Contact number\n'
          '2. Name\n'
          '3. Surname\n'
          '4. Patronymic\n'
          '5. Phone\n'
          '6. Address\n'
          )
    user_data = input("Select search type : ")
    while user_data not in ('1', '2', '3', '4', '5', '6'):
        user_data = input("Select search type : ")

    search_index = int(user_data)-1
    # Minus 1, tak kak indexaciya na4inayetsa s 0-la

    search_data = input("Enter search data : ")
    # spisok_kontaktov = file_read().strip().split('\n')
    # print(spisok_kontaktov)
    for kontakt in spisok_kontaktov:
        kontakt_params = kontakt.split(";")
        # print(kontakt_params)

        if search_data in kontakt_params[search_index]:
            print(*kontakt_params)


# search_contact()


def change_contact():  # vivod menu

    # Logika dannoy funkcii sostoit v tom ctobi menat soderjimoe
    # vsego kontakta/stroki iz spiska kontaktov - eto 1-oe menu
    # a takje  - menu -2-6 - menat soderjimoe elementov  samogo kontaka/stroki - 2-6-e menu
    # 1-oe menu vipolnayetsa v uslovii - if - eto rabotaet

    import os

    file_names = []

    for filename in os.listdir("."):
        file_names.append(filename)

    print(file_names)

    source_file = str(input("Enter source file : "))

    spisok_kontaktov, rowscount, file_names = filerowsnumber_filedata(
        source_file)

    print(*file_names)

    print(spisok_kontaktov)
    print(rowscount)

    print('Select from : \n'
          '1. Whole contact\n'
          '2. Name\n'
          '3. Surname\n'
          '4. Patronymic\n'
          '5. Phone\n'
          '6. Address\n'
          )
    # vvod simvola dla ispolzovaniya kak index
    user_data = input("Select search type : ")
    while user_data not in ('1', '2', '3', '4', '5', '6'):
        user_data = input("Select search type : ")

    search_index = int(user_data)-1  # perevod v 4islovoy format
    # Minus 1, tak kak indexaciya na4inayetsa s 0-la

    # spisok_kontaktov = file_readlines()  # 4itaet fayl vozvrawaet Spisok Strok
    # print([spisok_kontaktov])
    # print(*file_read().strip().split("\n"))
    print_data(source_file)
    print(f'contacts count : {rowscount}')
    # vibor poradkovogo nomera kontakta
    contact_number_int = int(input('Enter contact number u want to change : '))
    #     i perevod v 4islovoy  format

    # vvodim peremennie   elementov(podstroki)  stroki  Spiska kontaktov

    old_name = spisok_kontaktov[contact_number_int-1].split(";")[1].rstrip()
    old_surname = spisok_kontaktov[contact_number_int-1].split(";")[2].rstrip()
    old_patronymic = spisok_kontaktov[contact_number_int -
                                      1].split(";")[3].rstrip()
    old_phone = spisok_kontaktov[contact_number_int-1].split(";")[4].rstrip()
    old_Address = spisok_kontaktov[contact_number_int-1].split(";")[5].rstrip()

    print(spisok_kontaktov[contact_number_int-1].split(";")[1])
    print(spisok_kontaktov[contact_number_int-1].split(";")[1])
    print(spisok_kontaktov[contact_number_int-1].split(";")[2])
    print(spisok_kontaktov[contact_number_int-1].split(";")[3])
    print(spisok_kontaktov[contact_number_int-1].split(";")[4])
    print(spisok_kontaktov[contact_number_int-1].split(";")[5])

    if search_index == 0:   # esli mi vibrali perviy punkt menu - Zamena Vsego kontakta to index==0
        # indeks zapisi berem iz peremennoy contact_number_int-1

        print("'Enter contact's new data'")

        # spisok_kontaktov = file_read().strip().split('\n')
        print(f'len(spisok_kontaktov)  {len(spisok_kontaktov) }')

        name = input("Enter name : ")
        surname = input("Enter surname : ")
        patronymic = input("Enter patronymic : ")
        phone = input("Enter phone :")
        address = input("Enter address :")

        spisok_kontaktov[contact_number_int -
                         1] = f'{contact_number_int};{name};{surname};{patronymic};{phone};{address}\n'

    if search_index == 1:

        new_name = input("Enter_contact's new name : ")
        spisok_kontaktov[contact_number_int -
                         1] = f'{contact_number_int};{new_name};{old_surname};{old_patronymic};{old_phone};{old_Address}\n'

    if search_index == 2:

        new_surname = input("Enter_contact's new surname : ")
        spisok_kontaktov[contact_number_int -
                         1] = f'{contact_number_int};{old_name};{new_surname};{old_patronymic};{old_phone};{old_Address}\n'

    if search_index == 3:

        new_patronymic = input("Enter_contact's new patronymic : ")
        spisok_kontaktov[contact_number_int -
                         1] = f'{contact_number_int};{old_name};{old_surname};{new_patronymic};{old_phone};{old_Address}\n'

    if search_index == 4:

        new_phone = input("Enter_contact's new phone : ")
        spisok_kontaktov[contact_number_int -
                         1] = f'{contact_number_int};{old_name};{old_surname};{old_patronymic};{new_phone};{old_Address}\n'

    if search_index == 5:

        new_Address = input("Enter_contact's new Address : ")
        spisok_kontaktov[contact_number_int -
                         1] = f'{contact_number_int};{old_name};{old_surname};{old_patronymic};{old_phone};{new_Address}\n'

    file_rewritelines(spisok_kontaktov, source_file)

    # with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
    #     accounts.writelines(spisok_kontaktov)
    # print(*file_read().strip().split("\n"))
    print_data(source_file)

    # # vvodim iskomoe zna4eniye dla zameni
    # search_data = input("Enter search data : ")

    # data=[spisok_kontaktov[i].split(";")[1] for i in spisok_kontaktov]

    # print(spisok_kontaktov[contact_number_int-1].split(";")[1])

    #                 old_name = spisok_kontaktov[contact_number_int-1].split(";")[1]
    # old_surname = spisok_kontaktov[contact_number_int-1].split(";")[2]
    # old_patronymic = spisok_kontaktov[contact_number_int-1].split(";")[3]
    # old_phone = spisok_kontaktov[contact_number_int-1].split(";")[4]
    # old_address = spisok_kontaktov[contact_number_int-1].split(";")[5]

    #         with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
    #             accounts.write(
    #                 " ".join([str(el) for el in spisok_kontaktov]))

    # with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
    #     accounts.writelines(spisok_kontaktov)


# change_contact()


def delete_contact():

    import os

    file_names = []

    for filename in os.listdir("."):
        file_names.append(filename)

    print(file_names)

    source_file = str(input("Enter source file : "))

    spisok_kontaktov, rowscount, file_names = filerowsnumber_filedata(
        source_file)

    print(*file_names)

    print(spisok_kontaktov)
    print(rowscount)

    # spisok_kontaktov = file_readlines()  # 4itaet fayl vozvrawaet Spisok Strok
    # print([spisok_kontaktov])
    if len(spisok_kontaktov) == 0:
        print("kontaktov net")
    else:

        # print(*file_read().strip().split("\n"))
        print_data(source_file)
        print(f'len(spisok_kontaktov)  {len(spisok_kontaktov) }')
        # vibor poradkovogo nomera kontakta
        contact_number_int = int(
            input('Enter contact number u want to delete : '))
        #     i perevod v 4islovoy  format
        while contact_number_int not in (range(1, len(spisok_kontaktov)+1)):
            print('Enter contact number u want to delete')
            contact_number_int = int(input())

        print(spisok_kontaktov[contact_number_int-1])

        del spisok_kontaktov[contact_number_int-1]

        spisok_kontaktov = [f'{i + 1};{spisok_kontaktov[i].split(";")[1]};'
                            f'{spisok_kontaktov[i].split(";")[2]};'
                            f'{spisok_kontaktov[i].split(";")[3]};'
                            f'{spisok_kontaktov[i].split(";")[4]};'
                            f'{spisok_kontaktov[i].split(";")[5]}'
                            for i in range(len(spisok_kontaktov))]

        file_rewritelines(spisok_kontaktov, source_file)
        print("Kontakt deleted")
        print_data(source_file)


# delete_contact()


#
#


#
#


#

#

#

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

    for filename in os.listdir("."):
        file_names.append(filename)

    print(file_names)

    source_file = str(input("Enter source file : "))

    spisok_kontaktov, rowscount, file_names = filerowsnumber_filedata(
        source_file)

    print(*file_names)

    print(spisok_kontaktov)
    print(rowscount)

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
    print_data(source_file)
    print(f'len(spisok_kontaktov)  {len(spisok_kontaktov) }')

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


def interface():
    user_data = ''
    while user_data != '7':
        print('Select ur choice : \n'
              '1. Print data\n'
              '2. Search data\n'
              '3. Add data\n'
              '4. Copy data\n'
              '5. Delete data\n'
              '6. Change contact\n'
              '7. Exit\n'
              )
        user_data = input("Enter operation number : ")
        while user_data not in ('1', '2', '3', '4', '5', '6', '7'):
            user_data = input("Enter operation number : ")
        match user_data:
            case '1':
                print_contacts()
            case '2':
                search_contact()
            case '3':
                input_data()
            case '4':
                copy_contact()
            case '5':
                delete_contact()
            case '6':
                change_contact()
            case '7':
                print('Game over')


# change_row()
# input_data()
# print_data()
# search_contact()
# change_contact()
interface()
