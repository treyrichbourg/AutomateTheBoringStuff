#Define a function to tell if chess board is valid, return True or False
#black/white = 16 pieces max CHECK 
#8 pawns max per side
#2 max knight, bishop, rook
#1 queen/king
#each side must have 1 king or game is over CHECK
#all pieces must be within 1a-8h

def is_valid_chess_board(chess_dict):
    #count pieces in dict
    count = {} #create empty dict to hold our count
    for p in chess_dict.values():
        count.setdefault(p, 0) 
        count[p] += 1
    
    #check for kings
    if 'bking' not in count.keys() or 'wking' not in count.keys():
        return False 

    #count pieces per side
    black, white = 0, 0
    for c in count.keys():
        if c[0] == 'b':
            black += 1
        elif c[0] == 'w':
            white += 1
        else:
            return False
    if black >= 17 or white >= 17:
        return False

    #validate number of pieces
    for pieces in count.keys():
        if 'bpawn' or 'wpawn' 

