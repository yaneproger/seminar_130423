

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


print_data()


def search_contact():
    print('Select from : \n'
          '1. Contact number\n'
          '2. Name\n'
          '3. Surname\n'
          '4. Patronymic\n'
          '5. Address\n'
          '6. Phone\n'
          )
    user_data = input("Select search type : ")
    while user_data not in ('1', '2', '3', '4', '5', '6'):
        user_data = input("Select search type : ")

    search_index = int(user_data)-1
    # Minus 1, tak kak indexaciya na4inayetsa s 0-la

    search_data = input("Enter search data : ")
    spisok_kontaktov = file_read().strip().split('\n\n')
    print(spisok_kontaktov)
    for kontakt in spisok_kontaktov:
        kontakt_params = kontakt.replace("\n", " ").split()

        if search_data in kontakt_params[search_index]:
            print(kontakt)

# search_contact()


def change_contact():
    print('Select from : \n'
          '1. Whole contact\n'
          '2. Name\n'
          '3. Surname\n'
          '4. Patronymic\n'
          '5. Address\n'
          '6. Phone\n'
          )
    user_data = input("Select search type : ")
    while user_data not in ('1', '2', '3', '4', '5', '6'):
        user_data = input("Select search type : ")

    search_index = int(user_data)-1
    # Minus 1, tak kak indexaciya na4inayetsa s 0-la

    spisok_kontaktov = file_readlines()

    # print(*file_read().strip().split("\n"))
    print_data()
    contact_number = int(input('Enter contact number u want to change : '))

    if search_index == 0:
        contact_number_int = int(contact_number)
        print("'Enter contact's new data'")

        # spisok_kontaktov = file_read().strip().split('\n')
        print(f'len(spisok_kontaktov)  {len(spisok_kontaktov) }')
        row_number = contact_number_int

        name = input("Enter name : ")
        surname = input("Enter surname : ")
        patronymic = input("Enter patronymic : ")
        phone = input("Enter phone :")
        address = input("Enter address :")
        # contact_data = f'{row_number} {name} {surname} {patronymic} {phone} {address}'
        spisok_kontaktov[contact_number_int -
                         1] = f'{row_number};{name};{surname};{patronymic};{phone};{address}\n'

        # print(spisok_kontaktov)

        # file_rewrite(spisok_kontaktov)
        # with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
        #     accounts.writelines(spisok_kontaktov)

        with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
            accounts.writelines(spisok_kontaktov)
        # print(*file_read().strip().split("\n"))
        print_data()

    else:
        # pass

        spisok_kontaktov = file_read().strip().split("\n")
        print(spisok_kontaktov)

        search_data = input("Enter search data : ")
        for kontakt in spisok_kontaktov:
            for temp in kontakt:

                temp = kontakt.split(";")
                print(f'temp[contact_number]  {temp[contact_number]}')
                print(f'temp  {temp}')

                if search_data in temp[contact_number]:
                    print(f'temp[search_index] {temp[search_index]}')
                    entered_data = input("Enter data to change : ")
                    temp[search_index] = entered_data
                    print(spisok_kontaktov)
                else:
                    print("wrong input")
                    break

        # with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
        #     # accounts.writelines(
        #     # " ".join([str(el) for el in spisok_kontaktov]))
        #     accounts.writelines(spisok_kontaktov)
        #     print(*file_read().strip().split("\n"))

            # for position in kontakt:s
            # print(f'position {position}')
            # print(f'len position {len(position)}')

            # kontakt_params = kontakt.replace("\n", " ").split()
            # print(f'kontakt_params {kontakt_params}')
            # print(f'search_index {search_index}')
            # print(f'contact_number {contact_number}')
            # if contact_number in kontakt_params[0]:
            #     if search_data in kontakt_params:
            #         data_to_be_written = input(
            #             "Enter data to be written : ")

            #         kontakt_params[search_index] = data_to_be_written
            #         spisok_kontaktov[contact_number_int-1] = kontakt_params
            #         # file_rewrite(spisok_kontaktov)
            #         print(spisok_kontaktov)

            #         with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
            #             accounts.write(
            #                 " ".join([str(el) for el in spisok_kontaktov]))

            # with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
            #     accounts.writelines(spisok_kontaktov)


change_contact()


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
