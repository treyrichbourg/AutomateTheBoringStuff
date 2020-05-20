all_spaces = [f"{ch}{i}" for ch in 'abcdefgh' for i in range(1,9)]
pieces_on_board = []

def king_check(chess_dict):
    pieces_on_board = []
    for space in all_spaces:
        if chess_dict.get(space):
            pieces_on_board.append(chess_dict.get(space))
    #print(pieces_on_board)
    return ('bking' in pieces_on_board) and ('wking' in pieces_on_board)
def main(chess_dict):
    while True:
        king_check(chess_dict)
        return True
    else:
        return False

trial = {'h1': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen', 'e3': 'wking'}
trial2 = {'h1': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen'}

print(main(trial))
print(main(trial2))
#print(is_chess_board_valid(trial2))














# def is_chess_board_valid(chess_dict):
#     all_spaces = [f"{ch}{i}" for ch in 'abcdefgh' for i in range(1,9)]
#     piece_set = {'bpawn': 8, 'bknight': 2, 'bbishop': 2, 'brook': 2, 'bqueen': 1, 'bking': 1,
#                  'wpawn': 8, 'wknight': 2, 'wbishop': 2, 'wrook': 2, 'wqueen': 1, 'wking': 1}
#     def king_checker(chess_dict):
#         pieces_on_board = []
#         for space in all_spaces:
#             if chess_dict.get(space):
#                 pieces_on_board.append(chess_dict.get(space))
#         return ('bking' in pieces_on_board) and ('wking' in pieces_on_board)
#     king_checker_results = king_checker(chess_dict)
#     #print(king_checker_results)
# def king_checker(chess_dict):
    