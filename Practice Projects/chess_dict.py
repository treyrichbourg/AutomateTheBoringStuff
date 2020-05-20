#Define a function to tell if chess board is valid, return True or False
#black/white = 16 pieces max CHECK 
#8 pawns max per side
#2 max knight, bishop, rook
#1 queen/king
#each side must have 1 king or game is over CHECK
#all pieces must be within 1a-8h

count = {}
#count all pieces in the dictionary and put in dict with all pieces available
def count_pieces(chess_dict):
    pieces_available = ['bking', 'wking', 'bqueen', 'wqueen', 'bpawn', 'wpawn', 'bknight', 'wknight', 'bbishop', 'wbishop', 'brook', 'wrook'] 
    for pieces in pieces_available:
        count.setdefault(pieces, 0)
    for p in chess_dict.values():
        count[p] += 1
#check for kings
def kings(k):
    if k['bking'] and k['wking'] != 1:
        return False
#check for rest of pieces
def checker(players):
    if ('bqueen' in count) and ('wqueen' in count) in range(2):
        pass
    if ('bpawn' in count) and ('wpawn' in count) in range(9):
        pass
    if ('bknight' in count) and ('wknight' in count) and ('bbishop' in count) and ('wbishop' in count) and ('brook' in count) and ('wrook' in count) in range(3):
        pass
    else:
        return False    
    

def main(chess_dict):
    count_pieces(chess_dict)
    kings(count)
    if False:
        print('False')

trial = {'h1': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen', 'e3': 'wking'}
trial2 = {'h1': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen'}
trial3 = {'g2': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen', 'e3': 'wking'}
trial4 = {'h1': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen', 'e3': 'wking', 'c7':'bbishop'}
main(trial)
main(trial2)
main(trial3)
main(trial4)