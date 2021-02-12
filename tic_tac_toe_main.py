# tic tac toe game

# So, for the game itself to function we kinda need these things to be done:

#     board creator
#     board printer (display it)
#     game process itself
#     check for a win/tie
#         check rows, columns and diagonals
#     change turns between players
#     and then, computer player


# My first try I will put into the class Game




# we are importing this module to measure the time of evaluation
import time




class Game:
    # this class will use stright minmax method


    # the properties of this class are:

    # self.current_state - a 3x3 matrix, which contains the game's board
    # self.player_turn - this one checks whose turn is now


    def __init__(self):
        self.initialize_game();


    def initialize_game(self):
        # reset the board (make it empty)
        self.current_state = [['.', '.', '.'],
                              ['.', '.', '.'],
                              ['.', '.', '.']]
        # X is always first
        self.player_turn = 'X'


    def display_board(self):
        # this method will display (draw) the board
        for i in range(3):
            for j in range(3):
                print(f'{self.current_state[i][j]}|', end=' ')
            print() # just making a new line
        print() # at the end make a new line as well


    def is_valid(self, x_coordinate: int, y_coordinate: int) -> bool:
        # determines whether the made move is a legal move
        if (x_coordinate < 0 or x_coordinate > 2) or \
                                        (y_coordinate < 0 or y_coordinate > 2):
            # checking whether the entered coordinates are within the board
            is_valid = False
        elif self.current_state[x_coordinate][y_coordinate] != '.':
            # if the chosen spot is not empty, we can't make a move there
            is_valid = False
        else:
            # otherwise everything is cool
            is_valid = True

        return is_valid


    def is_end(self):
        # checks if the game is finished and returns the winner or None (if tie)
        
        # winner_is = '.' # this value will not change if it is a draw
        # it was easier to just use many return points
        # and not trying to have only one

        for i in range(3):
            # checks for the vertical win
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                # if it is a win condition, return the winner value (X or O)
                return self.current_state[0][i]

        for i in range(3):
            # checks for the horizontal win
            if self.current_state[i] == ['X', 'X', 'X']:
                # if the whole row is filled with X, then X has won
                return 'X'
            elif self.current_state[i] == ['O', 'O', 'O']:
                # but if the whole row is filled with O, then O has won
                return 'O'
            else:
                # otherwise just pass it
                pass

        # From the left diagonal check
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # from the right diagonal check
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]
        
        # checks if the board is full or not
        for i in range(3):
            for j in range(3):
                if (self.current_state[i][j] == '.'):
                    # if there is an empty space, stop the function
                    # so the game could continue
                    return None

        # if we are here, then it is a tie
        return '.'