

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

def change_contact():  # vivod menu
    print('Select from : \n'
          '1. Whole contact\n'
          '2. Name\n'
          '3. Surname\n'
          '4. Patronymic\n'
          '5. Address\n'
          '6. Phone\n'
          )
    # vvod simvola dla ispolzovaniya kak index
    user_data = input("Select search type : ")
    while user_data not in ('1', '2', '3', '4', '5', '6'):
        user_data = input("Select search type : ")

    search_index = int(user_data)-1  # perevod v 4islovoy format
    # Minus 1, tak kak indexaciya na4inayetsa s 0-la

    spisok_kontaktov = file_readlines()  # 4itaet fayl vozvrawaet Spisok Strok

    # print(*file_read().strip().split("\n"))
    print_data()
    # vibor poradkovogo nomera kontakta
    contact_number_int = int(input('Enter contact number u want to change : '))
    #     i perevod v 4islovoy  format

    if search_index == 0:   # esli mi vibrali perviy punkt menu - Zamena Vsego kontakta to index==0
        # i poisk idet po nomeram kontaktov

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

        with open(f'accounts.txt', 'w', encoding='UTF-8') as accounts:
            accounts.writelines(spisok_kontaktov)
        # print(*file_read().strip().split("\n"))
        print_data()

    else:

        # problemi v etoy 4asti -
        # posle vibora etix punktov upravlenie idet suda
        # tut po planu mi izmenayem sostavlayuwue strok
        # dla etogo
        #   '2. Name\n'
        #   '3. Surname\n'
        #   '4. Patronymic\n'
        #   '5. Address\n'
        #   '6. Phone\n'

        spisok_kontaktov = file_read().strip().split("\n")
        # polu4ayu  spisok strok razdelenniy po perevodu stroki "\n" i ubirayem probeli
        print(spisok_kontaktov)
        print(type(spisok_kontaktov))

        # vvodim iskomoe zna4eniye dla zameni
        search_data = input("Enter search data : ")
        for kontakt in spisok_kontaktov:    # iwem stroku v spiske
            for element in kontakt:         # iwem v  kajdoy stroke  spiska
                # print(f'kontakt  {kontakt}')
                element = kontakt.split(";")
                # razdelayem stroku po ' ; ' - razdelitelu
                # print(f'element[search_index]  {element[search_index]}')
                print(f'element  {element}')

                if search_data in element[search_index]:  #
                    #   zdesiwem element s indeksom otsuda  i minus odin  -1->
                    # ->
                    #   '2. Name\n'
                    #   '3. Surname\n'
                    #   '4. Patronymic\n'
                    #   '5. Address\n'
                    #   '6. Phone\n'
                    #
                    print(f'element[search_index] {element[search_index]}')
                    #    pe4ataem naydenniy element

                    entered_data = input("Enter data to change : ")
                    # vvodim zna4enie dla zapisi vmesto naydennogo zna4eniya
                    element = entered_data
                    # prisvaivaem vvedennoe zna4enie
                    print(spisok_kontaktov)
                else:
                    print("wrong input")
                    break

# Zdes ne udayetsa zapisat zna4eniye

# i vtoroe -
# ya ispolzoval 2-voynoy cikl - on naxodit zna4eniye neskolko raz

                # A takje problema s obratnoy sborkoy stroki v prevona4alniy vid i zapisi ee v fayl

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
