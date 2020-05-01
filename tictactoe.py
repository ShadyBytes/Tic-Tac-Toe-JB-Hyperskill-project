cells_input = '_________'


def print_field(cells_input_list_f):
    print('---------')
    print('| {0} {1} {2} |'.format(cells_input_list_f[0], cells_input_list_f[1], cells_input_list_f[2]))
    print('| {0} {1} {2} |'.format(cells_input_list_f[3], cells_input_list_f[4], cells_input_list_f[5]))
    print('| {0} {1} {2} |'.format(cells_input_list_f[6], cells_input_list_f[7], cells_input_list_f[8]))
    print('---------')


print_field(['_', '_', '_', '_', '_', '_', '_', '_', '_'])


cells_input_list = list(cells_input)

win_positions = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 5, 7], [3, 6, 9], [4, 5, 6], [7, 8, 9]]
positions = []
correct_numbers_list = ['1', '2', '3']
wrong_numbers_list = ['4', '5', '6', '7', '8', '9']


def input_on_field(char_to_place):
    while True:
        usr_pos_choice = input('Enter the coordinates: ').split()
        if usr_pos_choice[0] in correct_numbers_list and usr_pos_choice[1] in correct_numbers_list:
            if usr_pos_choice == ['1', '1']:
                if cells_input_list[6] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    cells_input_list[6] = char_to_place
                    break
            if usr_pos_choice == ['1', '2']:
                if cells_input_list[3] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    cells_input_list[3] = char_to_place
                    break
            if usr_pos_choice == ['1', '3']:
                if cells_input_list[0] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    cells_input_list[0] = char_to_place
                    break
            if usr_pos_choice == ['2', '1']:
                if cells_input_list[7] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    cells_input_list[7] = char_to_place
                    break
            if usr_pos_choice == ['2', '2']:
                if cells_input_list[4] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    cells_input_list[4] = char_to_place
                    break
            if usr_pos_choice == ['2', '3']:
                if cells_input_list[1] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    cells_input_list[1] = char_to_place
                    break
            if usr_pos_choice == ['3', '1']:
                if cells_input_list[8] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    cells_input_list[8] = char_to_place
                    break
            if usr_pos_choice == ['3', '2']:
                if cells_input_list[5] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    cells_input_list[5] = char_to_place
                    break
            if usr_pos_choice == ['3', '3']:
                if cells_input_list[2] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    cells_input_list[2] = char_to_place
                    break
        elif usr_pos_choice[0] or usr_pos_choice[1] in wrong_numbers_list:
            print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')



def x_counter(cells):
    cntr = 0
    for x in cells:
        if x == 'X':
            cntr += 1
    return cntr


def o_counter(cells):
    counterr = 0
    for x in cells:
        if x == 'O':
            counterr += 1
    return counterr


def impossible_rows(cells, o_pos, x_pos):
    x_win = False
    o_win = False
    for x in win_positions:
        if all(elem in o_pos for elem in x) and abs(x_counter(cells) - o_counter(cells)) < 2:
            o_win = True

    for x in win_positions:
        if all(elem in x_pos for elem in x) and abs(x_counter(cells) - o_counter(cells)) < 2:
            x_win = True

    if x_win and o_win:
        return True


def impossible_check(cells, o_pos, x_pos):
    if abs(x_counter(cells) - o_counter(cells)) >= 2 or impossible_rows(cells, o_pos, x_pos):
        return True


def empty_check(cells_input_list_f):
    for x in cells_input_list_f:
        if x == '_':
            return True


def win_check(cells_input_list_f):
    o_pos = []
    x_pos = []

    for index, x in enumerate(cells_input_list_f):
        if x == 'X':
            x_pos.append(index + 1)
        elif x == 'O':
            o_pos.append(index + 1)

    for x in win_positions:
        if all(elem in o_pos for elem in x) and not impossible_check(cells_input_list_f, o_pos, x_pos):
            return 'O wins'

    for x in win_positions:
        if all(elem in x_pos for elem in x) and not impossible_check(cells_input_list_f, o_pos, x_pos):
            return 'X wins'


def game_state_check(cells_input_list_f):
    zeroes = '_' in cells_input
    o_pos = []
    x_pos = []
    for index, x in enumerate(cells_input_list_f):
        if x == 'X':
            x_pos.append(index + 1)
        elif x == 'O':
            o_pos.append(index + 1)

    draw_state = not win_check(cells_input_list_f) and not zeroes

    not_finished = not win_check(cells_input_list_f) and zeroes

    if win_check(cells_input_list_f) == 'O wins':
        return 'O wins'
    elif win_check(cells_input_list_f) == 'X wins':
        return 'X wins'
    elif draw_state:
        return 'Draw'
    elif impossible_check(cells_input_list_f, o_pos, x_pos):
        return 'Impossible'
    # elif not_finished:
    # print('Game not finished')


counter = 0
while True:
    if counter % 2 == 0:
        input_on_field('X')
    else:
        input_on_field('O')

    if game_state_check(cells_input_list) == 'X wins':
        print_field(cells_input_list)
        print('X wins')
        break
    elif game_state_check(cells_input_list) == 'O wins':
        print_field(cells_input_list)
        print('O wins')
        break
    elif game_state_check(cells_input_list) == 'Draw':
        print_field(cells_input_list)
        print('Draw')
        break
    elif game_state_check(cells_input_list) not in ['Draw', 'O wins', 'X wins']:
        if '_' not in cells_input_list:
            print_field(cells_input_list)
            print('Draw')
            break
    print_field(cells_input_list)
    counter += 1
