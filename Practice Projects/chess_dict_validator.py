#Board must have exactly one black king and one white king.  Each player can only have 16 pieces, at most 8 pawns and all pieces must be on a valid space.  
#Available spaces on the chess board
board_keys = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
              'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
              'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
              'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
              'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
              'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
              'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
              'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
#Check if all spaces are valid on the chess board
def valid_space(board_dict):
    for s in board_dict:
        if s not in board_keys:
            return False
#Check to see if there is a black and white king on the board
def king_check(board_dict):
    if 'bking' not in board_dict.values() or 'wking' not in board_dict.values():
        return False
    else:
        return True
#Set of all possible pieces on the board
piece_set = {'bpawn': 8, 'bknight': 2, 'bbishop': 2, 'brook': 2, 'bqueen': 1, 'bking': 1,
             'wpawn': 8, 'wknight': 2, 'wbishop': 2, 'wrook': 2, 'wqueen': 1, 'wking': 1}
#Count pieces in the dictionary in question
count = {}
def count_pieces(chess_dict):
    for count_new in chess_dict.values():
        if count_new in piece_set:
            count.setdefault(count_new, 0)
            count[count_new] += 1
#Create a function to ensure the pieces counted are within the valid range
def test(count, piece_set):
    for k in count:
        if piece_set[k] < count[k]:
            return False
#Main Validator function
def is_valid_chess_board(chess_dict, dict2):
    if king_check(chess_dict) and valid_space(chess_dict):
        count_pieces(chess_dict)
    if test(chess_dict, dict2):
        print('The board is valid')
    else:
        print('Invalid Board')

count = {}
#count all pieces in the dictionary and put in dict with all pieces available
def count_pieces(chess_dict):
    pieces_available = ['bking', 'wking', 'bqueen', 'wqueen', 'bpawn', 'wpawn', 'bknight', 'wknight', 'bbishop', 'wbishop', 'brook', 'wrook'] 
    for pieces in pieces_available:
        count.setdefault(pieces, 0)
    for p in chess_dict.values():
        count[p] += 1

  
trial = {'h1': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen', 'e3': 'wking'}
trial2 = {'h1': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen'}
trial3 = {'g2': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen', 'e3': 'wking'}
trial4 = {'h1': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen', 'e3': 'wking', 'c7':'bbishop'}
print(is_valid_chess_board(trial, count))
print(is_valid_chess_board(trial2, count))



