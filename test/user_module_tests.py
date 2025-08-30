"""
test
def show_menu():
    # نمایش دادن منو
    print('1) Add users')
    print('2) Login check')
    print('3) Show users')
    print('0) Exit')
    print('-'*50)
    # دریافت انتخاب کاربر
    option = input('Enter your choice: ')
    print('-'*50)
    return option

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
             print('invalid option')
    print('-'*50)
    """