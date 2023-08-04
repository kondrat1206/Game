'''
|X| | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | |O|

'''
from random import randint, choice

rows = randint(5, 11)
columns  = rows


def check_condition(pos_x, pos_y, 
                    exit_x,exit_y, 
                    enemy_x, enemy_y, turns, char_sign):
    win_condition = pos_x == exit_x and pos_y == exit_y
    loss_condition = pos_x == enemy_x and pos_y == enemy_y
    if win_condition:
        char_sign = 'W'
        print(f'YOU WIN!!! in {turns} turns')
    if loss_condition:
        char_sign = 'L'
        print(f'YOU LOSS!!! in {turns} turns')
    return char_sign, win_condition or loss_condition


def generate_map(pos_x, pos_y, char_sign, 
                 exit_x, exit_y, exit_sign, 
                 enemy_x, enemy_y, enemy_sign, 
                 rows=rows, columns=columns):

    game_map = []
    for j in range(rows):
        row = []
        for i in range(columns):
            row.append(' ')

        game_map.append(row)

    game_map[exit_y][exit_x] = exit_sign
    game_map[enemy_y][enemy_x] = enemy_sign
    game_map[pos_y][pos_x] = char_sign

    return game_map


def move(direction, x, y, rows=rows, columns=columns):

    if (direction == 'D' or direction == 'd') and y < (columns - 1):
        y += 1
    if (direction == 'U' or direction == 'u') and y > 0:
        y -= 1
    if (direction == 'R' or direction == 'r') and x < (rows - 1):
        x += 1
    if (direction == 'L' or direction == 'l') and x > 0:
        x -= 1
    
    return(x, y)


def print_map(game_map):
    for row in game_map:
        print(f'|{"|".join(row)}|')


pos_x = randint(0, (columns - 1))
pos_y = randint(0, (rows - 1))
char_sign = 'X'

enemy_x = randint(0, (columns - 1))
enemy_y = randint(0, (rows - 1))
enemy_sign = 'E'

exit_x = randint(0, (columns - 1))
exit_y = randint(0, (rows - 1))
exit_sign = 'O'

turns = 0


while True:

    char_sign, exit_flag = check_condition(pos_x, pos_y, 
                                           exit_x,exit_y, 
                                           enemy_x, enemy_y, turns, char_sign)
    
    
    game_map = generate_map(pos_x, pos_y, char_sign, 
                            exit_x, exit_y, exit_sign, 
                            enemy_x, enemy_y, enemy_sign)
    #print(game_map)
    print_map(game_map)
    if exit_flag:
        break
    
    direction = input('Enter direction (U/D/L/R): ')
    pos_x, pos_y = move(direction, pos_x, pos_y)
    turns += 1
    enemy_direction = choice('udrl')
    enemy_x, enemy_y = move(enemy_direction, enemy_x, enemy_y)