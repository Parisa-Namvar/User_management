from re import match



def number_validator(number):
    return match(r'^[\w\d]{8}' ,number)



def username_validation(user_name):
    return match(r'^[a-zA-Z][\w.]{7,19}$' ,user_name)


def nick_name_validation(nickname):
    return match(r'^[a-zA-Z][\w.]{2,29}$', nickname)

