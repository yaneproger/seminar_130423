

def file_read():
    with open('accounts.txt', 'r', encoding='UTF-8') as accounts:
        return accounts.read()


def file_append(data=''):
    with open('accounts.txt', 'a', encoding='UTF-8') as accounts:
        accounts.write(data)


def input_data():

    name = input("Enter u name : ")
    surname = input("Enter ur surname : ")
    patronymic = input("Enter ur patronymic : ")
    address = input("Enter ur address :")
    phone = input("Enter ur phone :")
    contact_data = f'\n{name} {surname} {patronymic} {address} {phone}\n'
    file_append(contact_data)


def print_data():
    return print(file_read())


def search_contact():
    print('Select ur search variants : \n'
          '1. Name\n'
          '2. Surname\n'
          '3. Patronymic\n'
          '4. Address\n'
          '5. Phone\n'
          )
    user_data = input("Select search type : ")
    while user_data not in ('1', '2', '3', '4', '5'):
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


# input_data()
# print_data()
# search_contact()
interface()
