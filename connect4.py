import numpy as np
import random

rand = random.Random()

class Connect4():
    NUM_ROWS = 8
    NUM_COLS = 10
    NUM2WIN = 6
    def __init__(self):
        self.board = np.zeros((self.NUM_ROWS, self.NUM_COLS))

    def __str__(self):
        str_board = "\n\n" + str(self.board).replace("0.", "_").replace("-1.", " O").replace("1.", "X")
        str_board = str_board.replace("[", " ").replace("]", " ")
        return str_board
        
    def get_avail_moves(self):
        return [m for m in range(self.NUM_COLS) if self.board[0][m] == 0] # check top row for empty

    def make_move(self, move):
        if np.sum(self.board) == 0:
            player = 1
        else:
            player = -1
        
        j = 0
        while j+1 < self.NUM_ROWS and self.board[j+1][move] == 0: j+=1
        
        self.board[j][move] = player

    def get_winner(self):
        for i in range(self.NUM_ROWS-self.NUM2WIN+1):
            for j in range(self.NUM_COLS-self.NUM2WIN+1):
                subboard = self.board[i:i+self.NUM2WIN, j:j+self.NUM2WIN]
                if np.max(np.abs(np.sum(subboard, 0))) == self.NUM2WIN:
                    return True
                if np.max(np.abs(np.sum(subboard, 1))) == self.NUM2WIN:
                    return True
                elif np.abs(sum([subboard[k, k] for k in range(self.NUM2WIN)])) == self.NUM2WIN: # diag
                    return True
                elif np.abs(sum([subboard[k, self.NUM2WIN-1-k] for k in range(self.NUM2WIN)])) == self.NUM2WIN: # opp diag
                    return True
        return False


def main():
    XO = {-1: "O", 0: "Nobody", 1: "X"}
    my_game = Connect4()
    moves = my_game.get_avail_moves()
    print(my_game)
    player = 1 # first player is alway 1
    human_player = rand.choice([1, -1])
    while moves != []:

        if player == human_player:
            print(f"Available moves are: {moves}")
            move = int(input("Enter move human: "))
        else:
            move = rand.choice(moves)
        my_game.make_move(move)
        print(my_game)
        winner =  my_game.get_winner()
        if winner:
            print(f"{XO[player]} Wins!")
            break
        moves = my_game.get_avail_moves()
        player = -player


if __name__ == "__main__":
    main()        