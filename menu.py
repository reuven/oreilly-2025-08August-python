def menu(options):
    while True:
        choice = input('Choose: ').strip()
    
        if choice in options:    # is the user's entered string one of the items in options?
            return choice
