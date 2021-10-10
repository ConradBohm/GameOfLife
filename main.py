import random

board_state = []

def random_state(width, height):
    for i in range(height):
        state_list = []
        for j in range(width):
            rand = random.random()
            if rand >= 0.5:
                state_list.append(0)
            else:
                state_list.append(1)

        board_state.append(state_list)


random_state(5,5)
print(board_state)
