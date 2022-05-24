# This code generates an eight-character password which consists of numbers, lowercase and uppercase letters.
# It asks if the user wants to get a password, and if the answer is 'yes', it gives a random password.

import string
import random

small_letters = list(string.ascii_lowercase)
capital_letters = list(string.ascii_uppercase)
numbers = [i for i in range(10)]


def password_generator():
    small_counter = random.randrange(1, 7)  # 7 not 9 cause there must be at least 2 characters left for a capital and
    # a number
    capital_counter = random.randrange(1, 8 - small_counter)  # 8 cause there must be at least 1 character left for
    # a number
    num_counter = 8 - (small_counter + capital_counter)  # the remaining password positions are occupied by digits

    small_part = ''.join(random.choices(small_letters, k=small_counter))  # part of the password that consists of small
    # letters, the random number was chosen above
    capital_part = ''.join(random.choices(capital_letters, k=capital_counter))  # part of the password that consists of
    # capital letters, the random number was chosen above
    num_part = ''.join(str(i) for i in random.choices(numbers, k=num_counter))  # part of the password that consists
    # of numbers, the random number was chosen above

    unmixed_password = small_part + capital_part + num_part
    mixed_password = ''.join(random.sample(unmixed_password, len(unmixed_password)))
    print(mixed_password, '\n')


while True:
    try:
        choice = int(input('Wanna generate a random eight-character password consisting of at least one capital letter,'
                           ' one small letter and one number?\nEnter 1 for yes or 0 for exit:\n'))
        if choice == 0:
            print('Okay, bye!\n')
            break
        if choice == 1:
            password_generator()
        else:
            print('Wrong number!\n')
    except ValueError:
        print('Enter integers only!\n')
