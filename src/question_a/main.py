import question_a

menu = 1
while menu > 0:
    print(' ___________________________________ ')
    print('|                                   |')
    print('| Enter 5 numbers.                  |')
    print('|                                   |')
    print('|___________________________________|')
    print('')
    userNumber1 = input('First number: ')
    print('')
    userNumber2 = input('Second Number: ')
    print('')
    userNumber3 = input('Third Number: ')
    print('')
    userNumber4 = input('Fourth Number: ')
    print('')
    userNumber5 = input('Fifth Number: ')
    menu = 2
    while menu == 2:
        userList = question_a.listMaker(userNumber1,userNumber2,userNumber3,userNumber4,userNumber5)
        question_a.displayList(userList)
        print('Press Enter to exit program.')
        quitCheck = input('')
        menu = 0
