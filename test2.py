import random
import sys
print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print('Type one of r, p, s, or q.')
    if player_move == 'r':
        print('ROCK Versus...')
    elif player_move == 'p':
        print('PAPER Versus...')
    elif player_move == 's':
        print('SCISSORS Versus...')

    ran = random.randint(1, 3)
    if ran == 1:
        comp_move = 'r'
        print('ROCK')
    elif ran == 2:
        comp_move = 'p'
        print('PAPER')
    elif ran == 3:
        comp_move = 's'
        print('SCISSORS')

    if player_move == comp_move:
        print("IT'S A TIE!")
        ties += 1
    elif player_move == 'r' and comp_move == 's':
        print('You win!')
        wins += 1
    elif player_move == 'p' and comp_move == 'r':
        print('You win!')
        wins += 1
    elif player_move == 's' and comp_move == 'p':
        print('You win!')
        wins += 1
    elif player_move == 'r' and comp_move == 'p':
        print('You lose!')
        losses += 1
    elif player_move == 'p' and comp_move == 's':
        print('You lose!')
        losses += 1
    elif player_move == 's' and comp_move == 'r':
        print('You lose!')
        losses += 1
