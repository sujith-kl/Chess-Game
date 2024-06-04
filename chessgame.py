
class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        # Initialize the chessboard
        board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P"] * 8,
            [""] * 8,
            [""] * 8,
            [""] * 8,
            [""] * 8,
            ["p"] * 8,
            ["r", "n", "b", "q", "k", "b", "n", "r"]
        ]
        return board

    def print_board(self):
        for row in self.board:
            print(" ".join(str(piece) for piece in row))

    def make_move(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        piece = self.board[start_row][start_col]
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = ""

    def example_moves(self):
        # Make some example moves
        self.make_move((6, 0), (4, 0))  # Move a black pawn
        self.make_move((1, 1), (3, 1))  # Move a white pawn
        self.make_move((7, 4), (7, 3))  # Move the black king's bishop
        self.make_move((0, 3), (0, 5))  # Move the white queen

# Example usage:
game = ChessGame()
game.print_board()
game.example_moves()
print("\nAfter example moves:")
game.print_board()