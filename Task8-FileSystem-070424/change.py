

from slave import *


def change_contact():  # vivod menu

    # Logika dannoy funkcii sostoit v tom ctobi menat soderjimoe
    # vsego kontakta/stroki iz spiska kontaktov - eto 1-oe menu
    # a takje  - menu -2-6 - menat soderjimoe elementov  samogo kontaka/stroki - 2-6-e menu
    # 1-oe menu vipolnayetsa v uslovii - if - eto rabotaet

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
