def check_game_mode(mode):  # choose if we want ot load a file or create a new game
    if mode == 'N':
        return 0
    elif mode == 'S':
        return 1  # 1 for saved game
    else:
        # if user gives a invalid input raise an error
        raise ValueError(
            "In order to play the game select either (N) for new game or (S) for saved game")


def check_validity_of_rows(rows):  # rows need to be between 5 and 10
    if rows >= 5 and rows <= 10:
        return rows
    else:
        # in case of invalid number given for rows raise an error
        raise ValueError("Rows of the game should be between 5 and 10")


def print_grid(grid):  # used to print the grid
    grid_len = len(grid)
    val = len('\t' + '\t'.join(str(i+1)
              for i in range(grid_len)))  # make the grid pretty :)
    print('\t' + '\t'.join(str(i+1) for i in range(grid_len)))
    print('-' * (val+6*grid_len))
    letter = 65
    for i in range(grid_len):
        print(chr(letter) + '|', end='')
        for j in range(grid_len):
            print('\t' + grid[i][j] + '|', end='')
        print()
        letter += 1
    print('-' * (val+6*grid_len))


def create_grid(rows):  # 2dimensional list corresponds to the current grid
    # we initiate it with blank spaces
    grid = [[' ' for _ in range(rows)] for _ in range(rows)]
    print_grid(grid)
    return grid


# check if the user gave a valid spot to put his mark
def check_spot_validity(spot, len_grid):
    while spot <= 0 or spot >= len_grid + 1:  # wait until the user gives a valid spot
        print("Put a column number between 1 and the number you put in the start of the game") 
        spot = int(input())
    return spot


def fill_spot(grid, spot, player, show):
    changed = 0
    if player == 1:
        symbol = 'O'
    else:
        symbol = 'X'
    for i in range(len(grid)):
        if grid[-1 - i][spot - 1] != ' ':
            i += 1
        else:
            grid[-1 - i][spot - 1] = symbol
            coords = tuple((len(grid) - i - 1, spot-1))
            changed = 1
            break
    if changed == 0:
        print("There is no place for the column you chose. Select another column!") 
        selected_spot = int(input())
        selected_spot = check_spot_validity(selected_spot, len(grid))
        grid, coords = fill_spot(grid, selected_spot, player, True)

    if show:
        print_grid(grid)

    return grid, coords


def fill_grid_from_file(name):  # read file and translate it to grid and player coords

    with open(str(name), 'rb') as f:
        lines = [x.decode('utf8').strip().split(',')
                 for x in f.readlines()]  # read all lines of the file
    scores = lines[-1]
    # save the scores and delete the line
    scores = [int(score) for score in scores]
    del lines[-1]
    # create an empty grid in regard to the len of the lines list
    grid = [[' ' for _ in range(len(lines))] for _ in range(len(lines))]
    # fill the grid / depends on the values we read => 1 -> O and 2 -> X
    for i, item in enumerate(lines):
        for j, char in enumerate(item):
            if char == '0':
                grid[i][j] = ' '
            elif char == '1':
                grid[i][j] = 'O'
            elif char == '2':
                grid[i][j] = 'X'
            else:
                # if we give something that isnt 0,1 or 2 raise error
                raise ValueError("Values in the file are not correct!")
            j += 1
        i += 1
    print_grid(grid)
    player1_coords, player2_coords = find_coords(grid)  # update player points
    return grid, scores, player1_coords, player2_coords


def find_coords(grid):  # search the grid and save each players points
    player1_coords = set()
    player2_coords = set()
    for i, items in enumerate(grid):
        for j, element in enumerate(items):
            if element != ' ':
                if element == 'O':
                    player1_coords.add((i, j))
                else:
                    player2_coords.add((i, j))
    return player1_coords, player2_coords

def save_game(grid, scores, name):  # translate the grid to a file as requested

    f = open(str(name), "w")
    for i, items in enumerate(grid):
        comma = 1
        for j, element in enumerate(items):
            if j == len(grid) - 1:
                comma = 0
            if element == " ":
                if comma:
                    f.write('0,')
                else:
                    f.write('0')
            elif element == 'O':
                if comma:
                    f.write('1,')
                else:
                    f.write('1')
            elif element == 'X':
                if comma:
                    f.write('2,')
                else:
                    f.write('2')
        f.write('\n')
    for i, items in enumerate(scores):
        if i == 0:
            f.write(str(items) + ',')
        else:
            f.write(str(items))

    print("Game saved!")