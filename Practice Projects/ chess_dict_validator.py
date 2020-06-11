# Define a function to tell if chess board is valid, return True or False
# black/white = 16 pieces max CHECK
# 8 pawns max per side CHECK
# 2 max knight, bishop, rook CHECK
# 1 queen/king CHECK
# each side must have 1 king or game is over CHECK
# all pieces must be within 1a-8h CHECK

# board keys hardcoded
# board_keys = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
#               'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
#               'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
#               'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
#               'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
#               'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
#               'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
#               'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

# board_keys with list comp
# board_keys = [x + str(y) for x in 'abcdefgh' for y in range(1,9)]

# board_keys list comp fstr
board_keys = [f"{ch}{i}" for ch in "abcdefgh" for i in range(1, 9)]

piece_set = {
    "bpawn": 8,
    "bknight": 2,
    "bbishop": 2,
    "brook": 2,
    "bqueen": 1,
    "bking": 1,
    "wpawn": 8,
    "wknight": 2,
    "wbishop": 2,
    "wrook": 2,
    "wqueen": 1,
    "wking": 1,
}

# can I check to see if there are 16 pieces max each side?
def black_white(chess_dict):
    num_black_pieces = [piece[0] for piece in chess_dict.values()].count("b")
    # Sprint(num_black_pieces)
    num_white_pieces = [piece[0] for piece in chess_dict.values()].count("w")
    # print(num_white_pieces)
    if num_black_pieces > 16:
        return False
    elif num_white_pieces > 16:
        return False
    else:
        return True


# check to see if both kings are alive
def two_kings_alive(chess_dict):
    pieces_on_board = []
    for space in board_keys:
        if chess_dict.get(space):
            pieces_on_board.append(chess_dict.get(space))
    return ("bking" in pieces_on_board) and ("wking" in pieces_on_board)


# check to make sure each side has the proper number of pieces allowed
def count_pieces(chess_dict):
    # count all pieces in the dictionary and put in dict with all pieces available
    pieces_on_board = {}
    pieces_available = [
        "bking",
        "wking",
        "bqueen",
        "wqueen",
        "bpawn",
        "wpawn",
        "bknight",
        "wknight",
        "bbishop",
        "wbishop",
        "brook",
        "wrook",
    ]
    for piece in pieces_available:
        pieces_on_board.setdefault(piece, 0)
    for piece in chess_dict.values():
        pieces_on_board[piece] += 1
    return pieces_on_board


# check to make sure the number of each piece in the dictinary is within the range of allowed pieces in the game
def number_of_each_piece(chess_dict):
    valid_number = 0
    invalid_number = 0
    pieces_counted = count_pieces(chess_dict)
    for piece in pieces_counted:
        if piece_set[piece] < pieces_counted[piece]:
            invalid_number += 1
        else:
            valid_number += 1
    if invalid_number >= 1:
        return False
    else:
        return True


# Are the pieces within the coords of the board
def valid_space(chess_dict):
    invalid_coord = 0
    for coord in chess_dict:
        if coord not in board_keys:
            invalid_coord += 1
    if invalid_coord >= 1:
        return False
    else:
        return True


def main(chess_dict):
    # print(pieces_counted)
    return (
        black_white(chess_dict),
        two_kings_alive(chess_dict),
        number_of_each_piece(chess_dict),
        valid_space(chess_dict),
    )


# trials
trial = {
    "h1": "bking",
    "c6": "wqueen",
    "g2": "bbishop",
    "h5": "bqueen",
    "e3": "wking",
}  # True
trial2 = {"a1": "bpawn", "a2": "wking"}  # False: no bking
trial3 = {
    "a1": "wking",
    "a2": "wking",
    "c3": "bbishop",
}  # False: cannot have 2 white kings, no bking
trial4 = {"a1": "bking", "z9": "wking"}  # False: z9 is an invalid position
trial5 = {
    "a1": "bking",
    "a2": "wking",
    "h1": "bpawn",
    "h2": "bpawn",
    "h3": "bpawn",
    "h4": "bpawn",
    "h5": "bpawn",
    "h6": "bpawn",
    "h7": "bpawn",
    "h8": "bpawn",
    "g7": "bpawn",
    "g8": "bpawn",
}  # False theres more than 8 pawns
trial6 = {
    "a1": "wking",
    "a2": "wking",
    "c3": "bbishop",
    "c4": "bking",
}  # False: cannot have 2 white kings and 1 black king
trial7 = {
    "a1": "bking",
    "a2": "wking",
    "h1": "bpawn",
    "h2": "bpawn",
    "h3": "bpawn",
    "h4": "bpawn",
    "h5": "bpawn",
    "h6": "bpawn",
    "h7": "bpawn",
    "h8": "bpawn",
    "g7": "bpawn",
    "g8": "bpawn",
    "b2": "brook",
    "b3": "bknight",
    "b4": "brook",
    "b5": "bknight",
    "b6": "bbishop",
    "b7": "bbishop",
    "b8": "bqueen",
}  # False theres more than 16 black pieces
trial8 = {
    "a1": "wking",
    "a2": "wking",
    "h1": "wpawn",
    "h2": "wpawn",
    "h3": "wpawn",
    "h4": "wpawn",
    "h5": "wpawn",
    "h6": "wpawn",
    "h7": "wpawn",
    "h8": "wpawn",
    "g7": "wpawn",
    "g8": "wpawn",
    "b2": "wrook",
    "b3": "wknight",
    "b4": "wrook",
    "b5": "wknight",
    "b6": "wbishop",
    "b7": "wbishop",
    "b8": "bqueen",
}

print(main(trial))
print(main(trial2))
print(main(trial3))
print(main(trial4))
print(main(trial5))
print(main(trial6))
print(main(trial7))
print(main(trial8))
