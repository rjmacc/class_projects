#Ryan MacDonell

import pygame
import time
white = [255, 255, 255]
black = [0, 0, 0]

purple = [120, 0, 255]
red = [255, 0, 0]
pink = [255, 0, 255]
blue = [0, 0, 255]
green = [0, 255, 0]
teal = [0, 255, 255]
orange = [255, 200, 0]
surface = pygame.display.set_mode((600,600))

def print_game_board(board):
    '''prints the game board that is inputted as the parameter'''
    for i in range(len(board)):
        board_str = ''
        for j in board[i]:
            board_str += j
        print(board_str)

def clear_fallers(board, rows, columns):
    new_board = empty_board(rows, columns)
    for i in range(len(board)):
        for j in range(len(board[i])):
            #print(board[i][j])
            #print(board[i][j][0] == '*')
            if board[i][j][0] == '[' or (board[i][j][0] == '|' and j != 0 and j != len(board[i])-1):
                new_board[i][j] = '   '
            else:
                new_board[i][j] = board[i][j]
    return new_board

def lock_in_place(board, rows, columns):
    new_board = empty_board(rows, columns)
    for i in range(len(board)):
        for j in range(len(board[i])):
            #print(board[i][j])
            #print(board[i][j][0] == '*')
            try:
                if board[i][j][0] == '[':
                    new_board[i][j] = '   '
                elif board[i][j][0] == '|' and j != 0 and j != len(board[i])-1:
                    new_board[i][j] = ' ' + board[i][j][1] + ' '
                else:
                    new_board[i][j] = board[i][j]
            except:
                a = 0
    return new_board

def remove_matched_letters(board, rows, columns):
    '''removes all the letters the program has determined to be matched'''
    new_board = empty_board(rows, columns)
    recently_removed = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            #print(board[i][j])
            #print(board[i][j][0] == '*')
            if board[i][j][0] == '*':
                new_board[i][j] = '   '
                recently_removed += 1
            else:
                new_board[i][j] = board[i][j]
    #print(recently_removed)
    if recently_removed > 0:
        new_board = force_fall(new_board, rows, columns)
        return matching_check(new_board, rows, columns)
    else:
        #print_game_board(new_board)
        return new_board

def empty_board(rows, columns):
    '''returns an empty board object as a double list'''
    game_board = []
    for k in range(rows + 1):
        game_board.append([])
    for i in range(rows):
        game_board[i].append('|')
        for j in range(columns):
            game_board[i].append('   ')
        game_board[i].append('|')
    game_board[rows].append(' ')
    for k in range(columns):
        game_board[rows].append('---')
    game_board[rows].append(' ')
    return game_board

def check_horizontal_match(game_board, rows, columns):
    '''checks if there are any horizontal matches'''
    for i in range(rows):
        set_letter = ''
        for j in range(columns+1):
            if game_board[i][j] != '   ' and game_board[i][j] != '|':
                set_letter = game_board[i][j][1]
                try:
                    if set_letter == game_board[i][j+1][1]:
                        try:
                            if set_letter == game_board[i][j+2][1]:
                                game_board[i][j] = '*' + set_letter + '*'
                                game_board[i][j+1] = '*' + set_letter + '*'
                                game_board[i][j+2] = '*' + set_letter + '*'
                                k = j+3
                                while k < columns:
                                    if game_board[i][k][1] == set_letter:
                                        game_board[i][k] =  '*' + set_letter + '*'
                                    else:
                                        break
                                    k += 1
                        except:
                            a = 0
                except:
                    a = 0             
    return game_board

def check_vertical_match(game_board, rows, columns):
    '''checks if there are any vertical matches'''
    for i in range(rows):
        set_letter = ''
        for j in range(columns+1):
            if game_board[i][j] != '   ' and game_board[i][j] != '|':
                set_letter = game_board[i][j][1]
                try:
                    if set_letter == game_board[i+1][j][1]:
                        try:
                            if set_letter == game_board[i+2][j][1]:
                                game_board[i][j] = '*' + set_letter + '*'
                                game_board[i+1][j] = '*' + set_letter + '*'
                                game_board[i+2][j] = '*' + set_letter + '*'
                                k = i+3
                                while k < rows:
                                    if game_board[i][k][1] == set_letter:
                                        game_board[i][k] =  '*' + set_letter + '*'
                                    else:
                                        break
                                    k += 1
                        except:
                            a = 0
                except:
                    a = 0             
    return game_board

