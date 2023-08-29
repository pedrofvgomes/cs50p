import sys, time, random

def main():
    print('#########################\n\nWelcome to Tic Tac Toe!')

    # escolher simbolo
    symbol = pick_symbol()
    if symbol == -1:
        sys.exit()
    
    if symbol == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    # random para ver quem começa
    turn = first_to_play()
    grid = start_grid()

    while True:
        time.sleep(1)

        display_grid(grid)

        if turn == symbol:
            print('Your turn! (' + symbol + ')' )
            get_choice(grid, symbol)
        
        else:
            print("CPU's turn! (" + opponent + ')') 
            time.sleep(2)
            available = []
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == ' ':
                        a = []
                        a.append(i)
                        a.append(j)
                        available.append(a)

            choice = random.choice(available)
            grid[choice[0]][choice[1]] = opponent

        if check_winner(grid) != 0:
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
        print('\n\n\n\n\n')

    winner = check_winner(grid)
    print('\n\n\n\n\n')
    time.sleep(1)
    display_grid(grid)

    if winner == symbol:
        print('\n\n\n#########################')
        print('        You won!!        ')
        print('#########################')

    elif winner == opponent:
        print('\n\n\n#########################')
        print('        You lost...        ')
        print('#########################')

    else:
        print('\n\n\n#########################')
        print("         It's a tie!          ")
        print('#########################')



def pick_symbol():
    print('\n#########################\n')
    print('Please choose your symbol')
    print('1) X')
    print('2) O')
    print('0) Exit')
    n = input('--> ')
    if n.isnumeric():
        if n == '1':
            return 'X'
        if n == '2':
            return 'O'
    return -1
        
def first_to_play():
    time.sleep(0.5)
    print('\n#########################\n')
    print('Randomly determining who plays first...', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.')
    a = random.choice(['X', 'O'])
    return a

def start_grid():
    rows = []
    for i in range(3):
        row = []
        row.append(' ')
        row.append(' ')
        row.append(' ')
        rows.append(row)
    return rows

# se ninguem tiver ganho e o jogo puder continuar, return 0
# se alguem tiver ganho, return do simbolo
# se terminar em empate, return -1
def check_winner(grid):   
    # horizontal
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
        
    # vertical
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != ' ':
            return grid[0][i]
        
    # diagonal
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
        return grid[0][2]
    
    # jogo pode continuar
    for row in grid:
        for cell in row:
            if cell == ' ':
                return 0
    
    # empate
    return -1

def display_grid(grid):
    print(f'---1------2------3---\n|     ||     ||     |\n|  {grid[0][0]}  ||  {grid[0][1]}  ||  {grid[0][2]}  |\n|     ||     ||     |')
    print(f'---4------5------6---\n|     ||     ||     |\n|  {grid[1][0]}  ||  {grid[1][1]}  ||  {grid[1][2]}  |\n|     ||     ||     |')
    print(f'---7------8------9---\n|     ||     ||     |\n|  {grid[2][0]}  ||  {grid[2][1]}  ||  {grid[2][2]}  |\n|     ||     ||     |')
    print('---------------------')

def get_choice(grid, symbol):
    while True:
        try:
            n = int(input('--> '))
            n -= 1
            row = n // 3
            col = n % 3
            if grid[row][col] == ' ':
                grid[row][col] = symbol
                break
            print('Invalid choice')
        except (ValueError, IndexError):
            print('Invalid choice')



if __name__ == '__main__':
    main()


