import question_d

menu = 1
table = question_d.create_multiplication_table()
while menu >0:
    print('')
    question_d.display_multiplication_table(table)
    print('')
    select = input('enter Q or Quit to quit the program. ')
    print('')
    try:
        if select.upper()=='Q' or select.upper()=='QUIT':
            menu = 0
            quit()
    except ValueError:
        print('Unexpected error')