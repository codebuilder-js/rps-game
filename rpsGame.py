import random, sys

print('<--- ROCK, PAPER, SCISSORS --->')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins | %s Losses | %s Ties' % (wins, losses, ties))

    while True:
        playerMove = input('> Enter (r)ock, (p)aper, (s)cissors or (q)uit: ')

        if playerMove == 'q':
            sys.exit()

        if playerMove == 'r' or \
            playerMove == 'p' or \
            playerMove == 's':
            break

        print('Please, type only the letters in parentheses...')

    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif (playerMove == 'r' and computerMove == 's') or \
         (playerMove == 'p' and computerMove == 'r') or \
         (playerMove == 's' and computerMove == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1
