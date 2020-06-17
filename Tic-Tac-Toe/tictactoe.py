from string import digits

s = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
valid_coordinates = [[1 ,3], [2, 3], [3, 3], [1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [3, 1]]

def show_board():
    print('---------')
    print(f'| {s[0]} {s[1]} {s[2]} |')
    print(f'| {s[3]} {s[4]} {s[5]} |')
    print(f'| {s[6]} {s[7]} {s[8]} |')
    print('---------')

def make_move(co, player):
    global s
    s[valid_coordinates.index(co)] = player

def is_occupied(c):
    if s[valid_coordinates.index(c)] == 'X' or s[valid_coordinates.index(c)] == 'O':
        return True
    return False

def analyze_board():
    winner = []
    if s[0] == s[1] == s[2] == 'X' or s[3] == s[4] == s[5] == 'X' or s[6] == s[7] == s[8] == 'X':
        winner.append('X')
    elif s[0] == s[3] == s[6] == 'X' or s[1] == s[4] == s[7] == 'X' or s[2] == s[5] == s[8] == 'X':
        winner.append('X')
    elif s[0] == s[4] == s[8] == 'X' or s[2] == s[4] == s[6] == 'X':
        winner.append('X')
    if s[0] == s[1] == s[2] == 'O' or s[3] == s[4] == s[5] == 'O' or s[6] == s[7] == s[8] == 'O':
        winner.append('O')
    elif s[0] == s[3] == s[6] == 'O' or s[1] == s[4] == s[7] == 'O' or s[2] == s[5] == s[8] == 'O':
        winner.append('O')
    elif s[0] == s[4] == s[8] == 'O' or s[2] == s[4] == s[6] == 'O':
        winner.append('O')

    if len(winner) == 0:
        if abs(s.count('X') - s.count('O')) > 1:
            return 'Impossible'
        else:
            if ' ' in s or '_' in s:
                return None
            else:
                return 'Draw'

    if len(winner) == 2:
        return 'Impossible'

    if len(winner) == 1:
        return f'{winner[0]} wins'

move = 1
while True:
    show_board()
    while True:
        coordinates = input('Enter the coordinates: ').split()
        if coordinates[0] in digits and coordinates[1] in digits:
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            if 1 <= coordinates[0] <= 3 and 1 <= coordinates[1] <= 3:
                if not is_occupied(coordinates):
                    if move % 2 == 1:
                        make_move(coordinates, 'X')
                    else:
                        make_move(coordinates, 'O')
                    move += 1
                    break
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')
    result = analyze_board()
    if result == 'X wins' or result == 'O wins' or result == 'Draw':
        show_board()
        print(result)
        break