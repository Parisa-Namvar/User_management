from farayandha import *


while True:
    option = show_menu()
    match option:
         case '0':
             break
         case '1':
            print(1)
         case '2':
            print(2)
         case '3':
            print(3)
         case _:
             print('invalid option!!! you should choose from among thr option')
    print('-'*50)