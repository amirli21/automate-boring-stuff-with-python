# Write your code here :-)
rows = [str(i) for i in range(1, 9)]
columns = [chr(j) for j in range(97, 105)]
colors = ['w', 'b']
figures = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

key_combinations = [row + col for row in rows for col in columns]
figure_combinations = [color + figure for color in colors for figure in figures]

def isValidChessboard(board):
    for comb in board:
        if comb not in key_combinations:
            return False
    board_values = list(board.values())
    for colored_figure in board_values:
        if board_values.count(colored_figure) > 2 \
        and colored_figure not in ['wpawn', 'bpawn']:
            return False
        elif board_values.count(colored_figure) <=2:
            board_keys = list(board.keys())
            if not set(board_keys).issubset(set(key_combinations)):
                return False
            else:
                if colored_figure == 'wking' or colored_figure == 'bking':
                    return board_values.count(colored_figure) <= 1

    return True

print(isValidChessboard({'1h':'bking', '2g':'bking'}))
