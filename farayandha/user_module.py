from validation_module import *

users_list = []

# test passed
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


def add_users():
    # دریافت اطلاعات کاربران و اعتبارسنجی آنها
    #todo سوال؟؟ اگر بخوایم تا وقتی که کاربر اسم معتبر یا رمز معتبر وارد نکرده به مرحله بعدی نریم و به ورودی گرفتن ادامه بدیم این روش (روش زیر) درست است ؟؟؟
    # todo (برای نگرفتن اسم تکراری این روش درست است ؟؟(یک تابع نوشته شده و اینجا استفاده شده
    while True:
        user_name = input('Enter username: ')
        if username_validation(user_name) and uniqe(user_name):
            print('INFO : username saved')
            break
        else:
            print('ERROR : invalid username (maybe username already exists!) try again')

    while True:
        password = input('Enter password: ')
        if number_validator(password):
            print('INFO : password seved')
            break
        else:
            print('ERROR : invalid password!! try again')

    while True:
        nickname = input('Enter nickname: ')
        if nick_name_validation(nickname):
            print('INFO : nickname saved')
            break
        else:
            print('ERROR : invalid nickname!! try again')

    status = input('is account active? (yes/no): ')
    if status == 'yes':
        status = True

    user={
        'username': user_name,
        'password': password,
        'nickname': nickname,
        'status': status
    }

    users_list.append(user)
    # LOG
    print('INFO : USER ADDED SUCCESSFULLY')
    return user


def show_users():
    for person in users_list:
        if person['status']:
            activity = 'OK'
        else:
            activity = 'LOCKED'

        print(f'{person["username"]} ******** {activity}')
        print('-'*25)

    print('-'*50)


def login_check():
    use = input('Enter username to search: ')
    pas = input('Enter account password: ')
    for person in users_list:
        if person['username'] == use and person['password'] == pas:
            if person['status']:
                print('INFO : login successful')
            else:
                print('ERROR : user is locked')
        else:
            print('ERROR : user not found!')

 # کاربر با اسم تکراری ثبت نشود
def uniqe(user_name):
    for user in users_list:
        return user_name != user['username']
