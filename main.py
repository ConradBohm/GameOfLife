import random

def dead_state(width, height):
    board_state = []
    for i in range(height):
        board_state.append([0]*width)
        
    return board_state

def random_state(width, height):
    board_state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            if random.random() >= 0.5:
                board_state[i][j] = 0
            else:
                board_state[i][j] = 1
    
    return board_state

def render(board_state):
    total_print = '-' * (len(board_state[0]) + 2) + '\n'
    for row in board_state:
        row_print = '|'
        for value in row:
            if value == 0:
                row_print += ' '
            else:
                row_print += '#'
        total_print += (row_print + '|\n')

    total_print += ('-' * (len(board_state[0]) + 2))
    print(total_print)
    


#print(dead_state(5,5))
#print(random_state(5,5))
render(random_state(20,20))

