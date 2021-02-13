# tic tac toe game

# So, we kinda need these things to be done:

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

    
    # this method will display (draw) the board
    def display_board(self):
        for i in range(3):
            for j in range(3):
                print(f'{self.current_state[i][j]}|', end=' ')
            print() # just making a new line
        print() # at the end make a new line as well

    
    # determines whether the made move is a legal move
    def is_valid(self, x_coordinate: int, y_coordinate: int) -> bool:
        if (x_coordinate < 0 or x_coordinate > 2) or \
                                    (y_coordinate < 0 or y_coordinate > 2):
            # If the entered coordinates are not within the board
            is_valid = False
        elif self.current_state[x_coordinate][y_coordinate] != '.':
            # If the chosen spot is not empty,
            # we can't make a move there.
            is_valid = False
        else:
            # Otherwise everything is cool
            is_valid = True

        return is_valid


    def is_end(self) -> str:
        # checks whether the game is finished 
        # and returns the winner or None (if it is a tie)
        
        # NOTE TO MYSELF: ###
        # winner_is = '.' # this value will not change if it is a draw
        # it was easier to just use many return points
        # and not trying to have only one
        # END OF THE NOTE ###
        
        # checks for the vertical win
        for i in range(3):    
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                # if it is a win condition, return the winner value 
                # (X or O)
                return self.current_state[0][i]
        
        # checks for the horizontal win
        for i in range(3):
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


    # The AI will play 'O' and will use the 'max' strategy
    def play_max(self) -> tuple:

        # Possible values for max_value are:
        # if it is a loss, then max_value = -1
        # if it is a tie - max_value = 0
        # if it is a win - max_value = 1

        # We start with -2 as the worst case
        max_value = -2

        x_coordinate = None
        y_coordinate = None

        result = self.is_end()

        # If the game has came to an end, the function needs to return
        # the evaluation function of the end.
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)
        else:
            # You can get None in self.is_end,
            # if the game is not finished. In that case just continue
            pass

        for i in range(3):
            for j in range(3):
                if self.current_state[i][j] == '.':
                    # Basically, we are having "non straight" recursion.
                    # We take the first available spot
                    # and put there 'O'.
                    # Afterwards, we will call self.play_min
                    # (which is a function that makes turn for 'X').
                    # self.play_min will do the same
                    # and eventually call self.play_max.
                    # And this will continue
                    # until self.is_end() returns not None
                    self.current_state[i][j] = 'O'
                    (min_value, min_i, min_j) = self.play_min()
                    # Fixing the max_value if needed
                    if min_value > max_value:
                        max_value = min_value
                        # these are coordinates
                        # of the best outcome so far
                        x_coordinate = i
                        y_coordinate = j
                    # Making the field back empty
                    self.current_state[i][j] = '.'

        return (max_value, x_coordinate, y_coordinate)


    # For now 'X' will be played by a human player,
    # but with help of this function
    def play_min(self):

        # Possible values for min_value are:
        # for win: -1
        # for a tie: 0
        # for a loss: 1

        # we will set min_value to 2 as the worst case scenario
        min_value = 2

        x_coordinate = None
        y_coordinate = None

        result = self.is_end()

        # If the game has came to an end, the function needs to return
        # the evaluation function of the end.
        # -1 - win
        # 0  - a tie
        # 1  - loss
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)
        else:
            # You can get None in self.is_end,
            # if the game is not finished. In that case just continue
            pass

        for i in range(3):
            for j in range(3):
                if self.current_state[i][j] == '.':
                    # The same thing as in self.play_max(),
                    # you find an empty spot, fill it with the 'X',
                    # call self.play_max(), whish will find next spot
                    # and fill it with 'O', after which it will call
                    # self.play_min() and etc, until we hit the end
                    # (self.is_end() returning something, but not None)
                    # and check who won. If it is a good move to do,
                    # we will save it. If not - we will continue with
                    # another spot.
                    self.current_state[i][j] = 'X'
                    (max_value, max_i, max_j) = self.play_max()
                    if max_value < min_value:
                        min_value = max_value
                        # these are coordinates
                        # of the best outcome so far
                        x_coordinate = i
                        y_coordinate = j
                    self.current_state[i][j] = '.'

        return (min_value, x_coordinate, y_coordinate)
