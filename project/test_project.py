from project import pick_symbol, first_to_play, start_grid, check_winner, display_grid, get_choice
import mock

def main():
    test_pick_symbol()
    test_first_to_play()
    test_start_grid() 
    test_check_winner()

def test_pick_symbol():
    with mock.patch('builtins.input', return_value='1'):
        assert pick_symbol() == 'X'

    with mock.patch('builtins.input', return_value='2'):
        assert pick_symbol() == 'O'

    with mock.patch('builtins.input', return_value='10'):
        assert pick_symbol() == -1

    with mock.patch('builtins.input', return_value='abc'):
        assert pick_symbol() == -1


def test_first_to_play():
    assert first_to_play() in ['X', 'O']

def test_start_grid():
    grid = start_grid()
    assert len(grid) == 3
    assert len(grid[0]) == len(grid[1]) == len(grid[2]) == 3
    for row in grid:
        for cell in row:
            assert cell == ' '

def test_check_winner():
    grid = start_grid()
    assert check_winner(grid) == 0
    
    grid[0] = ['X','X','X']
    assert check_winner(grid) == 'X'

    grid[0] = [' ',' ',' ']
    grid[1] = ['O','O','O']
    assert check_winner(grid) == 'O'

    grid[0] = ['X','O','X']
    grid[1] = ['X','O','X']
    grid[2] = ['O','X','O']
    assert check_winner(grid) == -1
