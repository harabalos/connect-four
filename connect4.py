def check_game_mode(mode):  
    if mode == 'N':
        return 0
    elif mode == 'S':
        return 1  
    else:
        raise ValueError(
            "In order to play the game select either (N) for new game or (S) for saved game")


def check_validity_of_rows(rows):  
    if rows >= 5 and rows <= 10:
        return rows
    else:
        raise ValueError("Rows of the game should be between 5 and 10")


def print_grid(grid):  
    grid_len = len(grid)
    val = len('\t' + '\t'.join(str(i+1)
              for i in range(grid_len)))  
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