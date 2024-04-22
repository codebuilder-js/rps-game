A Rock, Paper, Scissors Game

This program uses a while loop inside of another while loop. The first 
loop is the main game loop, and a single game of rock, paper, scissors 
is played on each iteration through this loop. The second loop asks for 
input from the player, and keeps looping until the player has entered 
an r, p, s, or q for their move. The r, p, and s correspond to rock, 
paper, and scissors, respectively, while the q means the player intends 
to quit. In that case, sys.exit() is called and the program exits. If 
the player has entered r, p, or s, the execution breaks out of the loop. 
Otherwise, the program reminds the player to enter r, p, s, or q and goes 
back to the start of the loop.