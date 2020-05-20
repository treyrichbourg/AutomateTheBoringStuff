#Define a function to tell if chess board is valid, return True or False
#black/white = 16 pieces max CHECK 
#8 pawns max per side
#2 max knight, bishop, rook
#1 queen/king
#each side must have 1 king or game is over CHECK
#all pieces must be within 1a-8h

board_keys = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
              'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
              'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
              'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
              'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
              'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
              'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
              'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

piece_set = {'bpawn': 8, 'bknight': 2, 'bbishop': 2, 'brook': 2, 'bqueen': 1, 'bking': 1,
             'wpawn': 8, 'wknight': 2, 'wbishop': 2, 'wrook': 2, 'wqueen': 1, 'wking': 1}

#can I check to see if there are 16 pieces max each side?  
def black_white(chess_dict):
    black = 0
    white = 0
    for colors in chess_dict.values():
        if 'b' in colors:
            black += 1
        elif 'w' in colors:
            white += 1
    if black >= 17:
        return False
    elif white >= 17:
        return False
    else:
        return True


#trials
# trial = {"h1": "bking", "c6": "wqueen", "g2": "bbishop", "h5": "bqueen", "e3": "wking"}))  # True
# trial2 = {"a1": "bpawn", "a2": "wking"}))  # False: no bking
# trial3 = {"a1": "wking", "a2": "wking", "c3": "bbishop"}))  # False: cannot have 2 white kings, no bking
# trial4 = {"a1": "bking", "z9": "wking"}))  # False: z9 is an invalid position
# trial5 = {'a1':'bking','a2':'wking','h1':'bpawn','h2':'bpawn','h3':'bpawn','h4':'bpawn','h5':'bpawn','h6':'bpawn','h7':'bpawn','h8':'bpawn','g7':'bpawn','g8':'bpawn'}))#False theres more than 8 pawns
# trial6 = {"a1": "wking", "a2": "wking", "c3": "bbishop", "c4": "bking"})) # False: cannot have 2 white kings and 1 black king