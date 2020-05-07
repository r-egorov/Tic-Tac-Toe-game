class GameBoard:
    """The main class, an instance of which is the game's board.
    Has methods which can make a move, validate user's input, print the board,
    count wins and print the winner
    """
    x_won = 0
    o_won = 0

    def __init__(self):
        self.board = {7: " ", 8: " ", 9: " ",
                      4: " ", 5: " ", 6: " ",
                      1: " ", 2: " ", 3: " "}

    def make_a_move(self, turn: str):
        """Takes an "X" of "O" as an argument and makes a move.
        Asks for the position in which places the "X" or "O" after validation the input data.
        """
        while True:
            self.print_board()
            print(f"It's your move, {turn}.")
            try:
                move_input = int(input("Enter a number of the cell: "))
                if self.board[self.valid_move(move_input)] == " ":
                    self.board[self.valid_move(move_input)] = turn
                    break
                else:
                    print("This cell is already occupied. Try again.")
                    continue
            except ValueError:
                print("Wrong number of the cell. Try again.")
                continue

    @staticmethod
    def valid_move(move_input: int):
        """Validates the input number of the cell position
        """
        if move_input in range(1, 10):
            return move_input
        else:
            raise ValueError

    def print_board(self):
        """Prints the board with the moves.
        """
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])
        print("-+-+-")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("-+-+-")
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])

    @classmethod
    def print_win_counter(cls):
        """Prints the wins counter.
        """
        print(f"Win count: \n",
              f"X: {cls.x_won}, O: {cls.o_won}")

    @classmethod
    def count_wins(cls, player):
        """Counts the wins, prints the win counter using the class method "print_win_counter".
        """
        if player == "X":
            cls.x_won += 1
        else:
            cls.o_won += 1
        cls.print_win_counter()

    def check_winner(self):
        """Checks the winner. If there is one, prints the winner, counts the win,
        using the "count_win" method and returns True.
        If there is no winner, returns False.
        """
        if self.board[7] == self.board[8] == self.board[9] != " ":  # top-across winner
            self.print_board()
            print(f"***{self.board[7]} is the winner!***")
            self.count_wins(self.board[7])
            return True
        elif self.board[4] == self.board[5] == self.board[6] != " ":  # middle-across winner
            self.print_board()
            print(f"***{self.board[4]} is the winner!***")
            self.count_wins(self.board[4])
            return True
        elif self.board[1] == self.board[2] == self.board[3] != " ":  # lower-across winner
            self.print_board()
            print(f"***{self.board[1]} is the winner!***")
            self.count_wins(self.board[1])
            return True
        elif self.board[1] == self.board[4] == self.board[7] != " ":  # left low-top-across winner
            self.print_board()
            print(f"***{self.board[1]} is the winner!***")
            self.count_wins(self.board[1])
            return True
        elif self.board[2] == self.board[5] == self.board[8] != " ":  # middle low-top-across winner
            self.print_board()
            print(f"***{self.board[2]} is the winner!***")
            self.count_wins(self.board[2])
            return True
        elif self.board[3] == self.board[6] == self.board[9] != " ":  # right low-top-across winner
            self.print_board()
            print(f"***{self.board[3]} is the winner!***")
            self.count_wins(self.board[3])
            return True
        elif self.board[1] == self.board[5] == self.board[9] != " ":  # diagonal winner
            self.print_board()
            print(f"***{self.board[1]} is the winner!***")
            self.count_wins(self.board[1])
            return True
        elif self.board[7] == self.board[5] == self.board[3] != " ":  # diagonal winner
            self.print_board()
            print(f"***{self.board[7]} is the winner!***")
            self.count_wins(self.board[7])
            return True
        else:
            return False


def play_again():
    """Asks if the players want to play once more.
    """
    while True:
        a = input("Play again? Y/N: ")
        if a == "Y" or a == "y":
            return True
        elif a == "N" or a == "n":
            return False
        else:
            print("Invalid input. Try again.")


def game():
    """Launches the game.
    """
    game_board = GameBoard()
    move_counter = 0
    turn = "X"

    for i in range(10):
        if move_counter >= 5 and game_board.check_winner():
            break
        game_board.make_a_move(turn)
        move_counter += 1
        if move_counter == 9:
            print("Game over.")
            print("It's a tie!")
            break
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    return


def introduction():
    print("Welcome to \"Tic-Tac-Toe\"!\n"
          "Player enters the number of the cell on the board.\n"
          "The cells are numbered as the NUM-keyboard:")
    print("7" + "|" + "8" + "|" + "9")
    print("-+-+-")
    print("4" + "|" + "5" + "|" + "6")
    print("-+-+-")
    print("1" + "|" + "2" + "|" + "3")
    print("Have fun!\n")


if __name__ == "__main__":
    introduction()
    while True:
        game()
        if not play_again():
            break
    print("Thanks for playing!")
    GameBoard.print_win_counter()



