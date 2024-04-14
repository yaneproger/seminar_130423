

def file_read():
    with open('accounts.txt', 'r', encoding='UTF-8') as accounts:
        return accounts.read()


def file_readlines():
    with open('accounts.txt', 'r', encoding='utf-8') as accounts:
        return accounts.readlines()


def file_append(data=''):
    with open('accounts.txt', 'a', encoding='UTF-8') as accounts:
        accounts.write(data)


def file_rewrite(data=''):
    with open('accounts.txt', 'w', encoding='UTF-8') as accounts:
        accounts.write(data)


def file_rewritelines(data=''):
    with open('accounts.txt', 'w', encoding='UTF-8') as accounts:
        accounts.writelines(data)


def input_data():
    spisok_kontaktov = file_readlines()
    print(f'len(spisok_kontaktov)  {len(spisok_kontaktov) }')
    row_number = len(spisok_kontaktov)+1
    name = input("Enter name : ")
    surname = input("Enter surname : ")
    patronymic = input("Enter patronymic : ")
    phone = input("Enter phone :")
    address = input("Enter address :")
    contact_data = f'{row_number};{name};{surname};{patronymic};{phone};{address}\n'
    file_append(contact_data)


# input_data()


def print_data():
    return print(file_read())


# print_data()


def search_contact():
    spisok_kontaktov = file_read().strip().split('\n')
    print_data()
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
    spisok_kontaktov = file_read().strip().split('\n')
    # print(spisok_kontaktov)
    for kontakt in spisok_kontaktov:
        kontakt_params = kontakt.split(";")
        # print(kontakt_params)

        if search_data in kontakt_params[search_index]:
            print(kontakt)


search_contact()


def change_contact():  # vivod menu

    # Logika dannoy funkcii sostoit v tom ctobi menat soderjimoe
    # vsego kontakta/stroki iz spiska kontaktov - 1-oe menu
    # a takje menat soderjimoe elementov  samogo kontaka/stroki - 2-6-e menu
    # 1-oe menu vipolnayetsa v uslovii - if - eto rabotaet

    # 3 -ostalniye menu -2-6 poka polnostyu realizovat ne udayetsa
    # eto uslovie  - else :  -posle 144-oy stroki -
    # problema s ciklom -
    # samu zapis naxoju - no tak kak ispolzuyu 2-voynoy cikl
    # to zapis otrabativaet mnogo raz
    # i plus ne polu4aetsa vnesti izmeneniya v stroku

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

    spisok_kontaktov = file_readlines()  # 4itaet fayl vozvrawaet Spisok Strok
    print([spisok_kontaktov])
    # print(*file_read().strip().split("\n"))
    print_data()
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

        # print(spisok_kontaktov)

        # file_rewrite(spisok_kontaktov)
        # with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
        #     accounts.writelines(spisok_kontaktov)

        # with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
        #     accounts.writelines(spisok_kontaktov)
        # # print(*file_read().strip().split("\n"))
        # print_data()

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

    file_rewritelines(spisok_kontaktov)

    # with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
    #     accounts.writelines(spisok_kontaktov)
    # print(*file_read().strip().split("\n"))
    print_data()

    # problemi v etoy 4asti -
    # posle vibora etix punktov upravlenie idet suda
    # tut po planu mi izmenayem sostavlayuwue strok
    # dla etogo
    #   '2. Name\n'
    #   '3. Surname\n'
    #   '4. Patronymic\n'
    #   '5. Address\n'
    #   '6. Phone\n'

    # spisok_kontaktov = file_read().strip().split("\n")
    # # polu4ayu  spisok strok razdelenniy po perevodu stroki "\n" i ubirayem probeli
    # print(spisok_kontaktov)
    # print(type(spisok_kontaktov))

    # # vvodim iskomoe zna4eniye dla zameni
    # search_data = input("Enter search data : ")
    # for kontakt in spisok_kontaktov:    # iwem stroku v spiske
    #     for element in kontakt:         # iwem v  kajdoy stroke  spiska
    #         # print(f'kontakt  {kontakt}')
    #         element = kontakt.split(";")
    #         # razdelayem stroku po ' ; ' - razdelitelu
    #         # print(f'element[search_index]  {element[search_index]}')
    #         print(f'element  {element}')

    # data=[spisok_kontaktov[i].split(";")[1] for i in spisok_kontaktov]

    # print(spisok_kontaktov[contact_number_int-1].split(";")[1])

    #                 old_name = spisok_kontaktov[contact_number_int-1].split(";")[1]
    # old_surname = spisok_kontaktov[contact_number_int-1].split(";")[2]
    # old_patronymic = spisok_kontaktov[contact_number_int-1].split(";")[3]
    # old_phone = spisok_kontaktov[contact_number_int-1].split(";")[4]
    # old_address = spisok_kontaktov[contact_number_int-1].split(";")[5]

