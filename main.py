import random

class Board:
    # dimension -> (height,width)
    def __init__(self, dimension=[4, 4]) -> None:
        self.boardState = []
        self.dimension = dimension

    # Generating board state
    def getRandomState(self):
        for row in range(self.dimension[0]):
            stateList = []
            for col in range(self.dimension[1]):
                stateList.append(1 if random.random() >= 0.5 else 0)
            self.boardState.append(stateList)
        return self.boardState


if __name__ == "__main__":
    newBoard = Board([5, 5])
    print(newBoard.getRandomState())
