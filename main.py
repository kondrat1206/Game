'''
|X| | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | |O|

'''
from random import randint, choice

rows = randint(15, 16)
columns  = rows


def check_condition(objects, turns):

    for obj in objects:
        if obj['type'] == 'char':
            char = obj
        elif obj['type'] == 'portal':
            portal = obj
        elif obj['type'] == 'enemy':
            enemy = obj
            loss_condition = char['x'] == enemy['x'] and char['y'] == enemy['y']
            if loss_condition:
                char['sign'] = 'L'
                print(f'YOU LOSS!!! in {turns} turns')
                break

    win_condition = char['x'] == portal['x'] and char['y'] == portal['y']
    
    if win_condition:
        char['sign'] = 'W'
        print(f'YOU WIN!!! in {turns} turns')
    
    return win_condition or loss_condition


def generate_enemies(count):

    enemies = []

    for i in range(count):

        enemy = {"x" : randint(0, (columns - 1)),
                "y" : randint(0, (rows - 1)),
                "sign" : 'E',
                "type" : "enemy"}
        
        enemies.append(enemy)

    return enemies






def generate_map(objects, rows=rows, columns=columns):

    game_map = []

    for j in range(rows):
        row = []
        for i in range(columns):
            row.append(' ')

        game_map.append(row)

    for obj in objects:
        game_map[obj['y']][obj['x']] = obj['sign']

    return game_map


def move(direction, obj, rows=rows, columns=columns):

    if (direction == 'D' or direction == 'd') and obj['y'] < (columns - 1):
        obj['y'] += 1
    if (direction == 'U' or direction == 'u') and obj['y'] > 0:
        obj['y'] -= 1
    if (direction == 'R' or direction == 'r') and obj['x'] < (rows - 1):
        obj['x'] += 1
    if (direction == 'L' or direction == 'l') and obj['x'] > 0:
        obj['x'] -= 1
    


def print_map(game_map):
    for row in game_map:
        print(f'|{"|".join(row)}|')


char = {"x" : randint(0, (columns - 1)),
        "y" : randint(0, (rows - 1)),
        "sign" : 'X',
        "type" : "char"}


portal = {"x" : randint(0, (columns - 1)),
          "y" : randint(0, (rows - 1)),
          "sign" : 'O',
          "type" : "portal"}

enemies = generate_enemies(5)

objects = [char, portal] + enemies

turns = 0


while True:

    exit_flag = check_condition(objects, turns)
    
    
    game_map = generate_map(objects)
    print_map(game_map)
    
    if exit_flag:
        break

    for obj in objects:

        direction = ''

        if obj['type'] == 'char':
            direction = input('Enter direction (U/D/L/R): ')
        elif obj['type'] == 'enemy':
            direction = choice('udrl')
        
        move(direction, obj)

    turns += 1

    