import random
import string
import os
"""macke setting"""
settings = {
        'lower': True,
        'upper': True,
        'symbol': True,
        'number': True,
        'space': False,
        'length': 8
}

MAXIMUN_PASWORD_LENGTH = 4
MINIMUM_PASSWORD_LENGTH = 25

def get_user_pass_length(option, default, min = MINIMUM_PASSWORD_LENGTH, max = MAXIMUN_PASWORD_LENGTH ):
    while True:
        user_input = input(f'you kann give length Password: ')
        if user_input == '':
            return default

        if user_input.isdigit():
            user_pass_length = int(user_input)
            if min <= user_pass_length <= max:
                return int(user_input)    
            print('muss pass bitwin 4 < user_input_length < 25 ')
        else:
            print('input is shuld')
        print ('Please try again')

def cler_scren():
    os.system('cls')

def get_yes_or_no_settings(option, default):
     while True:
            user_input = input(f'Shulde {option}'
                                f'(Default is {default})(y = yes, n = no): (Enter is {default}: )')
            if user_input in ['y', 'n']: 
                return user_input == 'y'

            if user_input == '':
                return default
            print('Invalid input. Please try again') 


def generat_random_chr(choices):
    choice = random.choice(choices) 

    if choice == 'lower':
        return random.choice(string.ascii_lowercase)
    elif choice == 'upper':
        return random.choice(string.ascii_uppercase)
    elif choice == 'symbol':
        return random.choice(string.punctuation)
    elif choice == 'number':
        return random.choice(string.digits)
    elif choice == 'space':
        return ' ' 

def ask_if_change_settings(settings):
    while True:
        change_settings = input('Do you want Change settings?'
                                '(y = yes -- n = no -- enter = yes)')
        if change_settings in['y','n','']:
            if change_settings in ['y','']:
                print('-'*5, 'Start change', '-'*5)
                get_setting_from_user(settings)
            break
        else:
            print('Invalid input')
            print('Please try again')


def pass_generator(settings):
    final_pass = ''
    password_length = settings['length']

    choices = list(filter(lambda x: settings[x],['lower','upper','symbol', 'number']))
    for i in range(password_length):
        final_pass += generat_random_chr(choices)
    return f'Your Password is : {final_pass}'


def get_setting_from_user(settings):

    for option, default in settings.items():
        if option != 'length':
            user_chois = get_yes_or_no_settings(option, default)
            settings[option] = user_chois
        else:
            user_pass_length = get_user_pass_length(option,default)
            settings[option] = user_pass_length

def return_paas_2():
    while True:
        want_another_password = input('Do you waant another Password: (y = yes, n= no, Enter = yes): ')   
        if want_another_password in ['y', 'n', '']:
            if want_another_password == 'n':
                return False
            return True
        else:
            print('Invalid input. (Choos from: y = yes, n= no, Enter = yes')
            print('Please try again')

def return_pass_user(settings):
    while True:
        print('-' * 30)
        print(pass_generator(settings))

        if return_paas_2() == False :
            break
            
       
def run():
    cler_scren()
    ask_if_change_settings(settings)
    return_pass_user(settings)
    print('Thank you fur Choosing us.')


run()