def check_diagonal_match(game_board, rows, columns):
    '''checks if there are any diagonal matches'''
    for i in range(rows):
        set_letter = ''
        for j in range(columns+1):
            if game_board[i][j] != '   ' and game_board[i][j] != '|':
                set_letter = game_board[i][j][1]
                try:
                    if set_letter == game_board[i+1][j+1][1]:
                        try:
                            if set_letter == game_board[i+2][j+2][1]:
                                game_board[i][j] = '*' + set_letter + '*'
                                game_board[i+1][j+1] = '*' + set_letter + '*'
                                game_board[i+2][j+2] = '*' + set_letter + '*'
                                k = i+3
                                while k < rows and k < columns:
                                    if game_board[k][k][1] == set_letter:
                                        game_board[k][k] =  '*' + set_letter + '*'
                                    else:
                                        break
                                    k += 1
                        except:
                            a = 0
                except:
                    a = 0
                try:
                    #print(i,j)
                    #print(game_board[i][j])
                    #print(game_board[i+1][j-1])
                    #print(game_board[i-2][j-2])
                    if set_letter == game_board[i+1][j-1][1]:
                        try:
                            if set_letter == game_board[i+2][j-2][1]:
                                game_board[i][j] = '*' + set_letter + '*'
                                game_board[i+1][j-1] = '*' + set_letter + '*'
                                game_board[i+2][j-2] = '*' + set_letter + '*'
                                k = i+3
                                m = j-3
                                while k < rows and m >= 0:
                                    if game_board[k][m][1] == set_letter:
                                        game_board[k][m] =  '*' + set_letter + '*'
                                    else:
                                        break
                                    k += 1
                                    m -= 1
                        except:
                            a = 0
                except:
                    a = 0
    return game_board

def flash_matched_letters(game_board, rows, columns):
    for i in range(len(game_board) - 1):
        for j in range(len(game_board[i])):
            if game_board[i][j] != '|':
                if game_board[i][j][0] == '*':
                    pygame.draw.circle(surface, white, [(200+(30*j)-15), (100+(30*(i+1))-15)], 10)
    pygame.display.flip()
    time.sleep(.25)
    for i in range(len(game_board) - 1):
        for j in range(len(game_board[i])):
            if game_board[i][j] != '|':
                if game_board[i][j][1] == 'R':
                    pygame.draw.circle(surface, red, [(200+(30*j)-15), (100+(30*(i+1))-15)], 10)
                if game_board[i][j][1] == 'P':
                    pygame.draw.circle(surface, pink, [(200+(30*j)-15), (100+(30*(i+1))-15)], 10)
                if game_board[i][j][1] == 'G':
                    pygame.draw.circle(surface, green, [(200+(30*j)-15), (100+(30*(i+1))-15)], 10)
                if game_board[i][j][1] == 'O':
                    pygame.draw.circle(surface, orange, [(200+(30*j)-15), (100+(30*(i+1))-15)], 10)
                if game_board[i][j][1] == 'B':
                    pygame.draw.circle(surface, blue, [(200+(30*j)-15), (100+(30*(i+1))-15)], 10)
                if game_board[i][j][1] == 'V':
                    pygame.draw.circle(surface, purple, [(200+(30*j)-15), (100+(30*(i+1))-15)], 10)
                if game_board[i][j][1] == 'T':
                    pygame.draw.circle(surface, teal, [(200+(30*j)-15), (100+(30*(i+1))-15)], 10)
    pygame.display.flip()
    
def matching_check(game_board, rows, columns):
    '''check if there are any matches'''
    updated_game_board = check_horizontal_match(game_board, rows, columns)
    updated_game_board = check_vertical_match(game_board, rows, columns)
    updated_game_board = check_diagonal_match(game_board, rows, columns)
    flash_matched_letters(updated_game_board, rows, columns)
    updated_game_board = remove_matched_letters(updated_game_board, rows, columns)
    updated_game_board = force_fall(updated_game_board, rows, columns)
    updated_game_board = force_fall(updated_game_board, rows, columns)
    return updated_game_board

def force_fall(game_board, rows, columns):
    '''force the items in the game board to fall if nothing is below them'''
    for i in range(rows):
        for j in range(columns):
            #print(game_board[i][j+1], game_board[i-1][j+1])
            if game_board[i][j+1] != '   ':
                if game_board[i+1][j+1] == '   ':
                    game_board[i+1][j+1] = game_board[i][j+1]
                    game_board[i][j+1] = '   '
                    try:
                        if game_board[i-1][j+1] != '   ' and game_board[i-1][j+1] != '---':
                            if game_board[i][j+1] == '   ':
                                game_board[i][j+1] = game_board[i-1][j+1]
                                game_board[i-1][j+1] = '   '
                    except:
                        a = 1
            #print(i, j,)
            #print_game_board(game_board)
    return game_board
            
        
                
        
        
