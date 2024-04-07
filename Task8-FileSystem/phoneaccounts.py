

# Урок 8. Работа с файлами

# Задача №49. Решение в группах
# Создать телефонный справочник
# с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для
# поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.


# 1.Создать и открыть файл для добавления данных. ++++++++++++++++++++++
#   -обратиться к файлу accounts.txt в режиме "а" аппенд +++++++++++++++++++++++++
#   -( with open('accounts.txt', 'a', encoding='UTF-8') as phoneaccounts) ++++++++++++++

# def append_data():
# 	data=input("enter data: ")
# 	with open('accounts.txt', 'a', encoding='UTF-8') as phoneaccounts
# 		phoneaccounts.write(f'{data}\n')

# 2.Ввод данныж (запись контакта) ++++++++++++++++++++++++++++
#   -получить от пользователя данные по контакту ++++++++++++++++++++++
#   -подготовить данные, чтобы они были в нужном нам формате  ++++++++++++++++++++++
#   -обратиться к файлу accounts.txt в режиме "а" аппенд  ++++++++++++++++++++++
#   -добавить полученные данные +++++++++++++++++++++++++

# def input_data():
#     name = input('enter name: ')
#     surname = input('enter surname: ')
#     patronymic = input('enter patronymic: ')
#     address = input('enter address: ')
#     phone = input('enter phone: ')
#     data = (f'\n{name};{surname};{patronymic};{address};{phone}\n')
#     append_data(data)


# 3.Вывод данных на экран   +++++++++++++++++++++++++
#   -обратиться к файлу accounts.txt в режиме "р" рид +++++++++++++++++
#   -вывести на экран все данные из файла  +++++++++++++++++++++++++++++

# def print_data():
#     with open('accounts.txt', 'r', encoding='UTF-8') as phoneaccounts:
#         data = (f'Data output:{phoneaccounts.readlines()}')
#         print(('\n').join(data.split('\\n')))


# 4.Пользовательский поиск по характеристике ( имени,фамилии,телефону)  +++++++++
#   -Выбрать вариант поиска( по имени,фамилии,телефону) +++++++++++++++++++
#   -получить данные для поиска ++++++++++++++++++++++++++++++++++++
#   -обратиться к файлу accounts.txt в режиме "р" рид ++++++++++++++++++++
#   -поиск по файлу +++++++++++++++++++++++++++++++++++++++++
#   -вывод на экран при совпадении +++++++++++++++++++++++++++

# def search_data():
#     print("Select your search type: \n"
#           "1.name\n"
#           "2.surname\n"
#           "3.patronymic\n"
#           "4.address\n"
#           "5.phone\n ")
#     input_data = input(" : ")

#     while input_data not in ("1", "2", "3", "4", "5"):
#         print("Wrong input")
#         input_data = input("Select your search type:")

#     type_search_index = int(input_data) - 1
#     print(f'type_index_search {type_search_index}')
#     search_input = input("Enter search data: ")
#     accounts_data = read_data().split('\n\n')
#     # print(f'accounts_data{accounts_data}')
#     for account in accounts_data:
#         replaced_acc_data = account.replace('\n', ' ').split()
#         # print(f'Len account : {len(account)}')
#         # print(f'account : {account}')
#         # print(f'Len replaced_acc_data : {len(replaced_acc_data)}')
#         # print(f'replaced_acc_data{replaced_acc_data}')
#         if search_input in replaced_acc_data[type_search_index]:
#             print(f'Result Data: {replaced_acc_data[type_search_index]}')
#             print(account)


# 5.Интерфейс для пользователя
#   -сделать для пользователя выбор действий.


# def append_data():
#     newdata = input("Enter data :")
#     with open('accounts.txt', 'a', encoding='UTF-8') as phoneaccounts:
#         phoneaccounts.write(f'{newdata}\n')

# def append_data(newdata):
#     with open('accounts.txt', 'a', encoding='UTF-8') as phoneaccounts:
#         phoneaccounts.write(f'{newdata}\n')

# def name():
#     return input('enter name: ')
# def surname():
#     return input('enter surname: ')
# def patronymic():
#     return input('enter patronymic: ')
# def address():
#     return input('enter address: ')
# def phone():
#     return input('enter phone: ')

def read_data():
    with open('accounts.txt', 'r', encoding='UTF-8') as phoneaccounts:
        # data = phoneaccounts.read()
        # data = (f'{phoneaccounts.readlines()}')
        # print(type(data))
        # return data
        return phoneaccounts.read()


def print_data():
    with open('accounts.txt', 'r', encoding='UTF-8') as phoneaccounts:
        data = (f'Data output:{phoneaccounts.readlines()}')
        # data = (f'{phoneaccounts.readlines()}')
        print(('\n').join(data.split('\\n', )))
        # print(data.split('\\n'))


def append_data(newdata):
    with open('accounts.txt', 'a', encoding='UTF-8') as phoneaccounts:
        phoneaccounts.write(newdata)


def input_data():
    name = input('enter name: ')
    surname = input('enter surname: ')
    patronymic = input('enter patronymic: ')
    address = input('enter address: ')
    phone = input('enter phone: ')
    data = (f'\n{name} {surname} {patronymic} {address} {phone}\n')
    append_data(data)


def search_data():
    print("Select your search type 1 : \n"
          "1.name\n"
          "2.surname\n"
          "3.patronymic\n"
          "4.address\n"
          "5.phone\n ")
    input_data = input(" : ")

    while input_data not in ("1", "2", "3", "4", "5"):
        print("Wrong input")
        input_data = input("Select your search type 2 :")
        print(input_data)

    type_search_index = int(input_data) - 1
    print(f'type_search_index {type_search_index}')
    search_input = input("Enter search data: ")
    print(f'search_input {search_input}')
    accounts_data = read_data().split('\n\n')
    print(f'accounts_data{accounts_data}')
    for account in accounts_data:
        replaced_acc_data = account.replace('\n', ' ').split()

        # print(f'Len account : {len(account)}')
        # print(f'account : {account}')
        # print(f'Len replaced_acc_data : {len(replaced_acc_data)}')
        print(f'replaced_acc_data{replaced_acc_data}')
        if search_input in replaced_acc_data[type_search_index]:
            print(f'Result Data: {replaced_acc_data[type_search_index]}')
            print(account)


def user_interface():
    entered_data = None
    while entered_data != '4' or entered_data >= '5':
        print("Menu 3 :\n"
              "1.Add contact\n"
              "2.find contact\n"
              "3.print contacts\n"
              "4.exit\n")
        # command = input("Select menu number : ")
        entered_data = input("Select menu number 5 : ")

        while entered_data not in ("1", "2", "3", "4"):
            print("Wrong input")
        else:
            # entered_data = input("Select your search type 4 :")
            match entered_data:
                case '1':
                    input_data()
                case '2':
                    search_data()
                case '3':
                    print_data()
                case '4':
                    print('Game over')


user_interface()
