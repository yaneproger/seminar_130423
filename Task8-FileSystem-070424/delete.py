

from slave import *


def delete_contact():

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

    # spisok_kontaktov = file_readlines()  # 4itaet fayl vozvrawaet Spisok Strok
    # print([spisok_kontaktov])
    if len(spisok_kontaktov) == 0:
        print("kontaktov net")
    else:

        # print(*file_read().strip().split("\n"))
        print_data(source_file)
        print(f'{rowscount} entries')
        print()
        # print(f'len(spisok_kontaktov)  {len(spisok_kontaktov) }')
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
