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