#                 if search_data in element[search_index]:  #
#                     #   zdesiwem element s indeksom otsuda  i minus odin  -1->
#                     # ->
#                     #   '2. Name\n'
#                     #   '3. Surname\n'
#                     #   '4. Patronymic\n'
#                     #   '5. Address\n'
#                     #   '6. Phone\n'
#                     #
#                     print(f'element[search_index] {element[search_index]}')
#                     #    pe4ataem naydenniy element

#                     entered_data = input("Enter data to change : ")
#                     # vvodim zna4enie dla zapisi vmesto naydennogo zna4eniya
#                     element[search_index] = entered_data
#                     # prisvaivaem vvedennoe zna4enie
#                     print(spisok_kontaktov)
#                 else:
#                     print("wrong input")
#                     break

# # Zdes ne udayetsa zapisat zna4eniye

# i vtoroe -
# ya ispolzoval 2-voynoy cikl - on naxodit zna4eniye neskolko raz

    # A takje problema s obratnoy sborkoy stroki v prevona4alniy vid i zapisi ee v fayl

    #         with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
    #             accounts.write(
    #                 " ".join([str(el) for el in spisok_kontaktov]))

    # with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
    #     accounts.writelines(spisok_kontaktov)


# change_contact()


def delete_contact():

    spisok_kontaktov = file_readlines()  # 4itaet fayl vozvrawaet Spisok Strok
    print([spisok_kontaktov])
    # print(*file_read().strip().split("\n"))
    print_data()
    print(f'len(spisok_kontaktov)  {len(spisok_kontaktov) }')
    # vibor poradkovogo nomera kontakta
    contact_number_int = int(input('Enter contact number u want to delete : '))
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

    file_rewritelines(spisok_kontaktov)
    print("Kontakt deleted")
    print_data()


# delete_contact()


def copy_contact():

    spisok_kontaktov = file_readlines()  # 4itaet fayl vozvrawaet Spisok Strok
    print([spisok_kontaktov])
    # print(*file_read().strip().split("\n"))
    print_data()
    print(f'len(spisok_kontaktov)  {len(spisok_kontaktov) }')
    # vibor poradkovogo nomera kontakta
    contact_number_int = int(input('Enter contact number u want to delete : '))
    #     i perevod v 4islovoy  format


###
###


def interface():
    file_append()
    user_data = ''
    while user_data != '5':
        print('Select ur choice : \n'
              '1. Print data\n'
              '2. Search data\n'
              '3. Add data\n'
              '4. Copy data\n'
              '5. Exit\n'
              )
        user_data = input("Enter operation number : ")
        while user_data not in ('1', '2', '3', '4', '5'):
            user_data = input("Enter operation number : ")
        match user_data:
            case '1':
                print_data()
            case '2':
                search_contact()
            case '3':
                input_data()
            case '4':
                print('\nthis option is under construction\n')
                pass
            case '5':
                print('Game over')


# change_row()
# input_data()
# print_data()
# search_contact()
# change_contact()
# interface()
