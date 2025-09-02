def menu(options):
    while True:
        choice = input(f'Choose: {options}').strip()
    
        if choice in options:    # is the user's entered string one of the items in options?
            return choice


if __name__ == '__main__':
    user_entered_choices = input('Enter choices, separated by spaces: ').split()

    user_choice = menu(user_entered_choices)

    print(f'You chose {user_choice}')