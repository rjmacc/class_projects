#Ryan MacDonell


def get_falling_input():
    '''gets the input for the falling row in the form F (column #) (letter) (letter) (letter)'''
    falling_input = input()
    if falling_input == 'Q':
        return falling_input
    elif falling_input == '<':
        return falling_input
    elif falling_input == '>':
        return falling_input
    elif falling_input == 'R':
        return falling_input
    elif falling_input == '':
        return falling_input
    elif falling_input[0] == 'F':
        return falling_input
    else:
        print('ERROR')
        return get_falling_input()
    





            
