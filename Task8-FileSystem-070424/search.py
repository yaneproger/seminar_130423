

from slave import *


def search_contact():

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

    # spisok_kontaktov = file_read().strip().split('\n')
    print_data(source_file)
    print(f'{rowscount} entries')
    print()
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
