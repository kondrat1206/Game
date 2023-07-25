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

pos_x = 0
pos_y = 0

exit_x = randint(0, (columns - 1))
exit_y = randint(0, (rows - 1))

while True:
    game_map = ''
    win_condition = pos_x == exit_x and pos_y == exit_y
    for j in range(rows):
        row = '|'
        for i in range(columns):
            if i == pos_x and j == pos_y:
                row += 'X|'
            elif i == exit_x and j == exit_y:
                row += 'O|'
            elif win_condition:
                row += 'W|'
            else: 
                row += ' |'

        game_map += f"{row}\n"
    print(game_map)
    if win_condition:
        print('YOU WIN!!!')
        break
    direction = input('Enter direction (U/D/L/R): ')
    if (direction == 'D' or direction == 'd') and pos_y < (columns - 1):
        pos_y += 1
    if (direction == 'U' or direction == 'u') and pos_y > 0:
        pos_y -= 1
    if (direction == 'R' or direction == 'r') and pos_x < (rows - 1):
        pos_x += 1
    if (direction == 'L' or direction == 'l') and pos_x > 0:
        pos_x -= 1