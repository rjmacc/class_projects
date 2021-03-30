#Ryan MacDonell


import project5_functions
import pygame
import sys
import time
from random import randint
from project5_input_handler import *
AMOUNT_OF_ROWS = 0
AMOUNT_OF_COLUMNS = 0
GAME_BOARD = []
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


class faller():
    def __init__(self, column, top, middle, bottom):
        self.column = column
        self.top = top
        self.middle = middle
        self.bottom = bottom
        self.bottom_row = 0
        self.middle_row = -1
        self.top_row = -2
        self.landed = False
    def move_left(self):
        if self.column != 1:
            self.column -= 1
    def move_right(self, columns):
        if self.column != columns:
            self.column += 1
    def rotate(self):
        temp_top = self.top
        self.top = self.bottom
        self.bottom = self.middle
        self.middle = temp_top
    def move_down(self):
        self.bottom_row += 1
        self.middle_row += 1
        self.top_row += 1
    def land(self):
        self.landed = True
        

GAME_BOARD = []

def create_random_faller():
    randnum_list = []
    top = ''
    mid = ''
    bottom = ''
    for i in range(3):
        randnum_list.append(randint(1,7))
    for i in range(len(randnum_list)):
        if randnum_list[i] == 1:
            if i == 0:
                top = 'R'
            if i == 1:
                mid = 'R'
            if i == 2:
                bottom = 'R'
        if randnum_list[i] == 2:
            if i == 0:
                top = 'P'
            if i == 1:
                mid = 'P'
            if i == 2:
                bottom = 'P'
        if randnum_list[i] == 3:
            if i == 0:
                top = 'B'
            if i == 1:
                mid = 'B'
            if i == 2:
                bottom = 'B'
        if randnum_list[i] == 4:
            if i == 0:
                top = 'G'
            if i == 1:
                mid = 'G'
            if i == 2:
                bottom = 'G'
        if randnum_list[i] == 5:
            if i == 0:
                top = 'V'
            if i == 1:
                mid = 'V'
            if i == 2:
                bottom = 'V'
        if randnum_list[i] == 6:
            if i == 0:
                top = 'T'
            if i == 1:
                mid = 'T'
            if i == 2:
                bottom = 'T'
        if randnum_list[i] == 7:
            if i == 0:
                top = 'O'
            if i == 1:
                mid = 'O'
            if i == 2:
                bottom = 'O'
    return faller(randint(1,6), top, mid, bottom)

def time_tick(game_board, falling_object):
    '''runs through a tick in time and moves the falling object down'''
    before_letter = ''
    after_letter = ''
    if game_board[falling_object.bottom_row+1][falling_object.column] != '   ':
        before_letter = '|'
        after_letter = '|'
    else:
        before_letter = '['
        after_letter = ']'
    if falling_object.top_row >= 0:
        game_board[falling_object.top_row][falling_object.column] = str(before_letter + falling_object.top + after_letter)
    if falling_object.middle_row >= 0:
        game_board[falling_object.middle_row][falling_object.column] = str(before_letter + falling_object.middle + after_letter)        
    if falling_object.bottom_row >= 0:
        game_board[falling_object.bottom_row][falling_object.column] = str(before_letter + falling_object.bottom + after_letter)
    return game_board   

def flash_faller(game_board, faller):
    '''flashes the faller white once it lands for a second then it disappears'''
    pygame.draw.circle(surface, white, [(200+(30*faller.column)-15), (100+(30*(faller.bottom_row+1))-45)], 10)
    pygame.draw.circle(surface, white, [(200+(30*faller.column)-15), (100+(30*(faller.middle_row+1))-45)], 10)
    pygame.draw.circle(surface, white, [(200+(30*faller.column)-15), (100+(30*(faller.top_row+1))-45)], 10)
    pygame.display.flip()
    time.sleep(.25)
    surface.fill(white)
    pygame.draw.rect(surface, black, [200, 100, 180, 390])
    pygame.draw.rect(surface, purple, [200, 100, 180, 390], 2)
    for i in range(200, 380, 30):
        pygame.draw.line(surface, purple, [i, 100], [i, 490], 1)
    for i in range(100, 490, 30):
        pygame.draw.line(surface, purple, [200, i], [380, i], 1)
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
        
def run_game(game_board):
    '''loop for the game'''
    pygame.init()
    running = True
    white = [255, 255, 255]
    black = [0, 0, 0]

    purple = [120, 0, 255]
    red = [255, 0, 0]
    pink = [255, 0, 255]
    blue = [0, 0, 255]
    green = [0, 255, 0]
    teal = [0, 255, 255]
    orange = [255, 200, 0]
    
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((600,600), pygame.RESIZABLE)
    surface.fill(white)
    pygame.display.set_caption('Columns game')
    pygame.display.update()
    has_faller = False
    while running:
        if has_faller == False:
            faller = create_random_faller()
            has_faller = True
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.VIDEORESIZE:
                surface = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                surface.fill(white)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    faller.rotate()
                if event.key == pygame.K_RIGHT:
                    if game_board[faller.bottom_row][faller.column + 1] == '   ':
                        faller.move_right(6)
                if event.key == pygame.K_LEFT:
                    if game_board[faller.bottom_row][faller.column - 1] == '   ':
                        faller.move_left()
        game_board = time_tick(game_board, faller)
        faller.move_down()
        if game_board[faller.bottom_row][faller.column] != '   ':
            has_faller = False
            faller.land()
        surface.fill(white)
        pygame.draw.rect(surface, black, [200, 100, 180, 390])
        pygame.draw.rect(surface, purple, [200, 100, 180, 390], 2)
        for i in range(200, 380, 30):
            pygame.draw.line(surface, purple, [i, 100], [i, 490], 1)
        for i in range(100, 490, 30):
            pygame.draw.line(surface, purple, [200, i], [380, i], 1)
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
        if faller.landed:
            game_board = lock_in_place(game_board, 13, 6)
            flash_faller(game_board, faller)
            game_board = matching_check(game_board, 13, 6)
            if faller.top_row <= 0:
                pygame.quit()
                sys.exit(0)
        game_board = clear_fallers(game_board, 13, 6)
    

def setup_game_board():
    '''sets the amount of rows and columns, begins the main loop'''
    '''
    print('Welcome to Columns!')
    print('This is an interactive game in which you match jewels in groups of three\ndiagonally, horizontally, or vertically. \n\nYou can rotate the falling jewels by pressing R, and move them\nleft or right by pressing < or >, respectively.\n')
    print('All falling inputs will be in the format\n"F" (column) (letter) (letter) (letter)\nwith a space in between all of them.')
    print('\n\nHave fun playing!')
    '''
    AMOUNT_OF_ROWS = 13
    AMOUNT_OF_COLUMNS = 6
    game_board = []
    game_board = empty_board(int(AMOUNT_OF_ROWS), int(AMOUNT_OF_COLUMNS))
    return game_board
    

if __name__ == '__main__':
    GAME_BOARD = setup_game_board()
    run_game(GAME_BOARD)
