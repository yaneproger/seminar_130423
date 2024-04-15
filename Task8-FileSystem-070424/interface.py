

from slave import *
from change import *
from copydata import *
from delete import *
from inputdata import *
from search import *


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
# interface()
