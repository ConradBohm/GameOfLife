import random

def dead_state(width, height):
    board_state = []
    for i in range(height):
        board_state.append([0]*width)
        
    return board_state

def random_state(width, height):
    state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            if random.random() >= 0.5:
                state[i][j] = 0
            else:
                state[i][j] = 1
    
    return state



print(dead_state(5,5))


print(random_state(5,5))

