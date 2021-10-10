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

def check_neighbours(board_state, x_pos, y_pos):
    num_of_neighbours = 0
    for check_y in range(y_pos-1, y_pos+2):
        if check_y < 0 or check_y > (len(board_state)-1):
            continue
        else:
            for check_x in range(x_pos-1, x_pos+2):
                if check_x < 0 or check_x > (len(board_state[0])-1):
                    continue
                elif check_x == x_pos and check_y == y_pos:
                    continue
                else:
                    num_of_neighbours += board_state[check_y][check_x]

    return num_of_neighbours
                    

def advance_board(board_state):
    new_board_state = dead_state(len(board_state[0]),len(board_state))
    for i in range(len(board_state)):
        for j in range(len(board_state[0])):
            neighbours = check_neighbours(board_state,j,i)
            if neighbours <= 1 or neighbours > 3:
                new_board_state[i][j] = 0
            elif neighbours == 3:
                new_board_state[i][j] = 1
            elif neighbours == 2:
                new_board_state[i][j] = board_state[i][j]

    return new_board_state
    


#print(dead_state(5,5))
test = random_state(20,20)
#test = [[1,0],[1,1]]
render(test)
#render(random_state(20,20))
#check_neighbours(test,1,0)
render(advance_board(test))


