import question_b

menu = 1
while menu >=1:
    print('')
    print(' ________________________________________ ')
    print('|                                        |')
    print('|   1 - Display Stock Purchace History   |')
    print('|   2 - Quit                             |')
    print('|________________________________________|')
    print('')
    select = input('')
    print('')
    if select:
        menu = 2
    while menu ==2:
        try:
            choice = int(select)
        except:
            print('Error: please enter the number of the desired option.')
            print('')
            break
        if choice == 2:
            quit()
        elif choice == 1:
            question_b.stock_purchace_history()
        else:
            print('Error: Please enter the number of an option on the list. you entered: '+str(choice))
            print('')
        menu = 1