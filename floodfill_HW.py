from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

# Check board length before execute the function.
def check_board_row_lengths(input_board: List[str]) -> bool:
    # Get the length of the first row
    first_row_length = len(input_board[0])

    # Check if all rows have the same length
    for row in input_board:
        if len(row) != first_row_length:
            return False

    return True
    
# Check if all rows have the same length
if check_board_row_lengths(board):
    print("All rows have the same length.")
else:
    print("Rows have different lengths.")

# Main function
def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    def fill(x, y):
        if (
            x < 0
            or x >= len(input_board)
            or y < 0
            or y >= len(input_board[0])
            or input_board[x][y] != old
        ):
            return

        # Replace the old value with the new value
        input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]

        # Recursively call the fill function for adjacent cells
        fill(x + 1, y)
        fill(x - 1, y)
        fill(x, y + 1)
        fill(x, y - 1)

    # Start the flood fill from the specified coordinates
    fill(x, y)
    return input_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)
