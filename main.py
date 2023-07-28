'''
|X| | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | |O|

'''
from random import randint

rows = 5
columns  = 5

pos_x = randint(0, (columns - 1))
pos_y = randint(0, (rows - 1))
char_sign = 'X'

exit_x = randint(0, (columns - 1))
exit_y = randint(0, (rows - 1))

turns = 0

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

while True:
    game_map = ''
    win_condition = pos_x == exit_x and pos_y == exit_y
    if win_condition:
        char_sign = 'W'
    for j in range(rows):
        row = '|'
        for i in range(columns):
            if i == pos_x and j == pos_y:
                row += f'{char_sign}|'
            elif i == exit_x and j == exit_y:
                row += 'O|'
            else: 
                row += ' |'

        game_map += f"{row}\n"
    print(game_map)
    if win_condition:
        print(f'YOU WIN!!! in {turns} turns')
        break
    direction = input('Enter direction (U/D/L/R): ')
    turns += 1
    pos_x, pos_y = move(direction, pos_x, pos_y)
    
    